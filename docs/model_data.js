// Auto-generated Model Data
const KNOWN_INTERACTIONS = {
  "hydrochlorothiazide::lithium": {
    "severity": 3,
    "interaction_type": "lithium_toxicity",
    "evidence_source": "Standard clinical knowledge"
  },
  "clopidogrel::omeprazole": {
    "severity": 2,
    "interaction_type": "reduced_antiplatelet_effect",
    "evidence_source": "FDA label warning"
  },
  "digoxin::verapamil": {
    "severity": 2,
    "interaction_type": "digoxin_toxicity",
    "evidence_source": "Standard clinical knowledge"
  },
  "amiodarone::azithromycin": {
    "severity": 3,
    "interaction_type": "qt_prolongation",
    "evidence_source": "Standard clinical knowledge"
  },
  "lisinopril::spironolactone": {
    "severity": 2,
    "interaction_type": "hyperkalemia",
    "evidence_source": "Standard clinical knowledge"
  },
  "ciprofloxacin::theophylline": {
    "severity": 3,
    "interaction_type": "theophylline_toxicity",
    "evidence_source": "Standard clinical knowledge"
  },
  "phenytoin::valproic_acid": {
    "severity": 2,
    "interaction_type": "altered_phenytoin_levels",
    "evidence_source": "Standard clinical knowledge"
  },
  "clarithromycin::simvastatin": {
    "severity": 3,
    "interaction_type": "myopathy_rhabdomyolysis_risk",
    "evidence_source": "FDA label warning"
  },
  "nitroglycerin::sildenafil": {
    "severity": 3,
    "interaction_type": "severe_hypotension",
    "evidence_source": "Absolute contraindication"
  },
  "fluoxetine::tramadol": {
    "severity": 3,
    "interaction_type": "serotonin_syndrome",
    "evidence_source": "Standard clinical knowledge"
  },
  "alcohol::metronidazole": {
    "severity": 2,
    "interaction_type": "disulfiram_like_reaction",
    "evidence_source": "Standard clinical knowledge"
  },
  "atorvastatin::grapefruit_juice": {
    "severity": 2,
    "interaction_type": "increased_statin_toxicity",
    "evidence_source": "Standard clinical knowledge"
  },
  "allopurinol::azathioprine": {
    "severity": 3,
    "interaction_type": "bone_marrow_suppression",
    "evidence_source": "Standard clinical knowledge"
  },
  "potassium_chloride::spironolactone": {
    "severity": 3,
    "interaction_type": "hyperkalemia",
    "evidence_source": "Standard clinical knowledge"
  },
  "citalopram::fluconazole": {
    "severity": 2,
    "interaction_type": "qt_prolongation",
    "evidence_source": "Standard clinical knowledge"
  },
  "calcium_carbonate::levothyroxine": {
    "severity": 1,
    "interaction_type": "decreased_absorption",
    "evidence_source": "Standard clinical knowledge"
  },
  "methotrexate::trimethoprim": {
    "severity": 3,
    "interaction_type": "bone_marrow_suppression",
    "evidence_source": "Standard clinical knowledge"
  },
  "ibuprofen::warfarin": {
    "severity": 3,
    "interaction_type": "increased_bleeding_risk",
    "evidence_source": "Standard clinical knowledge"
  },
  "aspirin::warfarin": {
    "severity": 3,
    "interaction_type": "increased_bleeding_risk",
    "evidence_source": "Standard clinical knowledge"
  },
  "amiodarone::simvastatin": {
    "severity": 2,
    "interaction_type": "myopathy_risk",
    "evidence_source": "Standard clinical knowledge"
  }
};
const ALL_DRUGS = [
  "acetaminophen",
  "albuterol",
  "alcohol",
  "allopurinol",
  "amiodarone",
  "amlodipine",
  "amoxicillin",
  "aspirin",
  "atorvastatin",
  "azathioprine",
  "azithromycin",
  "bupropion",
  "calcium_carbonate",
  "cetirizine",
  "ciprofloxacin",
  "citalopram",
  "clarithromycin",
  "clonazepam",
  "clopidogrel",
  "digoxin",
  "duloxetine",
  "escitalopram",
  "fluconazole",
  "fluoxetine",
  "fluticasone",
  "gabapentin",
  "grapefruit_juice",
  "hydrochlorothiazide",
  "ibuprofen",
  "levothyroxine",
  "lisinopril",
  "lithium",
  "loratadine",
  "losartan",
  "meloxicam",
  "metformin",
  "methotrexate",
  "metronidazole",
  "nitroglycerin",
  "omeprazole",
  "pantoprazole",
  "phenytoin",
  "potassium_chloride",
  "rosuvastatin",
  "sertraline",
  "sildenafil",
  "simvastatin",
  "spironolactone",
  "theophylline",
  "tramadol",
  "trazodone",
  "trimethoprim",
  "valproic_acid",
  "venlafaxine",
  "verapamil",
  "vitamin_d",
  "warfarin",
  "zolpidem"
];
const MODEL_WEIGHTS = {
  "drug_acetaminophen": -1.1411302422704643,
  "drug_albuterol": -0.9153826194713212,
  "drug_alcohol": 0.7110143914203099,
  "drug_allopurinol": 0.7431992657390927,
  "drug_amiodarone": 0.9905513951853269,
  "drug_amlodipine": -1.3611753392949286,
  "drug_amoxicillin": -0.8122583358414394,
  "drug_aspirin": 0.4391604466246115,
  "drug_atorvastatin": -1.0724804972968611,
  "drug_azathioprine": 0.7431992657390927,
  "drug_azithromycin": 0.624252863592217,
  "drug_bupropion": -0.8442075734622764,
  "drug_calcium_carbonate": 1.41410591478997,
  "drug_cetirizine": -1.3069638601791242,
  "drug_ciprofloxacin": 0.6923125437743975,
  "drug_citalopram": 0.7341650008008087,
  "drug_clarithromycin": 0.6452671154651578,
  "drug_clonazepam": -0.9234604539116458,
  "drug_clopidogrel": 1.4059312634849153,
  "drug_digoxin": 0.7008566157948805,
  "drug_duloxetine": -0.9229433711741736,
  "drug_escitalopram": -0.7336995608175128,
  "drug_fluconazole": 0.7341650008008087,
  "drug_fluoxetine": 0.6723980876759983,
  "drug_fluticasone": -0.9153826194713212,
  "drug_gabapentin": -0.9302526173323997,
  "drug_grapefruit_juice": 1.5077669518826955,
  "drug_hydrochlorothiazide": 0.6880106167831544,
  "drug_ibuprofen": -0.2586704353223025,
  "drug_levothyroxine": -0.9681736568734769,
  "drug_lisinopril": -0.7431221647586645,
  "drug_lithium": 0.6880106167831544,
  "drug_loratadine": -1.2102767527398928,
  "drug_losartan": -0.8855505899785392,
  "drug_meloxicam": -0.6897226234211633,
  "drug_metformin": -1.2437859779159692,
  "drug_methotrexate": 0.7545093609729715,
  "drug_metronidazole": 0.7110143914203099,
  "drug_nitroglycerin": 0.7102507354651483,
  "drug_omeprazole": -0.9781445817868963,
  "drug_pantoprazole": -1.6025152417859525,
  "drug_phenytoin": 0.705938889272634,
  "drug_potassium_chloride": 0.35698786305383107,
  "drug_rosuvastatin": -0.7336487689450707,
  "drug_sertraline": -0.8430767929238288,
  "drug_sildenafil": 0.7102507354651483,
  "drug_simvastatin": 1.0115656470581942,
  "drug_spironolactone": 1.5060662329900392,
  "drug_theophylline": 0.6923125437743975,
  "drug_tramadol": 0.6723980876759983,
  "drug_trazodone": -0.8873510919986262,
  "drug_trimethoprim": 0.7545093609729715,
  "drug_valproic_acid": 0.705938889272634,
  "drug_venlafaxine": -0.583920711935942,
  "drug_verapamil": 0.7008566157948805,
  "drug_vitamin_d": -0.9302526173323997,
  "drug_warfarin": 1.3907667640413073,
  "drug_zolpidem": -1.041711248957209,
  "age": -0.0017207644113836557,
  "renal_function_crcl": -0.0025392717463884754,
  "liver_function_ast": -0.01055115119103176
};
const MODEL_INTERCEPT = 1.2364833770882195;
