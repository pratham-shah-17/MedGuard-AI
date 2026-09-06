import pandas as pd

class FeatureEngineer:
    def __init__(self, use_context=True):
        self.use_context = use_context
        self.all_drugs = set()
        
    def fit(self, df):
        # Collect all unique drugs for one-hot encoding
        self.all_drugs.update(df['drug1'].unique())
        self.all_drugs.update(df['drug2'].unique())
        return self
        
    def transform(self, df):
        features = []
        for _, row in df.iterrows():
            feat_dict = {}
            # Drug presence features
            for drug in self.all_drugs:
                feat_dict[f'drug_{drug}'] = 1 if (row['drug1'] == drug or row['drug2'] == drug) else 0
                
            # Context features
            if self.use_context:
                feat_dict['age'] = row['age']
                feat_dict['renal_function_crcl'] = row['renal_function_crcl']
                feat_dict['liver_function_ast'] = row['liver_function_ast']
                
            features.append(feat_dict)
            
        return pd.DataFrame(features, index=df.index)
        
    def get_feature_names(self):
        feats = [f'drug_{d}' for d in self.all_drugs]
        if self.use_context:
            feats.extend(['age', 'renal_function_crcl', 'liver_function_ast'])
        return feats
