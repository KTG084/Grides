import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, RobustScaler
from sentence_transformers import SentenceTransformer
import joblib
import warnings
warnings.filterwarnings('ignore')

print("🚀 Initializing V8.2 TITAN Pipeline (Fixing Road Closure Imbalance)...")

# --- 1. DATA INGESTION & PREPROCESSING ---
filepath = "Astram event data_anonymized - Astram event data_anonymizedb40ac87.csv"
df = pd.read_csv(filepath)

df['start_datetime'] = pd.to_datetime(df['start_datetime'], errors='coerce', utc=True)
df['closed_datetime'] = pd.to_datetime(df['closed_datetime'], errors='coerce', utc=True)
df['resolved_datetime'] = pd.to_datetime(df['resolved_datetime'], errors='coerce', utc=True)
df['end_time_proxy'] = df['resolved_datetime'].fillna(df['closed_datetime'])
df['actual_duration_mins'] = (df['end_time_proxy'] - df['start_datetime']).dt.total_seconds() / 60
df = df[(df['actual_duration_mins'] > 0) & (df['actual_duration_mins'] < 1440)]

df['description'] = df['description'].fillna("standard traffic event")
df['requires_road_closure'] = df['requires_road_closure'].fillna(False).astype(bool)

def calculate_ground_truth_severity(row):
    score = min(100, (row['actual_duration_mins'] / 120) * 50)
    if row['priority'] == 'High': score += 30
    if row['requires_road_closure'] == True: score += 20
    return min(100.0, score)

df['ground_truth_severity'] = df.apply(calculate_ground_truth_severity, axis=1)

df['hour'] = df['start_datetime'].dt.hour
df['day_of_week'] = df['start_datetime'].dt.dayofweek
df['is_weekend'] = df['day_of_week'].apply(lambda x: 1.0 if x >= 5 else 0.0)

df['hour_sin'] = np.sin(2 * np.pi * df['hour']/24)
df['hour_cos'] = np.cos(2 * np.pi * df['hour']/24)
df['day_sin'] = np.sin(2 * np.pi * df['day_of_week']/7)
df['day_cos'] = np.cos(2 * np.pi * df['day_of_week']/7)

cat_features = ['event_cause', 'veh_type']
spatial_features = ['latitude', 'longitude']
time_features = ['hour_sin', 'hour_cos', 'day_sin', 'day_cos']
bool_features = ['is_weekend']

all_tabular_features = cat_features + spatial_features + time_features + bool_features
df = df.dropna(subset=all_tabular_features + ['actual_duration_mins', 'ground_truth_severity', 'requires_road_closure'])

# --- ENCODING & SCALING ---
encoders = {}
embedding_sizes = []

for col in cat_features:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))
    encoders[col] = le
    num_classes = len(le.classes_)
    emb_dim = min(50, (num_classes + 1) // 2)
    embedding_sizes.append((num_classes, emb_dim))

scaler = RobustScaler()
df[spatial_features] = scaler.fit_transform(df[spatial_features])

joblib.dump({'encoders': encoders, 'scaler': scaler, 'embedding_sizes': embedding_sizes}, "preprocessors.pkl")

X_cat = df[cat_features].values
X_spatial = df[spatial_features].values
X_time = df[time_features].values
X_bool = df[bool_features].values.astype(float)

y_dur = np.log1p(df['actual_duration_mins'].values)
y_sev = df['ground_truth_severity'].values
y_closure = df['requires_road_closure'].values.astype(float)

# CALCULATE CLASS IMBALANCE FOR ROAD CLOSURES
# Because mostly false, we need to weight the 'True' class so the AI doesn't ignore it
num_positive = np.sum(y_closure)
num_negative = len(y_closure) - num_positive
pos_weight_val = torch.tensor([num_negative / num_positive], dtype=torch.float32)
print(f"⚖️ Calculated Road Closure Positive Weight: {pos_weight_val.item():.2f}")

print("📚 Generating NLP Vector Embeddings for Text Descriptions...")
nlp_model = SentenceTransformer('all-MiniLM-L6-v2')
X_text = nlp_model.encode(df['description'].tolist(), show_progress_bar=True)

indices = np.arange(len(df))
train_idx, test_idx = train_test_split(indices, test_size=0.2, random_state=42)

# --- 2. THE NEURAL ARCHITECTURE ---
class FourierSpatialEncoding(nn.Module):
    def __init__(self, input_dim=2, num_frequencies=16):
        super().__init__()
        self.B = nn.Parameter(torch.randn(input_dim, num_frequencies) * 10, requires_grad=False)
    def forward(self, x):
        x_proj = 2 * np.pi * torch.matmul(x, self.B)
        return torch.cat([torch.sin(x_proj), torch.cos(x_proj)], dim=-1)

class GatedResidualNetwork(nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.fc1 = nn.Linear(dim, dim)
        self.fc2 = nn.Linear(dim, dim * 2)
        self.norm = nn.LayerNorm(dim)
    def forward(self, x):
        h = F.gelu(self.fc1(x))
        gate, out = self.fc2(h).chunk(2, dim=-1)
        return self.norm((out * torch.sigmoid(gate)) + x)

class V8TitanNet(nn.Module):
    def __init__(self, embedding_sizes, num_time, num_bool, nlp_dim=384, fourier_freqs=16, hidden_dim=128):
        super().__init__()
        self.embeddings = nn.ModuleList([nn.Embedding(nc, ed) for nc, ed in embedding_sizes])
        n_emb = sum(ed for _, ed in embedding_sizes)
        self.spatial_encoder = FourierSpatialEncoding(input_dim=2, num_frequencies=fourier_freqs)
        n_spatial = fourier_freqs * 2

        self.tabular_proj = nn.Linear(n_emb + n_spatial + num_time + num_bool, hidden_dim)
        self.nlp_proj = nn.Linear(nlp_dim, hidden_dim)
        self.attention = nn.MultiheadAttention(embed_dim=hidden_dim, num_heads=4, batch_first=True)

        self.deep = nn.Sequential(
            GatedResidualNetwork(hidden_dim),
            nn.Dropout(0.3),
            GatedResidualNetwork(hidden_dim)
        )

        self.severity_head = nn.Sequential(nn.Linear(hidden_dim, 32), nn.ReLU(), nn.Linear(32, 1))
        self.duration_mu = nn.Linear(hidden_dim, 1)
        self.duration_sigma = nn.Linear(hidden_dim, 1)
        self.closure_head = nn.Sequential(nn.Linear(hidden_dim, 32), nn.ReLU(), nn.Linear(32, 1))

    def forward(self, x_cat, x_spatial, x_time, x_bool, x_text):
        x_emb = [emb_layer(x_cat[:, i]) for i, emb_layer in enumerate(self.embeddings)]
        x_emb = torch.cat(x_emb, 1)
        x_spat_encoded = self.spatial_encoder(x_spatial)

        x_tab_all = torch.cat([x_emb, x_spat_encoded, x_time, x_bool], 1)
        x_tab = F.gelu(self.tabular_proj(x_tab_all))
        x_txt = F.gelu(self.nlp_proj(x_text))

        x_stacked = torch.stack([x_tab, x_txt], dim=1)
        attn_out, _ = self.attention(x_stacked, x_stacked, x_stacked)
        x_fused = attn_out.mean(dim=1)
        x_out = self.deep(x_fused)

        severity = torch.sigmoid(self.severity_head(x_out)) * 100
        mu = self.duration_mu(x_out)
        sigma = F.softplus(self.duration_sigma(x_out)) + 1e-6
        closure_logits = self.closure_head(x_out)
        return severity, mu, sigma, closure_logits

def make_tensor(data, dtype=torch.float32): return torch.tensor(data, dtype=dtype)

train_dataset = TensorDataset(
    make_tensor(X_cat[train_idx], torch.long),
    make_tensor(X_spatial[train_idx]),
    make_tensor(X_time[train_idx]),
    make_tensor(X_bool[train_idx]),
    make_tensor(X_text[train_idx]),
    make_tensor(y_sev[train_idx]).unsqueeze(1),
    make_tensor(y_dur[train_idx]).unsqueeze(1),
    make_tensor(y_closure[train_idx]).unsqueeze(1)
)
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)

dl_model = V8TitanNet(embedding_sizes, num_time=X_time.shape[1], num_bool=X_bool.shape[1])

log_var_sev = torch.zeros((1,), requires_grad=True)
log_var_dur = torch.zeros((1,), requires_grad=True)
log_var_clos = torch.zeros((1,), requires_grad=True)

optimizer = optim.AdamW(list(dl_model.parameters()) + [log_var_sev, log_var_dur, log_var_clos], lr=0.001, weight_decay=1e-4)
scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, 'min', patience=5, factor=0.5)

criterion_severity = nn.HuberLoss()
criterion_duration_nll = nn.GaussianNLLLoss()
# FIX: Added pos_weight to force the AI to learn Road Closures
criterion_closure = nn.BCEWithLogitsLoss(pos_weight=pos_weight_val)

epochs = 60
print("⚙️ Training V8.2 Titan...")
for epoch in range(epochs):
    dl_model.train()
    epoch_loss = 0
    for b_cat, b_spat, b_time, b_bool, b_text, b_sev, b_dur, b_clos in train_loader:
        optimizer.zero_grad()
        p_sev, p_mu, p_sigma, p_clos = dl_model(b_cat, b_spat, b_time, b_bool, b_text)

        precision_sev = torch.exp(-log_var_sev)
        loss_sev = precision_sev * criterion_severity(p_sev, b_sev) + log_var_sev

        precision_dur = torch.exp(-log_var_dur)
        loss_dur = precision_dur * criterion_duration_nll(p_mu, b_dur, p_sigma**2) + log_var_dur

        precision_clos = torch.exp(-log_var_clos)
        loss_clos = precision_clos * criterion_closure(p_clos, b_clos) + log_var_clos

        loss = loss_sev + loss_dur + loss_clos

        loss.backward()
        torch.nn.utils.clip_grad_norm_(dl_model.parameters(), max_norm=1.0)
        optimizer.step()
        epoch_loss += loss.item()

    scheduler.step(epoch_loss)
    if (epoch + 1) % 10 == 0:
        print(f"   Epoch [{epoch+1}/{epochs}], Total Loss: {epoch_loss/len(train_loader):.4f}")

torch.save(dl_model.state_dict(), "v8_dl_model.pth")
print("✅ V8.2 Training Complete. Road Closure Logic Fixed.")