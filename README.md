# StressIntel PRO

Research-grade student stress analysis platform using XGBoost, SHAP, and LLMs.

## Features
- **Behavioral Assessment**: Multi-modal data fusion (Biomarkers + Journal + Micro-expressions).
- **XAI Dashboard**: Detailed feature influence visualization using SHAP.
- **Simulation Lab**: Forecast stress trajectories with interactive lifestyle sliders.
- **Peer Analytics**: Cohort benchmarking with spectrum markers.
- **Temporal Heatmap**: Weekly risk density visualization.
- **Clinical Reports**: AI-generated reports with markdown rendering.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Train model: `$env:PYTHONPATH = "."; python models/train/train_model.py`
3. Run app: `python app.py`

## Tech Stack
- **Backend**: Flask, Scikit-learn, XGBoost, SHAP.
- **Frontend**: Vanilla JS (ES6+), Chart.js, CSS (Glassmorphism).
- **Intelligence**: Simulated LLM for Clinical Reporting and Journal Analysis.
