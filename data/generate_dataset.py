import pandas as pd
import os
import random

# Ensure reproducible random synthetic data
random.seed(42)

# Manually compiled list of real, known drug-drug interactions
# Format: (drug1, drug2, interaction_type, severity (1-3), evidence)
KNOWN_INTERACTIONS = [
    ("warfarin", "aspirin", "increased_bleeding_risk", 3, "Standard clinical knowledge"),
    ("warfarin", "ibuprofen", "increased_bleeding_risk", 3, "Standard clinical knowledge"),
    ("simvastatin", "clarithromycin", "myopathy_rhabdomyolysis_risk", 3, "FDA label warning"),
    ("simvastatin", "amiodarone", "myopathy_risk", 2, "Standard clinical knowledge"),
    ("sildenafil", "nitroglycerin", "severe_hypotension", 3, "Absolute contraindication"),
    ("lisinopril", "spironolactone", "hyperkalemia", 2, "Standard clinical knowledge"),
    ("citalopram", "fluconazole", "qt_prolongation", 2, "Standard clinical knowledge"),
    ("methotrexate", "trimethoprim", "bone_marrow_suppression", 3, "Standard clinical knowledge"),
    ("clopidogrel", "omeprazole", "reduced_antiplatelet_effect", 2, "FDA label warning"),
    ("atorvastatin", "grapefruit_juice", "increased_statin_toxicity", 2, "Standard clinical knowledge"),
    ("digoxin", "verapamil", "digoxin_toxicity", 2, "Standard clinical knowledge"),
    ("levothyroxine", "calcium_carbonate", "decreased_absorption", 1, "Standard clinical knowledge"),
    ("metronidazole", "alcohol", "disulfiram_like_reaction", 2, "Standard clinical knowledge"),
    ("tramadol", "fluoxetine", "serotonin_syndrome", 3, "Standard clinical knowledge"),
    ("azithromycin", "amiodarone", "qt_prolongation", 3, "Standard clinical knowledge"),
    ("lithium", "hydrochlorothiazide", "lithium_toxicity", 3, "Standard clinical knowledge"),
    ("phenytoin", "valproic_acid", "altered_phenytoin_levels", 2, "Standard clinical knowledge"),
    ("theophylline", "ciprofloxacin", "theophylline_toxicity", 3, "Standard clinical knowledge"),
    ("allopurinol", "azathioprine", "bone_marrow_suppression", 3, "Standard clinical knowledge"),
    ("spironolactone", "potassium_chloride", "hyperkalemia", 3, "Standard clinical knowledge")
]

# Safe combinations (no major known interactions)
# Format: (drug1, drug2, interaction_type, severity (0), evidence)
SAFE_COMBINATIONS = [
    ("acetaminophen", "amoxicillin", "none", 0, "No known interaction"),
    ("ibuprofen", "loratadine", "none", 0, "No known interaction"),
    ("lisinopril", "atorvastatin", "none", 0, "No known interaction"),
    ("metformin", "levothyroxine", "none", 0, "No known interaction"),
    ("omeprazole", "cetirizine", "none", 0, "No known interaction"),
    ("albuterol", "fluticasone", "none", 0, "No known interaction"),
    ("pantoprazole", "acetaminophen", "none", 0, "No known interaction"),
    ("gabapentin", "vitamin_d", "none", 0, "No known interaction"),
    ("sertraline", "levothyroxine", "none", 0, "No known interaction"),
    ("amlodipine", "metformin", "none", 0, "No known interaction"),
    ("losartan", "atorvastatin", "none", 0, "No known interaction"),
    ("meloxicam", "pantoprazole", "none", 0, "No known interaction"),
    ("trazodone", "omeprazole", "none", 0, "No known interaction"),
    ("duloxetine", "levothyroxine", "none", 0, "No known interaction"),
    ("rosuvastatin", "amlodipine", "none", 0, "No known interaction"),
    ("escitalopram", "cetirizine", "none", 0, "No known interaction"),
    ("venlafaxine", "pantoprazole", "none", 0, "No known interaction"),
    ("bupropion", "atorvastatin", "none", 0, "No known interaction"),
    ("zolpidem", "lisinopril", "none", 0, "No known interaction"),
    ("clonazepam", "omeprazole", "none", 0, "No known interaction")
]

def generate_synthetic_context(severity, interaction_type):
    """
    Generate synthetic patient context. 
    In a real ML dataset, we want some correlation so the model learns.
    For bleeding risks, maybe older age is more dangerous.
    For renal cleared drugs (like lithium, digoxin), low CrCl is bad.
    """
    age = random.randint(18, 90)
    crcl = random.randint(30, 120)
    ast = random.randint(10, 100)
    
    # Introduce weak correlations for the ML model to find
    # E.g., if it's a severe interaction and renal related, maybe CrCl is lower in this sample.
    if severity >= 2 and interaction_type in ["lithium_toxicity", "digoxin_toxicity", "hyperkalemia"]:
        crcl = random.randint(20, 60) # lower renal function
    if severity >= 2 and interaction_type in ["increased_bleeding_risk"]:
        age = random.randint(65, 95) # older patients

    return age, crcl, ast

def main():
    data = []
    
    # We will oversample to get around 200 rows for training
    # Let's generate 100 positive and 100 negative samples by repeating with different patient context
    
    for _ in range(5):
        for drug1, drug2, int_type, sev, ev in KNOWN_INTERACTIONS:
            age, crcl, ast = generate_synthetic_context(sev, int_type)
            data.append({
                "drug1": drug1,
                "drug2": drug2,
                "age": age,
                "renal_function_crcl": crcl,
                "liver_function_ast": ast,
                "interaction_type": int_type,
                "severity": sev,
                "evidence_source": ev,
                "has_interaction": 1
            })
            
        for drug1, drug2, int_type, sev, ev in SAFE_COMBINATIONS:
            age, crcl, ast = generate_synthetic_context(sev, int_type)
            data.append({
                "drug1": drug1,
                "drug2": drug2,
                "age": age,
                "renal_function_crcl": crcl,
                "liver_function_ast": ast,
                "interaction_type": int_type,
                "severity": sev,
                "evidence_source": ev,
                "has_interaction": 0
            })
            
    df = pd.DataFrame(data)
    
    # Shuffle
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    
    os.makedirs(os.path.dirname("c:/Projects/MedGuardAI/data/interactions.csv"), exist_ok=True)
    df.to_csv("c:/Projects/MedGuardAI/data/interactions.csv", index=False)
    print(f"Generated data/interactions.csv with {len(df)} records.")

if __name__ == "__main__":
    main()
