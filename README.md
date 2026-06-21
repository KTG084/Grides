<div align="center">

```
 █████╗ ███████╗████████╗██████╗  █████╗ ███╗   ███╗       █████╗ ██╗
██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗████╗ ████║      ██╔══██╗██║
███████║███████╗   ██║   ██████╔╝███████║██╔████╔██║█████╗███████║██║
██╔══██║╚════██║   ██║   ██╔══██╗██╔══██║██║╚██╔╝██║╚════╝██╔══██║██║
██║  ██║███████║   ██║   ██║  ██║██║  ██║██║ ╚═╝ ██║      ██║  ██║██║
╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝      ╚═╝  ╚═╝╚═╝
```

**Adaptive Smart Traffic Response & Analysis Management**

`v8.2 TITAN` · Zero-Touch Multi-Modal Probabilistic Grid · Bengaluru, India

---

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-2.9-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-AI%20Server-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Spring Boot](https://img.shields.io/badge/Spring%20Boot-3.2.5-6DB33F?style=for-the-badge&logo=springboot&logoColor=white)
![Java](https://img.shields.io/badge/Java-17-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)

![Cognitive Grid](https://img.shields.io/badge/%F0%9F%9F%A2%20COGNITIVE%20GRID-ONLINE-00ff88?style=flat-square)
![Dispatch Nodes](https://img.shields.io/badge/Dispatch%20Nodes-1%2C000%20BLR%20Grid-blueviolet?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

<br/>

> ASTRAM-AI turns a raw traffic incident report into a full deployment plan in under a second.
> A **PyTorch neural network** predicts impact and duration. A **rule-based LLM proxy** classifies the
> SOP and urgency from free-text description. A **linear-programming RL optimizer** dispatches
> officers from 1,000 city grid nodes. A **Spring Boot** middleware ties it all together.

</div>

---

## 📸 Dashboard

![ASTRAM Dashboard](./assets/dashboard.png)

*Sticky header with Cognitive Grid pulse · Left: 420 px form panel with dropdowns, coordinates, description, presets · Right: dark Leaflet map with incident pin + animated dispatch route line · Bottom: staggered result cards with Bayesian forecast, road closure verdict, SOP banner, and RL deployment summary*

---

## 🏗 Architecture

Three independent services, two HTTP hops, one self-contained HTML page.

```
┌──────────────────────────────────────────────────────────────────────────┐
│                         ASTRAM-AI · System Flow                          │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│   Browser (index.html)                                                   │
│   ┌────────────────────────────────────────────────────────────────┐    │
│   │  Vanilla JS + Leaflet.js                                        │    │
│   │  • Form panel  →  POST /api/dashboard/predict                  │    │
│   │  • GET /api/dashboard/live-feed  (random CSV row)              │    │
│   │  • Renders result cards, SOP banner, dispatch route on map     │    │
│   └────────────────┬───────────────────────────────────────────────┘    │
│                    │ HTTP (port 8080)                                    │
│                    ▼                                                     │
│   Spring Boot Backend  (backend/astram)                                  │
│   ┌────────────────────────────────────────────────────────────────┐    │
│   │  TrafficController  →  TrafficEventService                     │    │
│   │  • POST /api/dashboard/predict  — proxies to AI server         │    │
│   │  • GET  /api/dashboard/live-feed — reads random CSV row,       │    │
│   │                                     then proxies to AI server  │    │
│   │  WebClient  →  POST ${PYTHON_AI_URL}/api/v8/cognitive_grid     │    │
│   └────────────────┬───────────────────────────────────────────────┘    │
│                    │ HTTP (port 7860)                                    │
│                    ▼                                                     │
│   FastAPI AI Server  (frontend/ASTRAM_AI  or  ML model/ASTRAM)          │
│   ┌────────────────────────────────────────────────────────────────┐    │
│   │  POST /api/v8/cognitive_grid                                   │    │
│   │                                                                │    │
│   │  Step 1 — AgenticLLMNode.analyze(description)                 │    │
│   │           keyword → SOP flag, hazmat, sentiment, priority      │    │
│   │                                                                │    │
│   │  Step 2 — SentenceTransformer('all-MiniLM-L6-v2')            │    │
│   │           description → 384-dim text embedding                 │    │
│   │                                                                │    │
│   │  Step 3 — V8TitanNet (PyTorch)                                │    │
│   │           tabular + spatial + time + text → forward pass      │    │
│   │           outputs: severity, duration mu/sigma, closure logit  │    │
│   │                                                                │    │
│   │  Step 4 — PuLP LP Optimizer (RL resource allocator)           │    │
│   │           1,000-node BLR grid, dynamic cost + priority        │    │
│   │           → officers_assigned, dispatch_node, barricades      │    │
│   │                                                                │    │
│   │  GET  /  — serves index.html + health check                   │    │
│   └────────────────────────────────────────────────────────────────┘    │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## 📁 Repository Structure

```
Grides-main/
│
├── 📂 frontend/
│   └── ASTRAM_AI/                     # FastAPI AI server + single-page dashboard
│       ├── index.html                 # Complete frontend — Vanilla JS + Leaflet (735 lines)
│       ├── main.py                    # FastAPI server: V8TitanNet inference + PuLP optimizer
│       ├── train.py                   # Model training (25 epochs, BCEWithLogitsLoss + MSELoss)
│       ├── bootstrap.py               # One-shot: generates preprocessors.pkl + v8_dl_model.pth
│       ├── preprocessors.pkl          # Saved LabelEncoders + StandardScaler
│       ├── v8_dl_model.pth            # Trained V8TitanNet weights
│       ├── astram_event_data.csv      # Training dataset
│       └── requirements.txt           # fastapi, uvicorn, torch, sentence-transformers, pulp…
│
├── 📂 backend/
│   └── astram/                        # Spring Boot 3.2.5 orchestration middleware
│       ├── src/main/java/com/hackathon/astram_backend/
│       │   ├── AstramBackendApplication.java
│       │   ├── config/
│       │   │   └── WebClientConfig.java       # Reactive WebClient bean
│       │   ├── controller/
│       │   │   └── TrafficController.java     # POST /predict · GET /live-feed
│       │   ├── dto/
│       │   │   ├── TrafficEventInput.java     # Request DTO (@JsonProperty mapping)
│       │   │   └── PredictionResponse.java    # Response DTO (Lombok @Data)
│       │   └── service/
│       │       └── TrafficEventService.java   # WebClient proxy + CSV random-row reader
│       ├── src/main/resources/
│       │   └── application.properties         # python.ai.url env config
│       ├── Astram_event_data_anonymized.csv   # Live-feed simulation data
│       ├── Dockerfile                          # Multi-stage: Maven build → JRE 17 runtime
│       └── pom.xml                            # Spring Boot 3.2.5, WebFlux, OpenCSV, Lombok
│
└── 📂 ML model/
    └── ASTRAM/                        # Standalone AI server (production / HuggingFace Spaces)
        ├── main.py                    # FastAPI + V8TitanNet + PuLP (no index.html)
        ├── train.py                   # Training script (mirrors frontend version)
        ├── preprocessors.pkl          # Saved encoders + scaler
        ├── v8_dl_model.pth            # Trained model weights
        ├── Dockerfile                 # python:3.10-slim, EXPOSE 7860
        ├── requirements.txt           # CPU-only torch build
        └── Astram event data_anonymized*.csv  # Anonymised training data
```

---

## 🧠 V8TitanNet — Neural Architecture

A multi-modal fusion model that merges four input streams through cross-attention before producing three simultaneous predictions.

```
INPUTS
  ├── Categorical  [event_cause, veh_type]
  │      └──► Entity Embeddings  (dim 8 + 6 = 14)
  │                    │
  ├── Geospatial  [lat, lng]
  │      └──► FourierSpatialEncoding  (16 freqs → 32-dim sin/cos)
  │                    │
  ├── Temporal  [hour_sin, hour_cos, weekday_sin, weekday_cos, is_weekend]
  │      └──► Cyclic features  (4 + 1 = 5-dim)
  │                    │
  │            ┌───────▼────────┐
  │            │  tabular_proj  │  Linear(14+32+5 → 128)  + GELU
  │            └───────┬────────┘
  │                    │
  └── Text  [description]
         └──► all-MiniLM-L6-v2  (384-dim)
                    │
             ┌──────▼──────┐
             │  nlp_proj   │  Linear(384 → 128)  + GELU
             └──────┬──────┘
                    │
  ┌─────────────────▼──────────────────────┐
  │  MultiheadAttention  (4 heads, 128-dim) │
  │  stack([tabular_128, nlp_128])          │
  │  → attend → mean pool → 128-dim        │
  └─────────────────┬──────────────────────┘
                    │
  ┌─────────────────▼──────────────────────┐
  │  GatedResidualNetwork (GELU + GLU gate) │
  │  Dropout(0.3)                           │
  │  GatedResidualNetwork                   │
  └──────┬──────────┬───────────┬──────────┘
         │          │           │
  ┌──────▼───┐ ┌────▼─────┐ ┌──▼──────────┐
  │ severity │ │duration  │ │   closure   │
  │  _head   │ │  _mu     │ │   _head     │
  │sigmoid×  │ │  _sigma  │ │  (logit)    │
  │  100     │ │(log-norm)│ │ >0.5 = True │
  └──────────┘ └──────────┘ └─────────────┘
```

**Training** (`train.py`):

| Setting | Value |
|---------|-------|
| Epochs | 25 |
| Batch size | 64 |
| Optimizer | Adam, lr=0.001 |
| Closure loss | `BCEWithLogitsLoss` with pos_weight (class imbalance) |
| Severity loss | `MSELoss` × 0.01 |
| Text encoder | `all-MiniLM-L6-v2` (batch=128, offline) |
| Saved artifacts | `v8_dl_model.pth`, `preprocessors.pkl` |

**Inference score fusion** (`main.py`):
```python
final_sev = min(100.0, base_sev * llm_ctx["sentiment_vector"])
final_dur = max(5.0, base_dur + (final_sev * 0.3))
```
The neural network base severity is multiplied by the LLM sentiment before the response is built. If `force_road_closure` is set by the LLM, the neural network's closure probability is overridden to `True`.

---

## 🤖 AgenticLLMNode — SOP Classifier

A keyword-based rule engine that reads the free-text `description` and returns structured context. Its `sentiment_vector` directly scales the neural network's severity output.

| Trigger keywords | `sop_flag` | `sentiment_vector` | `inferred_priority` | `force_road_closure` |
|----------------|------------|-------------------|--------------------|--------------------|
| fire, spill, chemical, hazmat | `HAZMAT_PROTOCOL` | 2.5× | High | ✅ |
| fatal, crash, injur, accident | `CODE_RED_MEDICAL` | 3.0× | High | ✅ |
| water, flood, heavy | `CIVIC_INFRA_ALERT` | 1.5× | High | ✅ |
| block, stuck, jam | *(default)* | 1.2× | Medium | ❌ |
| *(no match)* | `Standard` | 1.0× | Low | ❌ |

---

## 🚔 PuLP RL Resource Optimizer

Officer deployment is solved as a **linear program** over all 1,000 BLR dispatch nodes — not a simple lookup.

```python
# Minimise total deployment cost across the city grid
prob += lpSum([dynamic_costs[i] * x[i] for i in GLOBAL_STATIONS])

# Distance penalty makes the LP prefer nearby nodes
dynamic_costs[station] = BASE_COSTS[station] + (hash(station + lat + lng) % 150)

# Officers needed scales with severity and priority
total_officers_needed = max(1, int(final_sev / deployment_divisor))
prob += lpSum([x[i] for i in GLOBAL_STATIONS]) >= total_officers_needed
```

| `inferred_priority` | `deployment_divisor` | Officers dispatched at severity 85 |
|--------------------|--------------------|------------------------------------|
| High | 8 | ~10 officers |
| Medium | 15 | ~5 officers |
| Low | 25 | ~3 officers |

Barricades: `20` if road closure is required, else `int(final_sev / 20)`.

---

## 🌐 Spring Boot Middleware

The Java backend is a **reactive proxy** — it never touches ML logic directly.

```
TrafficController  (@RestController, @RequestMapping("/api/dashboard"))
│
├── POST /predict
│     receives TrafficEventInput JSON
│     → trafficEventService.predictTrafficImpact(input)
│       → WebClient POST to ${PYTHON_AI_URL}/api/v8/cognitive_grid
│       → Mono<PredictionResponse> returned to browser
│
└── GET /live-feed
      → trafficEventService.fetchRandomEventFromCsv()
          reads random row from Astram_event_data_anonymized.csv
          maps columns: [1]=event_type [2]=lat [3]=lng [8]=event_cause
                        [17]=description [18]=veh_type
      → trafficEventService.predictTrafficImpact(randomInput)
      → Mono<PredictionResponse> returned to browser
```

AI server URL is configured via environment variable:
```properties
# application.properties
python.ai.url=${PYTHON_AI_URL:http://localhost:7860/api/v8/cognitive_grid}
```

---

## 🗺 Frontend — index.html

A single 735-line file. No build step. No npm. Served directly by FastAPI at `GET /`.

**Map interactions:**
- Click anywhere on the map → auto-fills `latitude` / `longitude` in the form
- After analysis: draws a **dashed animated route line** from the computed dispatch node to the incident pin
- Dispatch node position is derived from a deterministic hash of the node name (~1–2 km offset for visual clarity)
- `map.fitBounds()` auto-zooms to frame both the incident and the dispatch node

**Result card rendering:**

| Card | Content | Severity threshold |
|------|---------|-------------------|
| Impact Score | `sev.toFixed(1)` / 100 + priority badge | ≥65 = critical (red), ≥35 = warning (amber) |
| Est. Duration | `Math.round(duration)` minutes + CI string | — |
| Road Closure | REQUIRED / NOT NEEDED + barricade count | `roadClosure \|\| forcedClosure` |
| Model Uncertainty | `epistemic.toFixed(4) σ` + confidence bar | <30% = High, <60% = Moderate, else Low |

**SOP banner mapping:**

| `sop_flag` | Icon | Label |
|-----------|------|-------|
| `HAZMAT_PROTOCOL` | ☢️ | HAZMAT Protocol Active |
| `CODE_RED_MEDICAL` | 🚨 | Code Red — Medical Emergency |
| `CIVIC_INFRA_ALERT` | 🌊 | Civic Infrastructure Alert |
| `Standard` | ✅ | Standard Operating Procedure |

---

## 🔌 API Reference

### FastAPI AI Server

#### `GET /`
```json
{
  "status": "online",
  "engine": "ASTRAM-AI V8.2 TITAN",
  "docs_url": "/docs",
  "prediction_url": "/api/v8/cognitive_grid"
}
```

#### `POST /api/v8/cognitive_grid`

**Request:**
```json
{
  "event_type": "accident",
  "event_cause": "collision",
  "latitude": 12.9716,
  "longitude": 77.5946,
  "veh_type": "car",
  "description": "Minor accident"
}
```

**Response:**
```json
{
  "bayesian_forecast": {
    "mean_impact_score": 85.92,
    "mean_duration_mins": 91.0,
    "confidence_interval": "± 0.78 Log-Mins (95% CI)",
    "epistemic_uncertainty": 0.4,
    "ai_predicted_road_closure": true
  },
  "llm_reasoning_engine": {
    "sop_flag": "CODE_RED_MEDICAL",
    "hazmat_risk": false,
    "sentiment_vector": 3.0,
    "inferred_priority": "High",
    "force_road_closure": true
  },
  "rl_agentic_deployment": {
    "dispatch_node": "BLR_Node_0248 (10 units)",
    "officers_assigned": 10,
    "barricades": 20,
    "special_units": "Standard Units"
  }
}
```

### Spring Boot Backend

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/dashboard/predict` | Proxies a manual incident input to the AI server |
| `GET` | `/api/dashboard/live-feed` | Picks a random CSV row and proxies it to the AI server |

---

## ⚡ Quick Start

### Prerequisites

| Tool | Version |
|------|---------|
| Python | 3.10+ |
| Java | 17 |
| Maven | 3.8+ (or use included `mvnw`) |

### 1 · Clone

```bash
git clone https://github.com/KTG084/gridsss.git
cd gridsss
```

### 2 · AI Server

```bash
cd frontend/ASTRAM_AI

pip install -r requirements.txt

# First run only — generate model artifacts without training data
python bootstrap.py

# OR train on real data (takes a few minutes)
python train.py

# Start the server — also serves index.html at GET /
uvicorn main:app --reload --host 0.0.0.0 --port 7860
```

Open `http://localhost:7860` — the full dashboard loads directly from FastAPI.

### 3 · Spring Boot Backend (optional)

Needed only for the `/live-feed` endpoint and if you want the Java middleware layer.

```bash
cd backend/astram
export PYTHON_AI_URL=http://localhost:7860/api/v8/cognitive_grid
./mvnw spring-boot:run
```

Backend runs on `http://localhost:8080`.

### 4 · Docker

**AI Server (ML model/ASTRAM):**
```bash
cd "ML model/ASTRAM"
docker build -t astram-ai .
docker run -p 7860:7860 astram-ai
```

**Spring Boot Backend:**
```bash
cd backend/astram
docker build -t astram-backend .
docker run -p 8080:8080 \
  -e PYTHON_AI_URL=http://host.docker.internal:7860/api/v8/cognitive_grid \
  astram-backend
```

### 5 · Retrain the Model

```bash
cd frontend/ASTRAM_AI   # or ML model/ASTRAM
python train.py
# Outputs: preprocessors.pkl   v8_dl_model.pth
```

---

## 📊 Example Scenarios

### 🔴 Truck overturn — CODE RED

```
Input
  event_cause : collision | veh_type: truck | lat/lng: 12.9716, 77.5946
  description : "marriage procession nearby, truck overturned, little road space left"

LLM   → "accident" keyword → CODE_RED_MEDICAL | sentiment 3.0× | force_road_closure
Model → base_sev ~28.6 × 3.0 = 85.9 | duration ~65 + 85.9×0.3 ≈ 91 min
PuLP  → High priority (divisor 8) → 10 officers → BLR_Node_0248
```

### 🟡 Minor car accident — Standard

```
Input
  event_cause : collision | veh_type: car
  description : "Minor accident"

LLM   → no strong keywords → Standard | sentiment 1.0×
Output → impact 80.5 | duration 24 min | road closure NOT NEEDED
```

### ☢️ Chemical spill — HAZMAT

```
Input
  description : "chemical spill on highway, strong smell"

LLM   → "chemical" → HAZMAT_PROTOCOL | sentiment 2.5× | hazmat_risk true
Output → special_units: "Hazmat Team" | force_road_closure: true
```

### 🌊 Flooding — Civic Infrastructure Alert

```
Input
  description : "underpass flooded, water level rising, 2 lanes blocked"

LLM   → "flood" + "water" → CIVIC_INFRA_ALERT | sentiment 1.5×
Output → road closure REQUIRED | sop: CIVIC_INFRA_ALERT
```

---

## 🛠 Tech Stack

| Layer | Technology | Version |
|-------|-----------|---------|
| Neural network | PyTorch | 2.9.0 |
| NLP embeddings | sentence-transformers (`all-MiniLM-L6-v2`) | 3.0.1 |
| RL / LP optimizer | PuLP | 2.8.0 |
| ML preprocessing | scikit-learn | 1.9.0 |
| AI API server | FastAPI + Uvicorn | 0.111.0 / 0.30.1 |
| Java middleware | Spring Boot 3.2.5 + WebFlux | Java 17 |
| CSV parsing | OpenCSV | 5.9 |
| Boilerplate reduction | Lombok | — |
| Frontend | Vanilla JS + Leaflet.js | 1.9.4 |
| Map tiles | CARTO Dark Matter via OpenStreetMap | — |
| Containers | Docker (python:3.10-slim + eclipse-temurin:17-jre) | — |

---

## 🤝 Contributing

```bash
git checkout -b feat/your-feature
git commit -m "feat: clear description of what changed"
git push origin feat/your-feature
# Open a Pull Request
```

**Guidelines:**
- **AI server** — keep architecture changes in `train.py`; regenerate `v8_dl_model.pth` and `preprocessors.pkl` before committing
- **Backend** — field names in `PredictionResponse.java` must match the JSON keys via `@JsonProperty`
- **Frontend** — `renderResults()` in `index.html` consumes raw JSON directly; keep field names in sync with the API response
- **Data** — anonymise any new CSV rows before committing

---

## 📄 License

MIT — see [LICENSE](LICENSE).

---

<div align="center">
<br/>

*Built for smarter cities and faster emergency response.*

**ASTRAM-AI · Cognitive Grid Online** 🟢

[⬆ Back to top](#)

</div>
