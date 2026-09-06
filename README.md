<div align="center">
  <h1>🛡️ MedGuard-AI</h1>
  <p><strong>An Explainable AI Framework for Medication Interaction Risk Screening</strong></p>
</div>

> **🚨 Important Disclaimer: Not for Clinical Use**  
> MedGuard-AI is an open-source educational and research tool. It must **never** be used to make clinical decisions or alter patient care. Always consult a qualified healthcare provider.

---

## 📖 Overview

MedGuard-AI is a lightweight, end-to-end machine learning framework designed to predict and explain Drug-Drug Interactions (DDIs). By combining known clinical guidelines with machine learning (Random Forest) and patient context (e.g., age, renal function, liver function), MedGuard-AI demonstrates how AI can assist in flagging potentially dangerous medication combinations.

The project features a **hybrid risk engine** that falls back on rule-based lookups for known severe interactions, while utilizing a predictive model to evaluate novel or less-documented pairs based on similarity and contextual risk factors. It uses **SHAP (SHapley Additive exPlanations)** to ensure every prediction is transparent and interpretable.

---

## ✨ Key Features

- **Hybrid Risk Engine:** Combines a deterministic rule-based baseline with a probabilistic Random Forest classifier.
- **Patient-Context Aware:** Incorporates synthetic patient context (Age, Creatinine Clearance, AST) into the risk calculation.
- **Explainable AI (XAI):** Integrated SHAP visualizations to break down exactly which features influenced the model's confidence.
- **Interactive UI:** Built-in Streamlit dashboard for real-time interaction screening.
- **Verifiable Dataset:** Includes a data generation pipeline grounded in established clinical interactions (e.g., Warfarin + Aspirin, Simvastatin + Clarithromycin).

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.8+ installed on your system.

### 1. Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/MedGuard-AI.git
cd MedGuard-AI
pip install -r requirements.txt
```

### 2. Generate the Dataset

Before running the application, generate the synthetic training data:

```bash
python data/generate_dataset.py
```

### 3. Run the Dashboard

Launch the interactive Streamlit application:

```bash
streamlit run app/streamlit_app.py
```

Navigate to `http://localhost:8501` in your browser to use the tool.

### 4. Run Experiments & Tests

Evaluate the model's performance and run the automated test suite:

```bash
# Run the evaluation experiments
python experiments/run_experiments.py

# Run the test suite
python -m pytest tests/test_core.py
```

---

## 📂 Project Structure

```
MedGuard-AI/
├── app/
│   └── streamlit_app.py        # Streamlit interactive dashboard
├── data/
│   └── generate_dataset.py     # Script to generate verifiable DDI data
├── experiments/
│   └── run_experiments.py      # Evaluation and ablation studies
├── reports/
│   └── error_analysis.md       # Model error analysis and SHAP outputs
├── src/
│   ├── preprocessing.py        # Data loading and normalization
│   ├── features.py             # Feature engineering
│   ├── models.py               # ML models and rule-based baselines
│   ├── explain.py              # SHAP explainability integration
│   └── risk_engine.py          # Hybrid risk calculation logic
├── tests/
│   └── test_core.py            # Unit tests
├── DATA_SOURCES.md             # Dataset documentation
├── DISCLAIMER.md               # Medical disclaimer
└── requirements.txt            # Python dependencies
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
