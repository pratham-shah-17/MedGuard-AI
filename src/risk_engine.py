def calculate_risk(rule_flag, ml_probability):
    """
    Combines rule-based flag and ML probability into a final risk category.
    
    Formula:
    - If Rule Based = 1: High Risk (Known Evidence)
    - If Rule Based = 0 and ML Prob >= 0.7: High Risk (Model Predicted)
    - If Rule Based = 0 and ML Prob >= 0.4 and < 0.7: Moderate Risk (Model Predicted)
    - If Rule Based = 0 and ML Prob < 0.4: Low Risk (Insufficient Evidence)
    """
    if rule_flag == 1:
        return "High Risk (Known Evidence)", "Found in known interaction database."
    elif ml_probability >= 0.7:
        return "High Risk (Model Predicted)", "Based on similarity and patient context, ML predicts high risk."
    elif ml_probability >= 0.4:
        return "Moderate Risk (Model Predicted)", "ML model predicts potential moderate risk based on context."
    else:
        return "Low Risk (Insufficient Evidence)", "No known interaction and ML predicts low probability."
