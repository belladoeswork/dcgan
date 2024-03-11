from sklearn.svm import SVC
from joblib import dump, load
from histories import *
import numpy as np
from processing import *

s = './Patient twin/'
# dictionary of files containing transition models
trans_files = {
    'postTrt_numPosLymphNodes': 'svm_postTrt_numPosLymphNodes_.joblib', 
    'metastasis_months': 'svm_metastasis_months_.joblib', 
    'tumor_size_cm_postTrt': 'svm_tumor_size_cm_postTrt_.joblib',
    'metastasis_months_1': 'svm_metastasis_months_1_.joblib', 
    'pCR': 'svm_pCR_.joblib', 
    'near_pCR': 'svm_near_pCR_.joblib', 
    'metastasis_1': 'svm_metastasis_1_.joblib', 
    'taxane': 'svm_taxane_.joblib',
    'metastasis_months_2': 'svm_metastasis_months_2_.joblib', 
    'estrogen_receptor': 'svm_estrogen_receptor_.joblib', 
    'letrozole': 'svm_letrozole_.joblib', 
    'aromatase_inhibitor': 'svm_aromatase_inhibitor_.joblib', 
    'tamoxifen': 'svm_tamoxifen_.joblib', 
    'anti_estrogen': 'svm_anti_estrogen_.joblib', 
    'other_treatment': 'svm_other_treatment_.joblib'
}

# outcome encodings in the transition models
outcome_dicts = {'Prescribed Chemo (Single/doublet/triplet/quadruplet/none/NOS)': {0: -1.0,
  1: 0.5,
  2: 0.0,
  3: 1.0},
 'Chemo Modification (Y/N)': {0: -1.0, 1: 1.0},
 'Dose modified': {0: -1.0, 1: 1.0},
 'Dose delayed': {0: -1.0, 1: 1.0},
 'Dose cancelled': {0: -1.0, 1: 1.0},
 'Regimen modification': {0: -1.0, 1: 1.0},
 'DLT (Y/N)': {0: -1.0, 1: 1.0},
 'DLT_Dermatological': {0: -1.0,
  1: -0.33333333333333337,
  2: 0.3333333333333333,
  3: 1.0},
 'DLT_Neurological': {0: -1.0,
  1: -0.33333333333333337,
  2: 0.3333333333333333,
  3: 1.0},
 'DLT_Gastrointestinal': {0: -1.0,
  1: -0.33333333333333337,
  2: 1.0,
  3: 0.3333333333333333},
 'DLT_Hematological': {0: -1.0, 1: -0.5, 2: 0.5, 3: 1.0},
 'DLT_Nephrological': {0: -1.0, 1: 1.0},
 'DLT_Vascular': {0: -1.0, 1: -0.33333333333333337, 2: 1.0},
 'DLT_Infection (Pneumonia)': {0: -1.0, 1: 1.0},
 'DLT_Other': {0: -1.0, 1: 1.0},
 'DLT_Grade': {0: -1.0, 1: 0.5, 2: -0.5, 3: 0.0, 4: 1.0},
 'No imaging (0=N, 1=Y)': {0: -1.0, 1: 1.0},
 'CR Primary': {0: -1.0, 1: 1.0},
 'CR Nodal': {0: -1.0, 1: 1.0},
 'PR Primary': {0: -1.0, 1: 1.0},
 'PR Nodal': {0: -1.0, 1: 1.0},
 'SD Primary': {0: -1.0, 1: 1.0},
 'SD Nodal': {0: -1.0, 1: 1.0},
 'CC Platinum': {0: -1.0, 1: 1.0, 2: -1.0, 3: -1.0},
 'CC Cetuximab': {0: -1.0, 1: -1.0, 2: 1.0, 3: -1.0},
 'CC Others': {0: -1.0, 1: -1.0, 2: -1.0, 3: 1.0},
 'CC modification (Y/N)': {0: -1.0, 1: 1.0},
 'CR Primary 2': {0: 1.0, 1: -1.0},
 'CR Nodal 2': {0: -1.0, 1: 1.0},
 'PR Primary 2': {0: -1.0, 1: 1.0},
 'PR Nodal 2': {0: 1.0, 1: -1.0},
 'SD Primary 2': {0: -1.0, 1: 1.0},
 'SD Nodal 2': {0: -1.0, 1: 1.0},
 'DLT_Dermatological 2': {0: -1.0, 1: 1.0},
 'DLT_Neurological 2': {0: -1.0, 1: 1.0},
 'DLT_Gastrointestinal 2': {0: -1.0, 1: 1.0},
 'DLT_Hematological 2': {0: -1.0, 1: 1.0},
 'DLT_Nephrological 2': {0: -1.0, 1: 1.0},
 'DLT_Vascular 2': {0: -1.0, 1: 1.0},
 'DLT_Other 2': {0: -1.0, 1: 1.0},
 'Overall Survival (4 Years)': {0: -1.0, 1: 1.0},
 'Feeding tube 6m': {0: -1.0, 1: 1.0},
 'Aspiration rate Post-therapy': {0: -1.0, 1: 1.0}
 }

default_outcomes = {
    A1: {
        'postTrt_numPosLymphNodes':0, 
        'metastasis_months':0, 
        'tumor_size_cm_postTrt':0
    },
    A2: {
        'metastasis_months_1':0 , 
        'pCR': 0, 
        'near_pCR': 0, 
        'metastasis_1': 0, 
        'taxane':0
    },
    A3: {'metastasis_months_2': 0, 
        'estrogen_receptor': 0, 
        'letrozole': 0,
        'aromatase_inhibitor': 0, 
        'tamoxifen': 0, 
        'anti_estrogen': 0, 
        'other_treatment': 0
    },
    A4: {}
}

# derived_outcomes = {
#     'Dysphagia': (lambda p: max(p['Feeding tube 6m'], p['Aspiration rate Post-therapy']))
# }


def load_patient_twin():
    trans_model = {}
    # importing models
    for key, value in trans_files.items():
        path = s + value
        trans_model[key] = load(path)
    return trans_model


def parse_history(history, action):
    if len(history.shape) > 1:
        sample = np.concatenate((history.to_numpy(), history.multiply(action, axis='index').to_numpy()), axis=1)

    else:
        sample = np.concatenate((history.to_numpy(), history.multiply(action, axis='index').to_numpy()),
                                axis=None).reshape(1, -1)

    return sample


def compute_outcome(history, action, model, outcome_dict):
    return outcome_dict[model.predict(parse_history(history, action))[0]]


def next_state(history, action, action_value, outcomes, trans_model):
    if np.array(outcomes).size == 1:
            outcomes = [outcomes]
    y = pd.Series(index = history.index.tolist() + [action] + outcomes, dtype='float64')
    y.loc[:] = 0
    y.loc[history.index] = history
    y.loc[action] = action_value
    for o in outcomes:
        if (o in default_outcomes[action].keys()) and (action_value == -1):
            y.loc[o] = default_outcomes[action][o]
        # elif o in derived_outcomes.keys():
        #     y.loc[o] = derived_outcomes[o](y)
        else:
            y.loc[o] = compute_outcome(history, action_value, trans_model[o], outcome_dicts[o])
    return y


def predict(data, step):
    trans_model = load_patient_twin()
    predicted = []
    for index, row in data.iterrows():
        predicted.append(next_state(data.loc[index, histories[step - 1]], decisions[step - 1], data.loc[index, decisions[step - 1]], states[step - 1], trans_model))
    return pd.DataFrame(predicted)
