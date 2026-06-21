<div align="center">

<img src="https://img.shields.io/badge/ASTRAM--AI-v8.2%20TITAN-00ff88?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEyIDJMMiA3bDEwIDUgMTAtNS0xMC01ek0yIDE3bDEwIDUgMTAtNS0xMC01LTEwIDV6TTIgMTJsMTAgNSAxMC01LTEwLTUtMTAgNXoiIGZpbGw9IndoaXRlIi8+PC9zdmc+" alt="ASTRAM-AI"/>

# 🚦 ASTRAM-AI
### **Adaptive Smart Traffic Response & Analysis Management**
#### *Intelligent Traffic Incident Management Powered by Bayesian AI + LLM Reasoning*

---

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/React-18+-61DAFB?style=flat-square&logo=react&logoColor=black)](https://reactjs.org)
[![Leaflet](https://img.shields.io/badge/Leaflet-Maps-199900?style=flat-square&logo=leaflet&logoColor=white)](https://leafletjs.com)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Cognitive%20Grid-ONLINE-00ff88?style=flat-square&logo=statuspage&logoColor=white)]()

<br/>

> **ASTRAM-AI** is a full-stack, AI-powered traffic incident management platform that combines **Bayesian forecasting**, **LLM reasoning**, and **Reinforcement Learning (RL) agent deployment** to help traffic authorities predict, assess, and respond to road incidents in real time — with sub-second latency.

</div>

---

## 📸 System Preview

<table>
<tr>
<td width="60%">

**Live Dashboard — Bengaluru Traffic Control**

![ASTRAM Dashboard](https://via.placeholder.com/700x400/0d1117/00ff88?text=ASTRAM+v8.2+TITAN+Dashboard)

*Cognitive Grid ONLINE — Bayesian Forecast + LLM Reasoning Engine*

</td>
<td width="40%">

**Key Metrics at a Glance**

| Metric | Value |
|--------|-------|
| 🔴 Impact Score | **85.92 / 100** |
| ⏱ Est. Duration | **91 min** |
| 🚧 Road Closure | **REQUIRED** |
| 🚨 Priority | **CODE RED** |
| 👮 Officers Deployed | **10 Units** |
| 🔒 Model Uncertainty | **0.769 σ** |

</td>
</tr>
</table>

---

## 🏗 System Architecture

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    ASTRAM-AI INTELLIGENT TRAFFIC MANAGEMENT FLOW                │
│                                                                                 │
│  ┌─────────────────┐    ┌──────────────────┐    ┌─────────────────────────┐   │
│  │  FEEDBACK SYSTEM │    │   DATA SOURCES   │    │    PREDICTION ENGINE    │   │
│  │                  │    │                  │    │                         │   │
│  │ Event Outcome ──►│    │ Social Media ────┤    │  ┌──────────────────┐  │   │
│  │ Collection       │    │ Signals          │    │  │Severity Prediction│  │   │
│  │        │         │    │                  │    │  └──────────────────┘  │   │
│  │        ▼         │    │ Historical ──────┤    │                         │   │
│  │ Prediction vs    │    │ Traffic Events   │───►│  ┌──────────────────┐  │   │
│  │ Actual Analysis  │    │                  │    │  │Duration Prediction│  │   │
│  │        │         │    │ Live Traffic ────┤    │  └──────────────────┘  │   │
│  │        ▼         │    │ Events           │    │                         │   │
│  │ Model Retraining─┤    │                  │    │  ┌──────────────────┐  │   │
│  └──────────────────┘    │ Weather API ─────┘    │  │Impact Radius Pred │  │   │
│          ▲               │                        │  └──────────────────┘  │   │
│          │ Improved Model └──────────────────┘    └──────────┬──────────┘   │
│          │                        │                           │               │
│  ┌───────┴──────────────────────────────────────────────────▼────────────┐   │
│  │              EVENT PROCESSING & FEATURE ENGINEERING                    │   │
│  └───────────────────────────────────────────────────────────────────────┘   │
│                                            │                                   │
│  ┌─────────────────────┐    ┌─────────────▼──────────┐    ┌────────────────┐ │
│  │ OPTIMIZATION ENGINE │    │                        │    │DECISION SUPPORT│ │
│  │                     │    │  Resource Allocation   │    │    SYSTEM      │ │
│  │  Route Diversion ───┤    │  Engine                │───►│                │ │
│  │  Engine             │    │                        │    │ Traffic Dash   │ │
│  │                     │    │  Priority Ranking      │    │ Smart Alerts   │ │
│  └─────────────────────┘    │  Engine                │    │ Officer Deploy │ │
│                              └────────────────────────┘    └────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────────┘
```

The system flows through **5 major subsystems**:

| # | Subsystem | Role |
|---|-----------|------|
| 1 | **Data Sources** | Ingests social media, historical events, live traffic feeds, and weather APIs |
| 2 | **Prediction Engine** | Runs Bayesian ML models for severity, duration, and impact radius prediction |
| 3 | **Optimization Engine** | Allocates resources and calculates route diversions |
| 4 | **Decision Support System** | Delivers actionable outputs: dashboard, alerts, officer plans |
| 5 | **Feedback System** | Closes the loop — compares predictions vs actuals and retrains the model |

---

## 📁 Repository Structure

```
gridsss/
│
├── 📂 frontend/                    # React + Leaflet dashboard
│   ├── src/
│   │   ├── components/
│   │   │   ├── MapView.jsx         # Leaflet map with incident pin
│   │   │   ├── BayesianForecast.jsx
│   │   │   ├── LLMReasoningPanel.jsx
│   │   │   ├── RLDeployment.jsx
│   │   │   └── ControlPanel.jsx    # Input form
│   │   ├── App.jsx
│   │   └── index.js
│   ├── public/
│   └── package.json
│
├── 📂 backend/                     # FastAPI server
│   ├── main.py                     # API entry point
│   ├── routers/
│   │   └── analysis.py             # /analyze endpoint
│   ├── services/
│   │   ├── bayesian_engine.py      # Bayesian impact + duration model
│   │   ├── llm_reasoning.py        # LLM SOP classifier
│   │   └── rl_deployment.py        # RL resource dispatch
│   ├── models/
│   │   └── schemas.py              # Pydantic I/O models
│   └── requirements.txt
│
└── 📂 ML model/                    # Training notebooks & saved artifacts
    ├── training/
    │   ├── bayesian_model.ipynb
    │   ├── severity_classifier.ipynb
    │   └── rl_policy.ipynb
    ├── saved_models/
    │   ├── bayesian_regressor.pkl
    │   └── severity_model.pkl
    └── data/
        ├── historical_incidents.csv
        └── feature_engineering.py
```

---

## 🧠 AI Architecture — Three-Layer Intelligence

ASTRAM-AI uses a **three-layer AI stack** for robust, explainable predictions:

```
┌─────────────────────────────────────────────────────────┐
│                  LAYER 1: BAYESIAN FORECAST              │
│  • Predicts impact score (0–100), duration (minutes)    │
│  • Outputs confidence intervals & epistemic uncertainty  │
│  • Uses log-normal regression over historical incidents  │
└────────────────────────────┬────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────┐
│               LAYER 2: LLM REASONING ENGINE              │
│  • Classifies Standard Operating Procedure (SOP)        │
│  • Detects HAZMAT risk from natural language description │
│  • Infers priority level and sentiment from input text   │
│  • Forces road closure when critical thresholds met      │
└────────────────────────────┬────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────┐
│             LAYER 3: RL AGENTIC DEPLOYMENT               │
│  • Dispatches officers to optimal BLR node              │
│  • Allocates barricades and special units               │
│  • Optimizes resource allocation via trained RL policy   │
└─────────────────────────────────────────────────────────┘
```

---

## 🔌 API Reference

### `POST /analyze` — Run Cognitive Analysis

**Request Body:**

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

| Field | Type | Description |
|-------|------|-------------|
| `event_type` | `string` | Type of incident (`accident`, `flood`, `hazmat`, etc.) |
| `event_cause` | `string` | Specific cause (`collision`, `breakdown`, `protest`, etc.) |
| `latitude` | `float` | GPS latitude coordinate |
| `longitude` | `float` | GPS longitude coordinate |
| `veh_type` | `string` | Vehicle involved (`car`, `truck`, `bus`, `bike`) |
| `description` | `string` | Free-text natural language incident description |

---

**Response Body:**

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

| Response Field | Meaning |
|----------------|---------|
| `mean_impact_score` | Predicted severity out of 100 |
| `mean_duration_mins` | Expected clearance time in minutes |
| `confidence_interval` | 95% Bayesian confidence bound (log-space) |
| `epistemic_uncertainty` | Model uncertainty score (lower = more confident) |
| `ai_predicted_road_closure` | Whether ML model recommends closure |
| `sop_flag` | SOP code triggered (`CODE_RED_MEDICAL`, `STANDARD`, etc.) |
| `hazmat_risk` | Boolean HAZMAT detection from description |
| `sentiment_vector` | Linguistic severity from description (0–5 scale) |
| `inferred_priority` | Aggregated priority: `Low`, `Medium`, `High`, `Critical` |
| `force_road_closure` | LLM override for road closure |
| `dispatch_node` | Nearest resource depot + unit count |
| `officers_assigned` | Number of officers to deploy |
| `barricades` | Barricade units recommended |
| `special_units` | Special response unit type |

---

## ⚡ Quick Start

### Prerequisites

- Python 3.10+
- Node.js 18+
- pip & npm

### 1. Clone the Repository

```bash
git clone https://github.com/KTG084/gridsss.git
cd gridsss
```

### 2. Backend Setup

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

The API will be live at `http://127.0.0.1:8000`

### 3. Frontend Setup

```bash
cd frontend
npm install
npm start
```

The dashboard will open at `http://127.0.0.1:3000`

### 4. ML Model (Optional — for retraining)

```bash
cd "ML model"
pip install jupyter scikit-learn pandas numpy
jupyter notebook
```

Open `training/bayesian_model.ipynb` and run all cells.

---

## 🗺 Dashboard Walkthrough

The ASTRAM-AI frontend (built with **React + Leaflet**) provides:

### Control Panel (Left Sidebar)
- **Event Type** dropdown — accident, flood, hazmat, protest
- **Event Cause** dropdown — collision, breakdown, fire, etc.
- **Vehicle Type** selector
- **Lat/Lng** input (or click-to-place on map)
- **Incident Description** free-text box
- **Quick Presets** — Fatal Crash, Flood, Hazmat (one-click templates)
- **Run Cognitive Analysis** button

### Interactive Map (Center)
- Powered by **Leaflet + OpenStreetMap + CARTO** tiles
- Dark-mode rendering with incident pin placement
- Click anywhere on map to auto-populate coordinates
- Real-time incident location marker

### Results Panel (Bottom)

| Panel | Content |
|-------|---------|
| 🎯 **Bayesian Forecast** | Impact score, duration, confidence interval |
| 🚧 **Road Closure Decision** | AI recommendation with rationale |
| 📊 **Model Uncertainty** | σ value + confidence bar |
| 🤖 **LLM Reasoning Engine** | SOP flag, HAZMAT risk, priority |
| 🚔 **RL Deployment Plan** | Officers, barricades, dispatch node |

---

## 🔬 ML Model Details

### Bayesian Regression (Impact + Duration)

The core prediction engine uses **Bayesian log-normal regression** trained on historical Bengaluru traffic incident data:

```
Features:
  - event_type (encoded)       → categorical
  - event_cause (encoded)      → categorical
  - vehicle_type (encoded)     → categorical
  - latitude / longitude       → geospatial features
  - time_of_day (engineered)   → cyclical sin/cos
  - road_category              → OSM-derived

Targets:
  - log(impact_score)          → Gaussian posterior
  - log(duration_minutes)      → Gaussian posterior

Output:
  - Posterior mean + 95% CI via sampling
  - Epistemic uncertainty = variance across samples
```

### LLM Reasoning Engine

Uses an LLM to extract:
- **SOP classification** from incident description
- **HAZMAT detection** (keywords + semantic context)
- **Sentiment vector** (linguistic urgency score 0–5)
- **Priority inference** combining ML score + LLM severity

### RL Agentic Deployment

A trained **Reinforcement Learning policy** maps:
```
(impact_score, priority, location) → (dispatch_node, officers, barricades)
```

Trained with reward shaping based on:
- Time-to-clear reduction
- Resource efficiency (minimize over-deployment)
- Historical outcome data from the Feedback System

---

## 🔄 Feedback Loop & Model Retraining

ASTRAM-AI is **self-improving**. The Feedback System:

1. **Collects event outcomes** — actual duration, final officer count, closure status
2. **Compares** predictions vs actuals (logged to database)
3. **Flags** high-error incidents for review
4. **Retrains** the Bayesian model periodically with new ground truth
5. **Pushes improved model** back to the Prediction Engine

```
Real Incident ──► Outcome Collection ──► Prediction vs Actual
                                                   │
                              Model Retraining ◄───┘
                                    │
                    Prediction Engine ◄── Improved Weights
```

---

## 🌐 SOP Codes Reference

| SOP Code | Trigger Condition | Response |
|----------|------------------|----------|
| `CODE_RED_MEDICAL` | High impact + vehicle collision | Emergency medical + road closure |
| `CODE_ORANGE_HAZMAT` | HAZMAT risk detected | Hazmat team + 500m exclusion zone |
| `CODE_YELLOW_STANDARD` | Medium impact, no special risk | Standard traffic officers |
| `CODE_GREEN_MONITOR` | Low impact, self-resolving | Remote monitoring only |
| `STANDARD` | Default response | SOP playbook dispatch |

---

## 🛠 Tech Stack

<table>
<tr>
<th>Layer</th>
<th>Technology</th>
<th>Purpose</th>
</tr>
<tr>
<td><b>Frontend</b></td>
<td>React 18, Leaflet.js, CARTO tiles</td>
<td>Interactive map dashboard</td>
</tr>
<tr>
<td><b>Backend</b></td>
<td>FastAPI (Python), Uvicorn</td>
<td>REST API + AI orchestration</td>
</tr>
<tr>
<td><b>ML Core</b></td>
<td>scikit-learn, NumPy, Pandas</td>
<td>Bayesian regression models</td>
</tr>
<tr>
<td><b>LLM Engine</b></td>
<td>OpenAI / Anthropic API</td>
<td>SOP reasoning & NLP classification</td>
</tr>
<tr>
<td><b>RL Agent</b></td>
<td>Custom RL policy (Gym)</td>
<td>Resource dispatch optimization</td>
</tr>
<tr>
<td><b>Maps</b></td>
<td>OpenStreetMap + Leaflet</td>
<td>Geospatial visualization</td>
</tr>
<tr>
<td><b>Geocoding</b></td>
<td>GPS coordinates (lat/lng)</td>
<td>Incident location pinning</td>
</tr>
</table>

---

## 📊 Sample Scenarios

### 🔴 Scenario A: Fatal Crash (CODE RED)

```json
Input:
  event_type: "accident"
  event_cause: "collision"
  veh_type: "truck"
  description: "marriage procession nearby, truck overturned, little road space left"

Output:
  impact_score: 85.92 / 100
  duration: 91 minutes
  road_closure: REQUIRED
  sop: CODE_RED_MEDICAL
  officers: 10
  barricades: 20
```

### 🟡 Scenario B: Minor Accident (LOW PRIORITY)

```json
Input:
  event_type: "accident"
  event_cause: "collision"
  veh_type: "car"
  description: "Minor accident"

Output:
  impact_score: 80.5 / 100
  duration: 24 minutes
  road_closure: NOT NEEDED
  priority: Low Priority
  officers: 3
```

### 🟠 Scenario C: Flood Event

```json
Input:
  event_type: "flood"
  event_cause: "waterlogging"
  description: "underpass submerged, 2 lanes blocked"

Output:
  impact_score: ~70+
  road_closure: LIKELY
  sop: STANDARD
  special_units: Water Rescue Team
```

---

## 📍 Coverage Area

Currently optimized for **Bengaluru (Bangalore), Karnataka, India**, with node dispatch grid covering:

- 📍 Central Bengaluru — BLR_Node_0001 to BLR_Node_0100
- 📍 North Bengaluru — BLR_Node_0101 to BLR_Node_0200
- 📍 South Bengaluru — BLR_Node_0201 to BLR_Node_0300
- 📍 East/West corridors — BLR_Node_0301+

> The system can be extended to any city by re-training the Bayesian model on local historical incident data and updating the node dispatch map.

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

```bash
# Fork the repo, then:
git checkout -b feature/your-feature-name
git commit -m "feat: add your feature"
git push origin feature/your-feature-name
# Open a Pull Request
```

### Development Guidelines

- Backend: Follow PEP8, add type hints, use Pydantic models for all I/O
- Frontend: Use functional React components with hooks
- ML: Document all feature engineering steps in notebooks
- Tests: Add pytest tests for all new API endpoints

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👥 Authors

Built with ❤️ for smarter cities and safer roads.

> *ASTRAM-AI — Cognitive Grid Online* 🟢

---

<div align="center">

**[⬆ Back to Top](#-astram-ai)**

</div>
