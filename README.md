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

- **Hybrid Risk Engine:** Combines a deterministic rule-based baseline with a probabilistic Logistic Regression classifier running entirely in the browser.
- **Patient-Context Aware:** Incorporates patient context (Age, Creatinine Clearance, AST) into the risk calculation.
- **Explainable AI (XAI):** Integrated SHAP-equivalent visualizations compute local feature contributions dynamically in JavaScript.
- **Serverless Architecture:** 100% static frontend (HTML/CSS/JS) designed to run freely and securely on GitHub Pages with zero backend required.
- **Premium UI/UX:** Clean, responsive design built with Tailwind CSS, FontAwesome, and smooth CSS animations.

---

## 🚀 Getting Started

### 1. View Live Demo

The application is deployed live on GitHub Pages! You can interact with the risk engine directly:
👉 **[View Live Demo](https://pratham-shah-17.github.io/MedGuard-AI/docs/)** *(or the root URL depending on Pages config)*

### 2. Local Development (Data Pipeline)

If you wish to modify the underlying data or retrain the model, you can run the Python pipeline locally.
Ensure you have Python 3.8+ installed.

```bash
git clone https://github.com/pratham-shah-17/MedGuard-AI.git
cd MedGuard-AI
pip install -r requirements.txt

# Generate the synthetic verifiable dataset
python data/generate_dataset.py

# Train the ML model and export it to JavaScript (docs/model_data.js)
python export_model_to_js.py
```

### 3. Local Development (Frontend)

To modify the frontend, simply open `docs/index.html` in your web browser. No local server is required!

---

## 📂 Project Structure

```
MedGuard-AI/
├── docs/                       # STATIC GITHUB PAGES FRONTEND
│   ├── index.html              # Main UI
│   ├── styles.css              # Custom animations and styling
│   ├── app.js                  # Risk engine and XAI logic
│   └── model_data.js           # Auto-exported model weights and rules
├── data/
│   └── generate_dataset.py     # Script to generate verifiable DDI data
├── experiments/
│   └── run_experiments.py      # Evaluation and ablation studies
├── reports/
│   └── error_analysis.md       # Model error analysis outputs
├── src/                        # Python backend logic
├── export_model_to_js.py       # Bridges Python ML to JS frontend
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
