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


def rescale(data, data_range, scale_range):
    return ((data - data_range[0]) / (data_range[1] - data_range[0])) * (scale_range[1] - scale_range[0]) + scale_range[0]





# ////////


# columns for prediction

prediction = [(H1_prepr + [A1], H1 + [A1]), (H2_prepr + [A2], H2 + [A2]), (H3_prepr + [A3], H3 + [A3])]





def preprocess(data, prediction_or_treatment, step):
    if len(data.shape) < 2:
        data = pd.DataFrame([data], columns=data.index)
    # dropping unused columns
    if prediction_or_treatment == 'prediction':
        data_cleaned = data[prediction[step - 1][0]]
    else:
        data_cleaned = data[treats[step - 1][0]]
    # changing packs/year to numerical
    data_cleaned.loc[data_cleaned['Smoking status (Packs/Year)'] == '>20', 'Smoking status (Packs/Year)'] = '20'
    data_cleaned = data_cleaned.astype({'Smoking status (Packs/Year)': 'float64'})

    # removing missing values
    for c in data_cleaned.columns:
        if data_cleaned[c].isnull().values.any():
            data_cleaned[c] = data_cleaned[c].fillna(missing_values[c])

    # preprocessing variables
    data_cleaned.loc[data_cleaned['Aspiration rate Pre-therapy'] == 'N', 'Aspiration rate Pre-therapy'] = 0
    data_cleaned.loc[data_cleaned['Aspiration rate Pre-therapy'] == 'Y', 'Aspiration rate Pre-therapy'] = 1

    data_cleaned.loc[data_cleaned['Pathological Grade'] == 'I', 'Pathological Grade'] = 1
    data_cleaned.loc[data_cleaned['Pathological Grade'] == 'II', 'Pathological Grade'] = 2
    data_cleaned.loc[data_cleaned['Pathological Grade'] == 'III', 'Pathological Grade'] = 3
    data_cleaned.loc[data_cleaned['Pathological Grade'] == 'IV', 'Pathological Grade'] = 4

    data_cleaned['R Laterality'] = 0
    data_cleaned['L Laterality'] = 0
    data_cleaned.loc[(data_cleaned['Tm Laterality (R/L)'] == 'R') | (
            data_cleaned['Tm Laterality (R/L)'] == 'Bilateral'), 'R Laterality'] = 1
    data_cleaned.loc[(data_cleaned['Tm Laterality (R/L)'] == 'L') | (
            data_cleaned['Tm Laterality (R/L)'] == 'Bilateral'), 'L Laterality'] = 1

    data_cleaned['BOT subsite'] = 0
    data_cleaned['Tonsil subsite'] = 0
    data_cleaned['Soft Palate subsite'] = 0
    data_cleaned['GPS subsite'] = 0
    data_cleaned.loc[
        data_cleaned['Tumor subsite (BOT/Tonsil/Soft Palate/Pharyngeal wall/GPS/NOS)'] == 'BOT', 'BOT subsite'] = 1
    data_cleaned.loc[data_cleaned[
                         'Tumor subsite (BOT/Tonsil/Soft Palate/Pharyngeal wall/GPS/NOS)'] == 'Tonsil', 'Tonsil subsite'] = 1
    data_cleaned.loc[data_cleaned[
                         'Tumor subsite (BOT/Tonsil/Soft Palate/Pharyngeal wall/GPS/NOS)'] == 'Soft palate', 'Soft Palate subsite'] = 1
    data_cleaned.loc[
        data_cleaned['Tumor subsite (BOT/Tonsil/Soft Palate/Pharyngeal wall/GPS/NOS)'] == 'GPS', 'GPS subsite'] = 1

    data_cleaned.loc[(data_cleaned['T-category'] == 'Tx') | (data_cleaned['T-category'] == 'Tis'), 'T-category'] = 1
    data_cleaned.loc[data_cleaned['T-category'] == 'T1', 'T-category'] = 1
    data_cleaned.loc[data_cleaned['T-category'] == 'T2', 'T-category'] = 2
    data_cleaned.loc[data_cleaned['T-category'] == 'T3', 'T-category'] = 3
    data_cleaned.loc[data_cleaned['T-category'] == 'T4', 'T-category'] = 4

    data_cleaned.loc[data_cleaned['N-category'] == 'N0', 'N-category'] = 0
    data_cleaned.loc[data_cleaned['N-category'] == 'N1', 'N-category'] = 1
    data_cleaned.loc[data_cleaned['N-category'] == 'N2', 'N-category'] = 2
    data_cleaned.loc[data_cleaned['N-category'] == 'N3', 'N-category'] = 3

    data_cleaned.loc[data_cleaned['N-category_8th_edition'] == 'N0', 'N-category_8th_edition'] = 0
    data_cleaned.loc[data_cleaned['N-category_8th_edition'] == 'N1', 'N-category_8th_edition'] = 1
    data_cleaned.loc[data_cleaned['N-category_8th_edition'] == 'N2', 'N-category_8th_edition'] = 2
    data_cleaned.loc[data_cleaned['N-category_8th_edition'] == 'N3', 'N-category_8th_edition'] = 3

    data_cleaned.loc[data_cleaned['AJCC 7th edition'] == 'I', 'AJCC 7th edition'] = 1
    data_cleaned.loc[data_cleaned['AJCC 7th edition'] == 'II', 'AJCC 7th edition'] = 2
    data_cleaned.loc[data_cleaned['AJCC 7th edition'] == 'III', 'AJCC 7th edition'] = 3
    data_cleaned.loc[data_cleaned['AJCC 7th edition'] == 'IV', 'AJCC 7th edition'] = 4

    data_cleaned.loc[data_cleaned['AJCC 8th edition'] == 'I', 'AJCC 8th edition'] = 1
    data_cleaned.loc[data_cleaned['AJCC 8th edition'] == 'II', 'AJCC 8th edition'] = 2
    data_cleaned.loc[data_cleaned['AJCC 8th edition'] == 'III', 'AJCC 8th edition'] = 3
    data_cleaned.loc[data_cleaned['AJCC 8th edition'] == 'IV', 'AJCC 8th edition'] = 4

    data_cleaned.loc[data_cleaned['Gender'] == 'Male', 'Gender'] = 0
    data_cleaned.loc[data_cleaned['Gender'] == 'Female', 'Gender'] = 1

    data_cleaned['White/Caucasian'] = 0
    data_cleaned['Hispanic/Latino'] = 0
    data_cleaned['African American/Black'] = 0
    data_cleaned['Asian'] = 0
    data_cleaned['Native American'] = 0
    data_cleaned.loc[data_cleaned['Race'] == 'White/Caucasion', 'White/Caucasian'] = 1
    data_cleaned.loc[data_cleaned['Race'] == 'Hispanic/Latino', 'Hispanic/Latino'] = 1
    data_cleaned.loc[data_cleaned['Race'] == 'African American/Black', 'African American/Black'] = 1
    data_cleaned.loc[data_cleaned['Race'] == 'Asian', 'Asian'] = 1
    data_cleaned.loc[data_cleaned['Race'] == 'Native American', 'Native American'] = 1

    data_cleaned.loc[data_cleaned['HPV/P16 status'] == 'Positive', 'HPV/P16 status'] = 1
    data_cleaned.loc[data_cleaned['HPV/P16 status'] == 'Negative', 'HPV/P16 status'] = -1
    data_cleaned.loc[data_cleaned['HPV/P16 status'] == 'Unknown', 'HPV/P16 status'] = 0

    data_cleaned.loc[data_cleaned[
                         'Smoking status at Diagnosis (Never/Former/Current)'] == 'Formar', 'Smoking status at Diagnosis (Never/Former/Current)'] = 1
    data_cleaned.loc[data_cleaned[
                         'Smoking status at Diagnosis (Never/Former/Current)'] == 'Current', 'Smoking status at Diagnosis (Never/Former/Current)'] = 2
    data_cleaned.loc[data_cleaned[
                         'Smoking status at Diagnosis (Never/Former/Current)'] == 'Never', 'Smoking status at Diagnosis (Never/Former/Current)'] = 0

    data_cleaned["Num Affected Lymph nodes"] = data_cleaned["Affected Lymph node"].apply(lambda x: len(x.split(',')))

    if (prediction_or_treatment == 'pred') or (step > 1):
        data_cleaned.loc[
            data_cleaned['Decision 1 (Induction Chemo) Y/N'] == 'N', 'Decision 1 (Induction Chemo) Y/N'] = 0
        data_cleaned.loc[
            data_cleaned['Decision 1 (Induction Chemo) Y/N'] == 'Y', 'Decision 1 (Induction Chemo) Y/N'] = 1

    if step > 1:
        data_cleaned.loc[(data_cleaned['Prescribed Chemo (Single/doublet/triplet/quadruplet/none/NOS)'] == 'None') | (
                data_cleaned[
                    'Prescribed Chemo (Single/doublet/triplet/quadruplet/none/NOS)'] == 'NOS'), 'Prescribed Chemo (Single/doublet/triplet/quadruplet/none/NOS)'] = 0
        data_cleaned.loc[data_cleaned[
                             'Prescribed Chemo (Single/doublet/triplet/quadruplet/none/NOS)'] == 'Single', 'Prescribed Chemo (Single/doublet/triplet/quadruplet/none/NOS)'] = 1
        data_cleaned.loc[data_cleaned[
                             'Prescribed Chemo (Single/doublet/triplet/quadruplet/none/NOS)'] == 'Doublet', 'Prescribed Chemo (Single/doublet/triplet/quadruplet/none/NOS)'] = 2
        data_cleaned.loc[data_cleaned[
                             'Prescribed Chemo (Single/doublet/triplet/quadruplet/none/NOS)'] == 'Triplet', 'Prescribed Chemo (Single/doublet/triplet/quadruplet/none/NOS)'] = 3
        data_cleaned.loc[data_cleaned[
                             'Prescribed Chemo (Single/doublet/triplet/quadruplet/none/NOS)'] == 'Quadruplet', 'Prescribed Chemo (Single/doublet/triplet/quadruplet/none/NOS)'] = 4

        data_cleaned.loc[data_cleaned['Chemo Modification (Y/N)'] == 'N', 'Chemo Modification (Y/N)'] = 0
        data_cleaned.loc[data_cleaned['Chemo Modification (Y/N)'] == 'Y', 'Chemo Modification (Y/N)'] = 1

        data_cleaned['Dose modified'] = 0
        data_cleaned['Dose delayed'] = 0
        data_cleaned['Dose cancelled'] = 0
        data_cleaned['Regimen modification'] = 0
        data_cleaned.loc[(data_cleaned[
                              'Modification Type (0= no dose adjustment, 1=dose modified, 2=dose delayed, 3=dose cancelled, 4=dose delayed & modified, 5=regimen modification, 9=unknown)'] == 1) | (
                                 data_cleaned[
                                     'Modification Type (0= no dose adjustment, 1=dose modified, 2=dose delayed, 3=dose cancelled, 4=dose delayed & modified, 5=regimen modification, 9=unknown)'] == 4), 'Dose modified'] = 1
        data_cleaned.loc[(data_cleaned[
                              'Modification Type (0= no dose adjustment, 1=dose modified, 2=dose delayed, 3=dose cancelled, 4=dose delayed & modified, 5=regimen modification, 9=unknown)'] == 2) | (
                                 data_cleaned[
                                     'Modification Type (0= no dose adjustment, 1=dose modified, 2=dose delayed, 3=dose cancelled, 4=dose delayed & modified, 5=regimen modification, 9=unknown)'] == 4), 'Dose delayed'] = 1
        data_cleaned.loc[data_cleaned[
                             'Modification Type (0= no dose adjustment, 1=dose modified, 2=dose delayed, 3=dose cancelled, 4=dose delayed & modified, 5=regimen modification, 9=unknown)'] == 3, 'Dose cancelled'] = 1
        data_cleaned.loc[data_cleaned[
                             'Modification Type (0= no dose adjustment, 1=dose modified, 2=dose delayed, 3=dose cancelled, 4=dose delayed & modified, 5=regimen modification, 9=unknown)'] == 5, 'Regimen modification'] = 1

        data_cleaned.loc[data_cleaned['DLT (Y/N)'] == 'N', 'DLT (Y/N)'] = 0
        data_cleaned.loc[data_cleaned['DLT (Y/N)'] == 'Y', 'DLT (Y/N)'] = 1

        data_cleaned['DLT_Other'] = 0
        for index, row in data_cleaned.iterrows():
            if row['DLT_Type'] == 'None':
                continue
            for i in re.split('&|and|,', row['DLT_Type']):
                if i.strip() != '' and data_cleaned.loc[index, dlt_dict[i.strip()]] == 0:
                    data_cleaned.loc[index, dlt_dict[i.strip()]] = 1

        if (prediction_or_treatment == 'pred') or (step > 2):
            data_cleaned.loc[data_cleaned['Decision 2 (CC / RT alone)'] == 'RT alone', 'Decision 2 (CC / RT alone)'] = 0
            data_cleaned.loc[data_cleaned['Decision 2 (CC / RT alone)'] == 'CC', 'Decision 2 (CC / RT alone)'] = 1

    if step > 2:
        data_cleaned['CC Platinum'] = 0
        data_cleaned['CC Cetuximab'] = 0
        data_cleaned['CC Others'] = 0
        data_cleaned.loc[data_cleaned[
                             'CC Regimen(0= none, 1= platinum based, 2= cetuximab based, 3= others, 9=unknown)'] == 1, 'CC Platinum'] = 1
        data_cleaned.loc[data_cleaned[
                             'CC Regimen(0= none, 1= platinum based, 2= cetuximab based, 3= others, 9=unknown)'] == 2, 'CC Cetuximab'] = 1
        data_cleaned.loc[data_cleaned[
                             'CC Regimen(0= none, 1= platinum based, 2= cetuximab based, 3= others, 9=unknown)'] == 3, 'CC Others'] = 1

        data_cleaned.loc[data_cleaned['CC modification (Y/N)'] == 'N', 'CC modification (Y/N)'] = 0
        data_cleaned.loc[data_cleaned['CC modification (Y/N)'] == 'Y', 'CC modification (Y/N)'] = 1

        data_cleaned['DLT_Dermatological 2'] = 0
        data_cleaned['DLT_Neurological 2'] = 0
        data_cleaned['DLT_Gastrointestinal 2'] = 0
        data_cleaned['DLT_Hematological 2'] = 0
        data_cleaned['DLT_Nephrological 2'] = 0
        data_cleaned['DLT_Vascular 2'] = 0
        data_cleaned['DLT_Infection (Pneumonia) 2'] = 0
        data_cleaned['DLT_Other 2'] = 0
        for index, row in data_cleaned.iterrows():
            if row['DLT 2'] == 'None':
                continue
            for i in re.split('&|and|,', row['DLT 2']):
                if i.strip() != '':
                    data_cleaned.loc[index, dlt_dict[i.strip()] + ' 2'] = 1

        if (prediction_or_treatment == 'pred') or (step > 3):
            data_cleaned.loc[
                data_cleaned['Decision 3 Neck Dissection (Y/N)'] == 'N', 'Decision 3 Neck Dissection (Y/N)'] = 0
            data_cleaned.loc[
                data_cleaned['Decision 3 Neck Dissection (Y/N)'] == 'Y', 'Decision 3 Neck Dissection (Y/N)'] = 1

    # selecting needed columns
    if prediction_or_treatment == 'pred':
        data_cleaned = data_cleaned[pred[step - 1][1]]
    else:
        data_cleaned = data_cleaned[treats[step - 1][1]]

    # scaling data to [-1, 1] range
    for c in data_cleaned.columns:
        data_cleaned[c] = rescale(data_cleaned[c], feature_range[c], (-1, 1))

    return data_cleaned

