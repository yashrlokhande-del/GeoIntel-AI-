# GeoIntel AI

A transparent, extensible geopolitical intelligence and risk-analysis prototype.

## V1 capabilities

- Country-pair selection
- Transparent 0–100 geopolitical risk scoring
- Security, political, diplomatic, economic, social and strategic dimensions
- Relationship modifiers
- Scenario analysis
- Early-warning indicators
- Methodology/guardrail display
- PostgreSQL schema for future real-world data

## Important

V1 uses **demonstration data**. The scores are not real-time intelligence assessments and must not be interpreted as probabilities of war or other specific events.

The next versions should replace the demo data with validated sources and add evidence/citation tracking.

## Run locally

### 1. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the app

```bash
streamlit run app.py
```

Streamlit's official documentation recommends a virtual environment and running apps with `streamlit run app.py`.

## Project structure

```text
GeoIntel-AI/
├── app.py
├── core/
│   ├── scoring.py
│   └── scenarios.py
├── data/
│   └── sample_data.py
├── database/
│   └── schema.sql
├── requirements.txt
└── README.md
```

## Roadmap

1. Real World Bank indicators
2. UCDP conflict-event ingestion
3. GDELT news/event ingestion
4. UN and official-source ingestion
5. Evidence/source reliability layer
6. RAG knowledge base
7. LLM analyst
8. Historical backtesting
9. Calibrated forecasting model
10. Interactive geopolitical map
