import shap
import pandas as pd
import matplotlib.pyplot as plt
import os

def explain_prediction(model, X_train, instance, model_name="RandomForest"):
    """
    Generate SHAP explanation for a single instance.
    For RandomForest, uses TreeExplainer.
    For LogisticRegression, uses LinearExplainer.
    """
    # Ensure instance is 2D
    if isinstance(instance, pd.Series):
        instance = pd.DataFrame([instance])
        
    if model_name == "RandomForest":
        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(instance)
        # Random Forest explainer returns a list of arrays for classification (one for each class). We want class 1.
        if isinstance(shap_values, list):
            sv = shap_values[1][0]
        else:
            sv = shap_values[0] # Some versions behave differently
        expected_value = explainer.expected_value[1] if isinstance(explainer.expected_value, list) or isinstance(explainer.expected_value, np.ndarray) else explainer.expected_value
    else: # LogisticRegression
        explainer = shap.LinearExplainer(model, X_train)
        shap_values = explainer.shap_values(instance)
        sv = shap_values[0]
        expected_value = explainer.expected_value
        
    # Return as dict for easy rendering
    feature_impacts = {col: val for col, val in zip(instance.columns, sv)}
    # Sort by absolute impact
    feature_impacts = dict(sorted(feature_impacts.items(), key=lambda item: abs(item[1]), reverse=True))
    
    return feature_impacts, expected_value

def generate_shap_summary_plot(model, X_train, X_test, output_path="c:/Projects/MedGuardAI/reports/shap_summary.png"):
    """Generates and saves a SHAP summary plot for the test set."""
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_test)
    
    if isinstance(shap_values, list):
        sv_class1 = shap_values[1]
    else:
        sv_class1 = shap_values
        
    plt.figure()
    shap.summary_plot(sv_class1, X_test, show=False)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
