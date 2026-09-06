import pandas as pd
from sklearn.model_selection import train_test_split

def normalize_drug_name(drug_name):
    """Simple normalization: lowercase and strip whitespace."""
    if not isinstance(drug_name, str):
        return ""
    return drug_name.lower().strip()

def load_and_preprocess_data(filepath="c:/Projects/MedGuardAI/data/interactions.csv"):
    """Loads dataset, normalizes drug names, and splits into train/test."""
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        # Return empty dataframe if not found, to avoid crash in Streamlit before generating
        return pd.DataFrame(), pd.DataFrame()
        
    df['drug1'] = df['drug1'].apply(normalize_drug_name)
    df['drug2'] = df['drug2'].apply(normalize_drug_name)
    
    # Sort drug pairs alphabetically so (A, B) is same as (B, A)
    for i, row in df.iterrows():
        drugs = sorted([row['drug1'], row['drug2']])
        df.at[i, 'drug1'] = drugs[0]
        df.at[i, 'drug2'] = drugs[1]
        
    # Drop duplicates if any were introduced by sorting
    df = df.drop_duplicates()
    
    # Split features and target
    # For splitting, we'll return the full df and let the caller decide features vs target
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42, stratify=df['has_interaction'])
    
    return train_df, test_df

def get_known_interactions_dict(filepath="c:/Projects/MedGuardAI/data/interactions.csv"):
    """Returns a dictionary of known interactions for the rule-based system."""
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        return {}
        
    df['drug1'] = df['drug1'].apply(normalize_drug_name)
    df['drug2'] = df['drug2'].apply(normalize_drug_name)
    
    interaction_dict = {}
    for _, row in df.iterrows():
        drugs = sorted([row['drug1'], row['drug2']])
        pair = (drugs[0], drugs[1])
        if row['has_interaction'] == 1:
            interaction_dict[pair] = {
                'severity': row['severity'],
                'interaction_type': row['interaction_type'],
                'evidence_source': row['evidence_source']
            }
    return interaction_dict
