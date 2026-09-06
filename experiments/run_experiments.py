import sys
import os
import pandas as pd
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from preprocessing import load_and_preprocess_data, get_known_interactions_dict
from features import FeatureEngineer
from models import train_models, evaluate_model, RuleBasedBaseline
from explain import generate_shap_summary_plot

def run_experiment_1(train_df, test_df):
    print("\n--- Experiment 1: Dataset Stats ---")
    full_df = pd.concat([train_df, test_df])
    print(f"Total pairs: {len(full_df)}")
    print(f"Positive pairs (known interaction): {full_df['has_interaction'].sum()}")
    print(f"Negative pairs (no known interaction): {len(full_df) - full_df['has_interaction'].sum()}")
    
    all_drugs = set(full_df['drug1']).union(set(full_df['drug2']))
    print(f"Unique drugs: {len(all_drugs)}")

def run_experiment_2(train_df, test_df, known_interactions, X_train, X_test, y_train, y_test, models):
    print("\n--- Experiment 2: Rule-Based vs ML ---")
    
    rule_model = RuleBasedBaseline(known_interactions)
    rule_metrics = evaluate_model(rule_model, None, y_test, is_rule_based=True, df_test=test_df)
    print("Rule-Based Metrics:")
    for k, v in rule_metrics.items():
        if k != 'ConfusionMatrix':
            print(f"  {k}: {v:.4f}" if isinstance(v, float) else f"  {k}: {v}")
            
    rf_metrics = evaluate_model(models['RandomForest'], X_test, y_test)
    print("\nRandom Forest (Med+Context) Metrics:")
    for k, v in rf_metrics.items():
        if k != 'ConfusionMatrix':
            print(f"  {k}: {v:.4f}" if isinstance(v, float) else f"  {k}: {v}")

def run_experiment_3(train_df, test_df, y_train, y_test, X_train_full, X_test_full, models_full):
    print("\n--- Experiment 3: Context Ablation ---")
    
    # Train Med-Only Model
    fe_med = FeatureEngineer(use_context=False)
    fe_med.fit(train_df)
    X_train_med = fe_med.transform(train_df)
    X_test_med = fe_med.transform(test_df)
    
    models_med = train_models(X_train_med, y_train)
    rf_med_metrics = evaluate_model(models_med['RandomForest'], X_test_med, y_test)
    
    rf_full_metrics = evaluate_model(models_full['RandomForest'], X_test_full, y_test)
    
    print("Medication-Only (RF) Metrics:")
    print(f"  F1: {rf_med_metrics['F1-Score']:.4f}, ROC-AUC: {rf_med_metrics['ROC-AUC']:.4f}")
    
    print("Medication+Context (RF) Metrics:")
    print(f"  F1: {rf_full_metrics['F1-Score']:.4f}, ROC-AUC: {rf_full_metrics['ROC-AUC']:.4f}")
    
def run_experiment_4(models, X_train, X_test):
    print("\n--- Experiment 4: Explainability (SHAP) ---")
    generate_shap_summary_plot(models['RandomForest'], X_train, X_test)
    print("Generated SHAP summary plot at reports/shap_summary.png")

if __name__ == "__main__":
    train_df, test_df = load_and_preprocess_data()
    known_interactions = get_known_interactions_dict()
    
    fe = FeatureEngineer(use_context=True)
    fe.fit(train_df)
    X_train = fe.transform(train_df)
    X_test = fe.transform(test_df)
    y_train = train_df['has_interaction']
    y_test = test_df['has_interaction']
    
    models = train_models(X_train, y_train)
    
    run_experiment_1(train_df, test_df)
    run_experiment_2(train_df, test_df, known_interactions, X_train, X_test, y_train, y_test, models)
    run_experiment_3(train_df, test_df, y_train, y_test, X_train, X_test, models)
    run_experiment_4(models, X_train, X_test)
