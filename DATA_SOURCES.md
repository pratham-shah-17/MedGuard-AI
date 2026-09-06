# Data Sources

This document describes the provenance of the data used in the MedGuard-AI project.

## Dataset: interactions.csv
To adhere to the "no fabrication" requirements, the dataset (`data/interactions.csv`) is manually compiled based on widely known and documented drug-drug interactions (DDIs). This is a simplified subset (~200 pairs) to serve as a verifiable standard for the project without the complexity of parsing the full FDA or DrugBank databases.

- **Positive Samples (Known Interactions)**: Derived from well-established clinical knowledge (e.g., Warfarin + Aspirin, Simvastatin + Clarithromycin, Sildenafil + Nitroglycerin).
- **Negative Samples (Safe/No Known Interaction)**: Derived from common, generally safe combinations (e.g., Acetaminophen + Amoxicillin), ensuring no known severe interactions exist for these pairs based on standard clinical knowledge.

The dataset includes the following columns:
- `drug1`: Name of the first medication.
- `drug2`: Name of the second medication.
- `interaction_type`: Category of the interaction (e.g., "bleeding_risk", "qt_prolongation", "myopathy", "none").
- `severity`: Rule-based severity score (0 = none, 1 = minor, 2 = moderate, 3 = severe).
- `evidence_source`: A brief reference (e.g., "FDA label common knowledge", "Standard clinical guidelines").

## Synthetic Patient Context
To evaluate the ML model's ability to incorporate patient context (RQ2/H2) without violating PII constraints, synthetic patient profiles are dynamically generated or randomly assigned during model training and evaluation. These include:
- `age`: Synthetically generated integer (18-90).
- `renal_function_crcl`: Synthetically generated (30-120 mL/min).
- `liver_function_ast`: Synthetically generated (10-100 U/L).

These features are entirely synthetic and do not reflect any real individuals.
