# ICD 10 codes are 3 digits for first level (categories) and 4 digits for second level (subcategories).
# 'V' codes are excluded because they are codes for external causes of morbidity and mortality.


# import sys
# import _pickle as pickle
# import numpy as np
# import pandas as pd


# icd_mapping = {
#     'M': 'C50',  # Malignant neoplasm of breast
#     'B': 'D24'  # Benign neoplasm of breast
# }


# def convert_to_icd(diagnosis):
#     return icd_mapping.get(diagnosis)


# if __name__ == '__main__':
    
#     from ucimlrepo import fetch_ucirepo
    
#     breast_cancer_wisconsin_diagnostic = fetch_ucirepo(id=17)
#     X = breast_cancer_wisconsin_diagnostic.data.feature
#     y = breast_cancer_wisconsin_diagnostic.data.targets

#     # print(breast_cancer_wisconsin_diagnostic.variables)
    
#     # Convert features and targets to df
#     # df = pd.DataFrame(X, columns=breast_cancer_wisconsin_diagnostic.variables['feature'])
    
#     feature_names = breast_cancer_wisconsin_diagnostic.variables[breast_cancer_wisconsin_diagnostic.variables['role'] == 'Feature']['name'].tolist()
#     df = pd.DataFrame(X, columns=feature_names)
#     df['Diagnosis'] = y

#     # Convert Diagnosis column to ICD codes
#     df['ICD_Code'] = df['Diagnosis'].apply(convert_to_icd)

#     # Convert Diagnosis column to binary (0 for Benign, 1 for Malignant)
#     df['Diagnosis'] = df['Diagnosis'].map({'M': 1, 'B': 0})

#     # Output files
#     outFile = sys.argv[1]
#     pickle.dump(df['ID'].tolist(), open(outFile+'.ids', 'wb'), -1)
#     pickle.dump(df.drop(columns=['ID', 'Diagnosis', 'ICD_Code']).to_numpy(), open(outFile+'.matrix', 'wb'), -1)
#     pickle.dump({'0': 'Benign', '1': 'Malignant'}, open(outFile+'.types', 'wb'), -1)




import sys
import _pickle as pickle
import numpy as np
import pandas as pd

icd_mapping = {
    'M': 'C50',  # Malignant neoplasm of breast
    'B': 'D24'  # Benign neoplasm of breast
}

def convert_to_icd(diagnosis):
    return icd_mapping.get(diagnosis)

if __name__ == '__main__':

    df = pd.read_csv('wdbc.data', header=None)

    df.columns = ['ID', 'Diagnosis'] + [f'feature_{i}' for i in range(1, 31)]

    # Convert Diagnosis column to ICD codes
    df['ICD_Code'] = df['Diagnosis'].apply(convert_to_icd)

    # Convert Diagnosis column to binary (0 for Benign, 1 for Malignant)
    df['Diagnosis'] = df['Diagnosis'].map({'M': 1, 'B': 0})

    # Output files
    outFile = sys.argv[1]
    pickle.dump(df['ID'].tolist(), open(outFile+'.ids', 'wb'), -1)
    pickle.dump(df.drop(columns=['ID', 'Diagnosis', 'ICD_Code']).to_numpy(), open(outFile+'.matrix', 'wb'), -1)
    pickle.dump({'0': 'Benign', '1': 'Malignant'}, open(outFile+'.types', 'wb'), -1)
