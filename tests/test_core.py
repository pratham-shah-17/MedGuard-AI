import pytest
import pandas as pd
from src.preprocessing import normalize_drug_name
from src.risk_engine import calculate_risk

def test_normalize_drug_name():
    assert normalize_drug_name(" Aspirin ") == "aspirin"
    assert normalize_drug_name("WARFARIN") == "warfarin"
    assert normalize_drug_name(None) == ""
    assert normalize_drug_name(123) == ""

def test_calculate_risk():
    # Rule Based High Risk
    risk, rationale = calculate_risk(1, 0.1)
    assert "High Risk" in risk
    assert "Known Evidence" in risk
    
    # ML Predicted High Risk
    risk, rationale = calculate_risk(0, 0.8)
    assert "High Risk" in risk
    assert "Model Predicted" in risk
    
    # ML Predicted Moderate Risk
    risk, rationale = calculate_risk(0, 0.5)
    assert "Moderate Risk" in risk
    
    # Low Risk
    risk, rationale = calculate_risk(0, 0.2)
    assert "Low Risk" in risk
