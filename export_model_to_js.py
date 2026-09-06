import pandas as pd
import json
import os
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

def normalize_drug_name(d):
    return d.lower().strip() if isinstance(d, str) else ""

def export():
    df = pd.read_csv("c:/Projects/MedGuardAI/data/interactions.csv")
    df['drug1'] = df['drug1'].apply(normalize_drug_name)
    df['drug2'] = df['drug2'].apply(normalize_drug_name)
    
    known_interactions = {}
    all_drugs = set()
    
    for i, row in df.iterrows():
        d1, d2 = sorted([row['drug1'], row['drug2']])
        df.at[i, 'drug1'] = d1
        df.at[i, 'drug2'] = d2
        all_drugs.update([d1, d2])
        if row['has_interaction'] == 1:
            known_interactions[f"{d1}::{d2}"] = {
                "severity": int(row['severity']),
                "interaction_type": row['interaction_type'],
                "evidence_source": row['evidence_source']
            }
            
    all_drugs = sorted(list(all_drugs))
    
    # Feature engineering for LogReg
    features = []
    for _, row in df.iterrows():
        feat = {}
        for d in all_drugs:
            feat[f"drug_{d}"] = 1.0 if (row['drug1'] == d or row['drug2'] == d) else 0.0
        feat["age"] = float(row["age"])
        feat["renal_function_crcl"] = float(row["renal_function_crcl"])
        feat["liver_function_ast"] = float(row["liver_function_ast"])
        features.append(feat)
        
    X = pd.DataFrame(features)
    y = df['has_interaction']
    
    # Train LogReg
    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)
    
    weights = {col: float(val) for col, val in zip(X.columns, model.coef_[0])}
    intercept = float(model.intercept_[0])
    
    js_content = f"""// Auto-generated Model Data
const KNOWN_INTERACTIONS = {json.dumps(known_interactions, indent=2)};
const ALL_DRUGS = {json.dumps(all_drugs, indent=2)};
const MODEL_WEIGHTS = {json.dumps(weights, indent=2)};
const MODEL_INTERCEPT = {intercept};
"""
    with open("c:/Projects/MedGuardAI/docs/model_data.js", "w") as f:
        f.write(js_content)
        
    print("Exported to docs/model_data.js")

if __name__ == "__main__":
    export()
