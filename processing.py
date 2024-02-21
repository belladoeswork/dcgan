import pandas as pd
from histories import *
import re


# dictionary with min, and max values for each variable, needed for filling missing values and rescaling
feature_range = {
    'Age at Diagnosis (Calculated)': (20.95, 85.8972222222222),
    'Pathological Grade': (1, 4),
    'Gender': (0, 1),
    'HPV/P16 status': (-1, 1),
    'T-category': (1, 4),
    'N-category': (0, 3),
    'N-category_8th_edition': (0, 3),
    'AJCC 7th edition': (2, 4),
    'AJCC 8th edition': (1, 4),
    'Smoking status at Diagnosis (Never/Former/Current)': (0, 2),
    'Smoking status (Packs/Year)': (0.0, 120.0),
    'Aspiration rate Pre-therapy': (0, 1),
    'Num Affected Lymph nodes': (1, 10),
    'R Laterality': (0, 1),
    'L Laterality': (0, 1),
    'BOT subsite': (0, 1),
    'Tonsil subsite': (0, 1),
    'Soft Palate subsite': (0, 1),
    'GPS subsite': (0, 1),
    'White/Caucasian': (0, 1),
    'Hispanic/Latino': (0, 1),
    'African American/Black': (0, 1),
    'Asian': (0, 1),
    'Native American': (0, 1),
    'Decision 1 (Induction Chemo) Y/N': (0, 1),
    'Prescribed Chemo (Single/doublet/triplet/quadruplet/none/NOS)': (0, 4),
    'Chemo Modification (Y/N)': (0, 1),
    'Dose modified': (0, 1),
    'Dose delayed': (0, 1),
    'Dose cancelled': (0, 1),
    'Regimen modification': (0, 1),
    'DLT (Y/N)': (0, 1),
    'DLT_Dermatological': (0, 3),
    'DLT_Neurological': (0, 3),
    'DLT_Gastrointestinal': (0, 3),
    'DLT_Hematological': (0, 4),
    'DLT_Nephrological': (0, 1),
    'DLT_Vascular': (0, 3),
    'DLT_Infection (Pneumonia)': (0, 1),
    'DLT_Other': (0, 1),
    'DLT_Grade': (0, 4),
    'No imaging (0=N, 1=Y)': (0, 1),
    'CR Primary': (0, 1),
    'CR Nodal': (0, 1),
    'PR Primary': (0, 1),
    'PR Nodal': (0, 1),
    'SD Primary': (0, 1),
    'SD Nodal': (0, 1),
    'Decision 2 (CC / RT alone)': (0, 1),
    'CC Platinum': (0, 1),
    'CC Cetuximab': (0, 1),
    'CC Others': (0, 1),
    'CC modification (Y/N)': (0, 1),
    'CR Primary 2': (0.0, 1.0),
    'CR Nodal 2': (0.0, 1.0),
    'PR Primary 2': (0.0, 1.0),
    'PR Nodal 2': (0.0, 1.0),
    'SD Primary 2': (0.0, 1.0),
    'SD Nodal 2': (0.0, 1.0),
    'DLT_Dermatological 2': (0, 1),
    'DLT_Neurological 2': (0, 1),
    'DLT_Gastrointestinal 2': (0, 1),
    'DLT_Hematological 2': (0, 1),
    'DLT_Nephrological 2': (0, 1),
    'DLT_Vascular 2': (0, 1),
    'DLT_Other 2': (0, 1),
    'Decision 3 Neck Dissection (Y/N)': (0, 1),
    'Overall Survival (4 Years)': (0, 1),
    'Feeding tube 6m': (0, 1),
    'Aspiration rate Post-therapy': (0, 1),
    'Dysphagia': (0, 1)
}

# mapping between DLT_Type and new columns
dlt_dict = {
     'Allergic reaction to Cetuximab': 'DLT_Other',
     'Cardiological (A-fib)': 'DLT_Other',
     'Dermatological': 'DLT_Dermatological',
     'Failure to Thrive': 'DLT_Other',
     'Failure to thrive': 'DLT_Other',
     'GIT [elevated liver enzymes]': 'DLT_Gastrointestinal',
     'Gastrointestina': 'DLT_Gastrointestinal',
     'Gastrointestinal': 'DLT_Gastrointestinal',
     'General': 'DLT_Other',
     'Hematological': 'DLT_Hematological',
     'Hematological (Neutropenia)': 'DLT_Hematological',
     'Hyponatremia': 'DLT_Other',
     'Immunological': 'DLT_Other',
     'Infection': 'DLT_Infection (Pneumonia)',
     'NOS': 'DLT_Other',
     'Nephrological': 'DLT_Nephrological',
     'Nephrological (ARF)': 'DLT_Nephrological',
     'Neurological': 'DLT_Neurological',
     'Neutropenia': 'DLT_Hematological',
     'Nutritional': 'DLT_Other',
     'Pancreatitis': 'DLT_Other',
     'Pulmonary': 'DLT_Other',
     'Respiratory (Pneumonia)': 'DLT_Infection (Pneumonia)',
     'Sepsis': 'DLT_Infection (Pneumonia)',
     'Suboptimal response to treatment' : 'DLT_Other',
     'Vascular': 'DLT_Vascular'
}

# columns to preprocess if the goal of the preprocessing is treatment
treats = [(H1_prepr, H1), (H2_prepr, H2), (H3_prepr, H3)]

# columns to preprocess if the goal of the preprocessing is prediction
pred = [(H1_prepr + [A1], H1 + [A1]), (H2_prepr + [A2], H2 + [A2]), (H3_prepr + [A3], H3 + [A3])]


def rescale(data, data_range, scale_range):
    return ((data - data_range[0]) / (data_range[1] - data_range[0])) * (scale_range[1] - scale_range[0]) + scale_range[0]

