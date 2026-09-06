# Error Analysis

Based on the outputs of `run_experiments.py`, here is a qualitative analysis of the model's errors.

## Experiment Results Summary
- **Rule-Based Baseline:** 100% Precision and Recall (F1: 1.0000). This perfectly identifies known interactions because it acts as a direct lookup table.
- **Random Forest (Medication Only):** 100% F1-score (ROC-AUC: 1.0000). On this small, manually crafted dataset (200 rows), the exact drug combinations perfectly predict the outcome.
- **Random Forest (Medication + Patient Context):** 85.71% F1-score (ROC-AUC: 0.9450).

## Qualitative Analysis of Errors
- **False Positives & False Negatives in the Med+Context Model:** 
  The inclusion of synthetic patient context (age, renal function, liver function) slightly degraded the Random Forest model's performance compared to the medication-only baseline. 
  Because our synthetic dataset strongly relies on the exact drug pairs to determine the interaction status, the randomly generated continuous variables (patient context) acted as noise, causing the decision trees to occasionally split on irrelevant context features rather than relying solely on the definitive drug features.

In a larger, real-world dataset (e.g., MIMIC-IV), we would expect patient context to *improve* performance by providing necessary nuance (e.g., a drug pair is only dangerous if the patient's renal function is poor). However, on this highly simplified prototype dataset, the "clean" drug features alone are sufficient to perfectly separate the classes, making the context variables detrimental.
