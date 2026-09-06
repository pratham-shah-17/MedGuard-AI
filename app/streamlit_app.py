import streamlit as st
import pandas as pd
import sys
import os

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from preprocessing import normalize_drug_name, get_known_interactions_dict, load_and_preprocess_data
from features import FeatureEngineer
from models import train_models
from risk_engine import calculate_risk
from explain import explain_prediction

st.set_page_config(page_title="MedGuard-AI", layout="wide")

# Persistent Disclaimer
st.warning("**Educational & Open-Source Tool — Not for Clinical Use.**\n\nThe information and predictions provided by this tool are for educational and research purposes only. This system should never be used to make clinical decisions. Do not start, stop, increase, or decrease any medication based on this tool. Always consult a qualified healthcare provider.")

st.title("MedGuard-AI: Medication Interaction Risk Screening")

@st.cache_resource
def load_app_data():
    train_df, test_df = load_and_preprocess_data()
    if train_df.empty:
        return None, None, None, None, None
        
    known_interactions = get_known_interactions_dict()
    
    fe = FeatureEngineer(use_context=True)
    fe.fit(train_df)
    X_train = fe.transform(train_df)
    y_train = train_df['has_interaction']
    
    models = train_models(X_train, y_train)
    rf_model = models['RandomForest']
    
    return train_df, known_interactions, fe, rf_model, X_train

train_df, known_interactions, fe, rf_model, X_train = load_app_data()

if train_df is None:
    st.error("Data not found. Please run `python data/generate_dataset.py` first.")
    st.stop()

st.sidebar.header("Patient Context")
age = st.sidebar.slider("Age", 18, 100, 65)
crcl = st.sidebar.slider("Renal Function (CrCl mL/min)", 10, 150, 90)
ast = st.sidebar.slider("Liver Function (AST U/L)", 5, 200, 25)

st.sidebar.header("Medications")
drug1 = st.sidebar.text_input("Drug 1", "Warfarin")
drug2 = st.sidebar.text_input("Drug 2", "Aspirin")

if st.sidebar.button("Analyze Risk"):
    d1_norm = normalize_drug_name(drug1)
    d2_norm = normalize_drug_name(drug2)
    drugs = sorted([d1_norm, d2_norm])
    pair = (drugs[0], drugs[1])
    
    # 1. Rule-based check
    rule_flag = 1 if pair in known_interactions else 0
    rule_details = known_interactions.get(pair, None)
    
    # 2. ML Prediction
    input_df = pd.DataFrame([{
        'drug1': drugs[0],
        'drug2': drugs[1],
        'age': age,
        'renal_function_crcl': crcl,
        'liver_function_ast': ast
    }])
    
    X_input = fe.transform(input_df)
    ml_prob = rf_model.predict_proba(X_input)[0][1]
    
    # 3. Risk Engine
    risk_category, rationale = calculate_risk(rule_flag, ml_prob)
    
    st.subheader(f"Risk Assessment for {drug1.title()} + {drug2.title()}")
    
    if "High" in risk_category:
        st.error(f"**{risk_category}**\n\n{rationale}")
    elif "Moderate" in risk_category:
        st.warning(f"**{risk_category}**\n\n{rationale}")
    else:
        st.success(f"**{risk_category}**\n\n{rationale}")
        
    if rule_details:
        st.info(f"**Known Interaction Details:**\n- Type: {rule_details['interaction_type']}\n- Severity: {rule_details['severity']}/3\n- Source: {rule_details['evidence_source']}")
        
    # 4. Explainability
    st.subheader("ML Model Prediction Explainability (SHAP)")
    feature_impacts, _ = explain_prediction(rf_model, X_train, X_input, "RandomForest")
    
    st.write("Top factors influencing the ML probability:")
    impact_data = pd.DataFrame({
        "Feature": list(feature_impacts.keys())[:5],
        "Impact (SHAP value)": list(feature_impacts.values())[:5]
    })
    st.bar_chart(impact_data.set_index("Feature"))
