from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score, average_precision_score, confusion_matrix
import numpy as np

class RuleBasedBaseline:
    def __init__(self, interaction_dict):
        self.interaction_dict = interaction_dict
        
    def predict(self, df):
        preds = []
        for _, row in df.iterrows():
            drugs = sorted([row['drug1'], row['drug2']])
            pair = (drugs[0], drugs[1])
            if pair in self.interaction_dict:
                preds.append(1)
            else:
                preds.append(0)
        return np.array(preds)
        
    def predict_proba(self, df):
        preds = self.predict(df)
        # Dummy probas [prob_0, prob_1]
        return np.array([[1 - p, p] for p in preds])

def train_models(X_train, y_train):
    log_reg = LogisticRegression(max_iter=1000, random_state=42)
    log_reg.fit(X_train, y_train)
    
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    
    return {'LogisticRegression': log_reg, 'RandomForest': rf}

def evaluate_model(model, X_test, y_test, is_rule_based=False, df_test=None):
    if is_rule_based:
        y_pred = model.predict(df_test)
        y_proba = model.predict_proba(df_test)[:, 1]
    else:
        y_pred = model.predict(X_test)
        y_proba = model.predict_proba(X_test)[:, 1]
        
    metrics = {
        'Precision': precision_score(y_test, y_pred, zero_division=0),
        'Recall': recall_score(y_test, y_pred, zero_division=0),
        'F1-Score': f1_score(y_test, y_pred, zero_division=0)
    }
    
    # Handle single class in y_test for ROC AUC
    if len(np.unique(y_test)) > 1:
        metrics['ROC-AUC'] = roc_auc_score(y_test, y_proba)
        metrics['PR-AUC'] = average_precision_score(y_test, y_proba)
    else:
        metrics['ROC-AUC'] = float('nan')
        metrics['PR-AUC'] = float('nan')
        
    cm = confusion_matrix(y_test, y_pred)
    metrics['ConfusionMatrix'] = cm
    
    return metrics
