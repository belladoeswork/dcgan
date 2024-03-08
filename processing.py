import pandas as pd
from histories import *
import re


# dictionary with min, and max values for each variable, needed for filling missing values and rescaling
# feature_range = {
# 'biopsy_preTreat': (1.0, 1.0),
# 'pCR_postTrt_days': (84, 84),
# 'tumor_size_cm_preTrt_preSurgery': (0.0, 25.0),
# 'tumor_size_cm_secondAxis_preTrt_preSurgery': (3.0, 8.0),
# 'tumor_size_cm_postTrt': (0.0, 4.0),
# 'preTrt_totalLymphNodes': (0, 40),
# 'preTrt_numPosLymphNodes': (0, 33),
# 'postTrt_numPosLymphNodes': (0, 17),
# 'preTrt_posDichLymphNodes': (0, 1),
# 'hist_grade': (1, 3),
# 'clinical_AJCC_stage_I': (0, 1),
# 'clinical_AJCC_stage_II': (0, 1),
# 'clinical_AJCC_stage_IIA': (0, 1),
# 'clinical_AJCC_stage_IIB': (0, 1),
# 'clinical_AJCC_stage_III': (0, 1),
# 'clinical_AJCC_stage_IIIA': (0, 1),
# 'clinical_AJCC_stage_IIIB': (0, 1),
# 'clinical_AJCC_stage_IIIC': (0, 1),
# 'clinical_AJCC_stage_IV': (0, 1),
# 'nuclear_grade_preTrt': (1, 3),
# 'pCR': (0, 1),
# 'near_pCR': (0, 1),
# 'RFS': (0, 1),
# 'DFS': (0, 1),
# 'OS': (0, 1),
# 'metastasis': (0, 1),
# 'metastasis_months': (1, 35),
# 'dead': (0, 1),
# 'died_from_cancer_if_dead': (0, 1),
# 'age': (24, 92),
# 'ER_preTrt': (0, 1),
# 'ER_fmolmg_preTrt': (0, 620),
# 'ESR1_preTrt': (0, 1),
# 'ERbb2_preTrt': (0, 1),
# 'Erbeta_preTrt': (0, 1),
# 'ERBB2_CPN_amplified': (0, 1),
# 'PR_preTrt': (0, 1),
# 'PR_percentage_preTrt': (0, 95),
# 'PR_fmolmg_preTrt': (0, 990),
# 'HER2_preTrt': (0, 1),
# 'HER2_fish_cont_score_preTrt': (0, 20),
# 'cytokeratin5_pos': (0, 1),
# 'top2atri_preTrt': (-1, 1),
# 'topoihc_preTrt': (0, 90),
# 'S_phase': (1, 36),
# 'intarvenous': (0, 1),
# 'intramuscular': (0, 1),
# 'oral': (0, 1),
# 'radiotherapyClass': (0, 1),
# 'hormone_therapyClass': (0, 1),
# 'postmenopausal_only': (0, 1),
# 'anthracycline': (0, 1),
# 'taxane': (0, 1),
# 'anti_estrogen': (0, 1),
# 'aromatase_inhibitor': (0, 1),
# 'estrogen_receptor_blocker': (0, 1),
# 'estrogen_receptor_blocker_and_stops_production': (0, 1),
# 'estrogen_receptor_blocker_and_eliminator': (0, 1),
# 'anti_HER2': (0, 1),
# 'tamoxifen': (0, 1),
# 'doxorubicin': (0, 1),
# 'epirubicin': (0, 1),
# 'docetaxel': (0, 1),
# 'capecitabine': (0, 1),
# 'fluorouracil': (0, 1),
# 'paclitaxel': (0, 1),
# 'cyclophosphamide': (0, 1),
# 'anastrozole': (0, 1),
# 'fulvestrant': (0, 1),
# 'gefitinib': (0, 1),
# 'trastuzumab': (0, 1),
# 'letrozole': (0, 1),
# 'chemotherapy': (0, 1),
# 'hormone_therapy': (0, 1),
# 'no_treatment': (0, 1),
# 'methotrexate': (0, 1),
# 'cetuximab': (0, 1),
# 'carboplatin': (0, 1),
# 'other_treatment': (0, 1),
# 'taxaneGeneral': (0, 1),
# 'preTrt_lymph_node_status_N0': (0, 1),
# 'preTrt_lymph_node_status_N1': (0, 1),
# 'preTrt_lymph_node_status_N2': (0, 1),
# 'preTrt_lymph_node_status_N3': (0, 1),
# 'preTrt_lymph_node_status_ND': (0, 1),
# 'preTrt_lymph_node_status_positive': (0, 1),
# 'postTrt_lymph_node_status_N0': (0, 1),
# 'postTrt_lymph_node_status_N1': (0, 1),
# 'postTrt_lymph_node_status_N1a': (0, 1),
# 'postTrt_lymph_node_status_N2': (0, 1),
# 'postTrt_lymph_node_status_N2a': (0, 1),
# 'postTrt_lymph_node_status_N3': (0, 1),
# 'postTrt_lymph_node_status_positive': (0, 1),
# 'tumor_stage_preTrt_T0': (0, 1),
# 'tumor_stage_preTrt_T1': (0, 1),
# 'tumor_stage_preTrt_T2': (0, 1),
# 'tumor_stage_preTrt_T3': (0, 1),
# 'tumor_stage_preTrt_T4': (0, 1),
# 'tumor_stage_postTrt_T0': (0, 1),
# 'tumor_stage_postTrt_T1': (0, 1),
# 'tumor_stage_postTrt_T1a': (0, 1),
# 'tumor_stage_postTrt_T1b': (0, 1),
# 'tumor_stage_postTrt_T1c': (0, 1),
# 'tumor_stage_postTrt_T1mic': (0, 1),
# 'tumor_stage_postTrt_T2': (0, 1),
# 'tumor_stage_postTrt_Tis': (0, 1),
# 'pam50_Basal': (0, 1),
# 'pam50_Claudin': (0, 1),
# 'pam50_Her2': (0, 1),
# 'pam50_Luminal A': (0, 1),
# 'pam50_Luminal B': (0, 1),
# 'pam50_Normal': (0, 1),
# 'pCR_spectrum_CR': (0, 1),
# 'pCR_spectrum_EPD': (0, 1),
# 'pCR_spectrum_NCR': (0, 1),
# 'pCR_spectrum_NE': (0, 1),
# 'pCR_spectrum_PD': (0, 1),
# 'pCR_spectrum_PR': (0, 1),
# 'pCR_spectrum_SD': (0, 1),
# 'RCB_0': (0, 1),
# 'RCB_0/I': (0, 1),
# 'RCB_1': (0, 1),
# 'RCB_2': (0, 1),
# 'RCB_3': (0, 1),
# 'RCB_II': (0, 1),
# 'RCB_III': (0, 1),
# 'race_asian': (0, 1),
# 'race_black': (0, 1),
# 'race_hispanic': (0, 1),
# 'race_mixed': (0, 1),
# 'race_white': (0, 1),
# 'menopausal_status_post': (0, 1),
# 'menopausal_status_pre': (0, 1),
# 'HER2_IHC_score_preTrt_0': (0, 1),
# 'HER2_IHC_score_preTrt_1': (0, 1),
# 'HER2_IHC_score_preTrt_2': (0, 1),
# 'HER2_IHC_score_preTrt_3': (0, 1),
# 'HER2_IHC_score_preTrt_ND': (0, 1),
# 'HER2_IHC_score_preTrt_NEG': (0, 1),
# 'ploidy_aneuploid': (0, 1),
# 'ploidy_diploid': (0, 1),
# 'ploidy_multiploid': (0, 1),
# 'surgery_breast preserving': (0, 1),
# 'surgery_mastectomy': (0, 1),
# 'neoadjuvant_or_adjuvant_adj': (0, 1),
# 'neoadjuvant_or_adjuvant_mixed': (0, 1),
# 'neoadjuvant_or_adjuvant_neo': (0, 1),
# 'neoadjuvant_or_adjuvant_unspecified': (0, 1)
# }


feature_range = {'biopsy_preTreat': (1.0, 1.0),
'pCR_postTrt_days': (84, 84),
'tumor_size_cm_preTrt_preSurgery': (0.0, 25.0),
'tumor_size_cm_secondAxis_preTrt_preSurgery': (3.0, 8.0),
'tumor_size_cm_postTrt': (0.0, 4.0),
'preTrt_totalLymphNodes': (0, 40),
'preTrt_numPosLymphNodes': (0, 33),
'postTrt_numPosLymphNodes': (0, 17),
'preTrt_posDichLymphNodes': (0, 1),
'hist_grade': (1, 3),
'nuclear_grade_preTrt': (1, 3),
'pCR': (0, 1),
'near_pCR': (0, 1),
'RFS': (0, 1),
'DFS': (0, 1),
'OS': (0, 1),
'metastasis': (0, 1),
'metastasis_months': (1, 35),
'died_from_cancer_if_dead': (0, 1),
'age': (24, 92),
'ER_preTrt': (0, 1),
'ER_fmolmg_preTrt': (0, 620),
'ESR1_preTrt': (0, 1),
'ERbb2_preTrt': (0, 1),
'Erbeta_preTrt': (0, 1),
'ERBB2_CPN_amplified': (0, 1),
'PR_preTrt': (0, 1),
'PR_percentage_preTrt': (0, 95),'PR_fmolmg_preTrt': (0, 990),
'HER2_preTrt': (0, 1),
'HER2_fish_cont_score_preTrt': (0, 20),
'cytokeratin5_pos': (0, 1),
'top2atri_preTrt': (-1, 1),
'topoihc_preTrt': (0, 90),
'S_phase': (1, 36),
'intarvenous': (0, 1),
'intramuscular': (0, 1),
'oral': (0, 1),
'radiotherapy': (0.0, 1.0),
'postmenopausal_only': (0, 1),
'anthracycline': (0, 1),
'taxane': (0, 1),
'anti_estrogen': (0, 1),
'aromatase_inhibitor': (0, 1),
'estrogen_receptor_blocker': (0, 1),
'estrogen_receptor_blocker_and_stops_production': (0, 1),
'estrogen_receptor_blocker_and_eliminator': (0, 1),
'anti_HER2': (0, 1),
'tamoxifen': (0, 1),
'doxorubicin': (0, 1),
'epirubicin': (0, 1),
'docetaxel': (0, 1),
'capecitabine': (0, 1),
'fluorouracil': (0, 1),
'paclitaxel': (0, 1),
'cyclophosphamide': (0, 1),
'anastrozole': (0, 1),
'fulvestrant': (0, 1),
'gefitinib': (0, 1),
'trastuzumab': (0, 1),
'letrozole': (0, 1),
'chemotherapy': (0, 1),
'hormone_therapy': (0, 1),
'no_treatment': (0, 1),
'methotrexate': (0, 1),
'cetuximab': (0, 1),
'carboplatin': (0, 1),
'other_treatment': (0, 1),
'metastasis_months_3': (1.0, 35.0),
'DFS_1': (0.0, 1.0),
'RFS_1': (0.0, 1.0),
'metastasis_1': (0.0, 1.0),
'metastasis_months_1': (10.0, 25.0),
'DFS_2': (0.0, 1.0),
'RFS_2': (0.0, 1.0),
'metastasis_2': (0.0, 1.0),
'metastasis_months_2': (10.0, 25.0),
'DFS_3': (0.0, 1.0),
'RFS_3': (0.0, 1.0),
'metastasis_3': (0.0, 1.0),
'clinical_AJCC_stage_I': (0, 1),
'clinical_AJCC_stage_II': (0, 1),
'clinical_AJCC_stage_IIA': (0, 1),
'clinical_AJCC_stage_IIB': (0, 1),
'clinical_AJCC_stage_III': (0, 1),
'clinical_AJCC_stage_IIIA': (0, 1),
'clinical_AJCC_stage_IIIB': (0, 1),
'clinical_AJCC_stage_IIIC': (0, 1),
'clinical_AJCC_stage_IV': (0, 1),
'preTrt_lymph_node_status_N0': (0, 1),
'preTrt_lymph_node_status_N1': (0, 1),
'preTrt_lymph_node_status_N2': (0, 1),
'preTrt_lymph_node_status_N3': (0, 1),
'preTrt_lymph_node_status_ND': (0, 1),
'preTrt_lymph_node_status_positive': (0, 1),
'postTrt_lymph_node_status_N0': (0, 1),
'postTrt_lymph_node_status_N1': (0, 1),
'postTrt_lymph_node_status_N1a': (0, 1),
'postTrt_lymph_node_status_N2': (0, 1),
'postTrt_lymph_node_status_N2a': (0, 1),
'postTrt_lymph_node_status_N3': (0, 1),
'postTrt_lymph_node_status_positive': (0, 1),
'tumor_stage_preTrt_T0': (0, 1),
'tumor_stage_preTrt_T1': (0, 1),
'tumor_stage_preTrt_T2': (0, 1),
'tumor_stage_preTrt_T3': (0, 1),
'tumor_stage_preTrt_T4': (0, 1),
'tumor_stage_postTrt_T0': (0, 1),
'tumor_stage_postTrt_T1': (0, 1),
'tumor_stage_postTrt_T1a': (0, 1),
'tumor_stage_postTrt_T1b': (0, 1),
'tumor_stage_postTrt_T1c': (0, 1),
'tumor_stage_postTrt_T1mic': (0, 1),
'tumor_stage_postTrt_T2': (0, 1),
'tumor_stage_postTrt_Tis': (0, 1),
'pam50_Basal': (0, 1),
'pam50_Claudin': (0, 1),
'pam50_Her2': (0, 1),
'pam50_Luminal A': (0, 1),
'pam50_Luminal B': (0, 1),
'pam50_Normal': (0, 1),
'pCR_spectrum_CR': (0, 1),
'pCR_spectrum_EPD': (0, 1),
'pCR_spectrum_NCR': (0, 1),
'pCR_spectrum_NE': (0, 1),
'pCR_spectrum_PD': (0, 1),
'pCR_spectrum_PR': (0, 1),
'pCR_spectrum_SD': (0, 1),
'RCB_0': (0, 1),
'RCB_0/I': (0, 1),
'RCB_1': (0, 1),
'RCB_2': (0, 1),
'RCB_3': (0, 1),
'RCB_II': (0, 1),
'RCB_III': (0, 1),
'race_asian': (0, 1),
'race_black': (0, 1),
'race_hispanic': (0, 1),
'race_mixed': (0, 1),
'race_white': (0, 1),
'menopausal_status_post': (0, 1),
'menopausal_status_pre': (0, 1),
'HER2_IHC_score_preTrt_0': (0, 1),
'HER2_IHC_score_preTrt_1': (0, 1),
'HER2_IHC_score_preTrt_2': (0, 1),
'HER2_IHC_score_preTrt_3': (0, 1),
'HER2_IHC_score_preTrt_ND': (0, 1),
'HER2_IHC_score_preTrt_NEG': (0, 1),
'ploidy_aneuploid': (0, 1),
'ploidy_diploid': (0, 1),
'ploidy_multiploid': (0, 1),
'surgery_breast preserving': (0, 1),
'surgery_mastectomy': (0, 1),
'neoadjuvant_or_adjuvant_adj': (0, 1),
'neoadjuvant_or_adjuvant_mixed': (0, 1),
'neoadjuvant_or_adjuvant_neo': (0, 1),
'neoadjuvant_or_adjuvant_unspecified': (0, 1),}


# columns to preprocess if the goal of the preprocessing is treatment
treats = [(H1), (H2), (H3)]

# columns for prediction
pred = [([A1], H1 + [A1]), ([A2], H2 + [A2]), ([A3], H3 + [A3])]

# columns to preprocess if the goal of the preprocessing is prediction
# def rescale(data, data_range, scale_range):
#     return ((data - data_range[0]) / (data_range[1] - data_range[0])) * (scale_range[1] - scale_range[0]) + scale_range[0]



def postprocess(data):
    if len(data.shape) < 2:
        data = pd.DataFrame([data], columns=data.index)
    data_cleaned = data.copy()
    
    columns = data.columns

    # rescaling to orig range
    # for c in columns:
    #     if c in feature_range.keys():
    #         data_cleaned[c] = rescale(data_cleaned[c], (-1, 1), feature_range[c])
    # return data_cleaned
    
    # # going back from numerical to categorical
    # data_cleaned.loc[data_cleaned['Aspiration rate Pre-therapy'] == 0, 'Aspiration rate Pre-therapy'] = 'N'
    # data_cleaned.loc[data_cleaned['Aspiration rate Pre-therapy'] == 1, 'Aspiration rate Pre-therapy'] = 'Y'




# OK
    # data_cleaned['clinical_AJCC_stage'] = 'NOS'
    new_data = pd.DataFrame({'clinical_AJCC_stage': 'NOS'}, index=data_cleaned.index)
    data_cleaned = pd.concat([data_cleaned, new_data], axis=1)
    data_cleaned.loc[data_cleaned['clinical_AJCC_stage_IIB'] == 1, 'clinical_AJCC_stage'] = 'IIB'
    data_cleaned.loc[data_cleaned['clinical_AJCC_stage_IIA'] == 1, 'clinical_AJCC_stage'] = 'IIA'
    data_cleaned.loc[data_cleaned['clinical_AJCC_stage_II'] == 1, 'clinical_AJCC_stage'] = 'II'
    data_cleaned.loc[data_cleaned['clinical_AJCC_stage_IIIA'] == 1, 'clinical_AJCC_stage'] = 'IIIA'
    data_cleaned.loc[data_cleaned['clinical_AJCC_stage_IIIB'] == 1, 'clinical_AJCC_stage'] = 'IIIB'
    data_cleaned.loc[data_cleaned['clinical_AJCC_stage_IIIC'] == 1, 'clinical_AJCC_stage'] = 'IIIC'
    data_cleaned.loc[data_cleaned['clinical_AJCC_stage_IV'] == 1, 'clinical_AJCC_stage'] = 'IV'
    data_cleaned.loc[data_cleaned['clinical_AJCC_stage_I'] == 1, 'clinical_AJCC_stage'] = 'I'
    data_cleaned.loc[data_cleaned['clinical_AJCC_stage_III'] == 1, 'clinical_AJCC_stage'] = 'III'
    data_cleaned = data_cleaned.drop(
        [ 'clinical_AJCC_stage_IIB', 'clinical_AJCC_stage_IIA','clinical_AJCC_stage_II' , 'clinical_AJCC_stage_IIIA' ,'clinical_AJCC_stage_IIIB', 'clinical_AJCC_stage_IIIC', 'clinical_AJCC_stage_I', 'clinical_AJCC_stage_III', 'clinical_AJCC_stage_IV'], axis=1)
    
    

# ok
    # data_cleaned['treatment_admin'] = 'NOS'
    new_data = pd.DataFrame({'treatment_admin': 'NOS'}, index=data_cleaned.index)
    data_cleaned = pd.concat([data_cleaned, new_data], axis=1)
    data_cleaned.loc[data_cleaned['intarvenous'] == 1, 'treatment_admin'] = 'intarvenous'
    data_cleaned.loc[data_cleaned['intramuscular'] == 1, 'treatment_admin'] = 'intramuscular'
    data_cleaned.loc[data_cleaned['oral'] == 1, 'treatment_admin'] = 'oral'
    data_cleaned = data_cleaned.drop(
        ['intarvenous', 'intramuscular', 'oral'], axis=1)


    # data_cleaned['Race'] = 'NOS'
    new_data = pd.DataFrame({'Race': 'NOS'}, index=data_cleaned.index)
    data_cleaned = pd.concat([data_cleaned, new_data], axis=1)
    data_cleaned.loc[data_cleaned['race_white'] == 1, 'Race'] = 'White'
    data_cleaned.loc[data_cleaned['race_hispanic'] == 1, 'Race'] = 'Hispanic'
    data_cleaned.loc[data_cleaned['race_black'] == 1, 'Race'] = 'Black'
    data_cleaned.loc[data_cleaned['race_asian'] == 1, 'Race'] = 'Asian'
    data_cleaned.loc[data_cleaned['race_mixed'] == 1, 'Race'] = 'Mixed'
    data_cleaned = data_cleaned.drop(
        ['race_white', 'race_hispanic', 'race_black', 'race_asian', 'race_mixed'], axis=1)


    # data_cleaned['preTrt_lymph_node_status'] = 'NOS'
    new_data = pd.DataFrame({'preTrt_lymph_node_status': 'NOS'}, index=data_cleaned.index)
    data_cleaned = pd.concat([data_cleaned, new_data], axis=1)
    data_cleaned.loc[data_cleaned['preTrt_lymph_node_status_N0'] == 1, 'preTrt_lymph_node_status'] = 'N0'
    data_cleaned.loc[data_cleaned['preTrt_lymph_node_status_N1'] == 1, 'preTrt_lymph_node_status'] = 'N1'
    data_cleaned.loc[data_cleaned['preTrt_lymph_node_status_N2'] == 1, 'preTrt_lymph_node_status'] = 'N2'
    data_cleaned.loc[data_cleaned['preTrt_lymph_node_status_N3'] == 1, 'preTrt_lymph_node_status'] = 'N3'
    data_cleaned.loc[data_cleaned['preTrt_lymph_node_status_ND'] == 1, 'preTrt_lymph_node_status'] = 'ND'
    data_cleaned.loc[data_cleaned['preTrt_lymph_node_status_positive'] == 1, 'preTrt_lymph_node_status'] = 'positive'
    data_cleaned = data_cleaned.drop(
        ['preTrt_lymph_node_status_N0', 'preTrt_lymph_node_status_N1', 'preTrt_lymph_node_status_N2', 'preTrt_lymph_node_status_N3', 'preTrt_lymph_node_status_ND', 'preTrt_lymph_node_status_positive'], axis=1)



    # data_cleaned['postTrt_lymph_node_status'] = 'NOS'
    new_data = pd.DataFrame({'postTrt_lymph_node_status': 'NOS'}, index=data_cleaned.index)
    data_cleaned = pd.concat([data_cleaned, new_data], axis=1)
    data_cleaned.loc[data_cleaned['postTrt_lymph_node_status_N0'] == 1, 'postTrt_lymph_node_status'] = 'N0'
    data_cleaned.loc[data_cleaned['postTrt_lymph_node_status_N1'] == 1, 'postTrt_lymph_node_status'] = 'N1'
    data_cleaned.loc[data_cleaned['postTrt_lymph_node_status_N1a'] == 1, 'postTrt_lymph_node_status'] = 'N1a'
    data_cleaned.loc[data_cleaned['postTrt_lymph_node_status_N2'] == 1, 'postTrt_lymph_node_status'] = 'N2'
    data_cleaned.loc[data_cleaned['postTrt_lymph_node_status_N2a'] == 1, 'postTrt_lymph_node_status'] = 'N2a'
    data_cleaned.loc[data_cleaned['postTrt_lymph_node_status_N3'] == 1, 'postTrt_lymph_node_status'] = 'N3'
    data_cleaned.loc[data_cleaned['postTrt_lymph_node_status_positive'] == 1, 'postTrt_lymph_node_status'] = 'positive'
    data_cleaned = data_cleaned.drop(
        ['postTrt_lymph_node_status_N0', 'postTrt_lymph_node_status_N1', 'postTrt_lymph_node_status_N1a', 'postTrt_lymph_node_status_N2', 'postTrt_lymph_node_status_N2a', 'postTrt_lymph_node_status_N3', 'postTrt_lymph_node_status_positive' ], axis=1)


    # data_cleaned['tumor_stage_postTrt'] = 'NOS'
    new_data = pd.DataFrame({'tumor_stage_postTrt': 'NOS'}, index=data_cleaned.index)
    data_cleaned = pd.concat([data_cleaned, new_data], axis=1)
    data_cleaned.loc[data_cleaned['tumor_stage_postTrt_T0'] == 1, 'tumor_stage_postTrt'] = 'T0'
    data_cleaned.loc[data_cleaned['tumor_stage_postTrt_T1'] == 1, 'tumor_stage_postTrt'] = 'T1'
    data_cleaned.loc[data_cleaned['tumor_stage_postTrt_T2'] == 1, 'tumor_stage_postTrt'] = 'T2'
    data_cleaned.loc[data_cleaned['tumor_stage_postTrt_T1a'] == 1, 'tumor_stage_postTrt'] = 'T1a'
    data_cleaned.loc[data_cleaned['tumor_stage_postTrt_T1b'] == 1, 'tumor_stage_postTrt'] = 'T1b'
    data_cleaned.loc[data_cleaned['tumor_stage_postTrt_T1c'] == 1, 'tumor_stage_postTrt'] = 'T1c'
    data_cleaned.loc[data_cleaned['tumor_stage_postTrt_T1mic'] == 1, 'tumor_stage_postTrt'] = 'T1mic'
    data_cleaned.loc[data_cleaned['tumor_stage_postTrt_Tis'] == 1, 'tumor_stage_postTrt'] = 'Tis'
    data_cleaned = data_cleaned.drop(
        ['tumor_stage_postTrt_T0', 'tumor_stage_postTrt_T1', 'tumor_stage_postTrt_T2', 'tumor_stage_postTrt_T1a', 'tumor_stage_postTrt_T1b', 'tumor_stage_postTrt_Tis', 'tumor_stage_postTrt_T1mic', 'tumor_stage_postTrt_T1c' ], axis=1)


    # data_cleaned['tumor_stage_preTrt'] = 'NOS'
    new_data = pd.DataFrame({'tumor_stage_preTrt': 'NOS'}, index=data_cleaned.index)
    data_cleaned = pd.concat([data_cleaned, new_data], axis=1)
    data_cleaned.loc[data_cleaned['tumor_stage_preTrt_T0'] == 1, 'tumor_stage_preTrt'] = 'T0'
    data_cleaned.loc[data_cleaned['tumor_stage_preTrt_T1'] == 1, 'tumor_stage_preTrt'] = 'T1'
    data_cleaned.loc[data_cleaned['tumor_stage_preTrt_T2'] == 1, 'tumor_stage_preTrt'] = 'T2'
    data_cleaned.loc[data_cleaned['tumor_stage_preTrt_T3'] == 1, 'tumor_stage_preTrt'] = 'T3'
    data_cleaned.loc[data_cleaned['tumor_stage_preTrt_T4'] == 1, 'tumor_stage_preTrt'] = 'T4'
    data_cleaned = data_cleaned.drop(
        ['tumor_stage_preTrt_T0', 'tumor_stage_preTrt_T1', 'tumor_stage_preTrt_T2', 'tumor_stage_preTrt_T3', 'tumor_stage_preTrt_T4'], axis=1)


    # data_cleaned['pam50'] = 'NOS'
    new_data = pd.DataFrame({'pam50': 'NOS'}, index=data_cleaned.index)
    data_cleaned = pd.concat([data_cleaned, new_data], axis=1)
    data_cleaned.loc[data_cleaned['pam50_Basal'] == 1, 'pam50'] = 'Basal'
    data_cleaned.loc[data_cleaned['pam50_Claudin'] == 1, 'pam50'] = 'Claudin'
    data_cleaned.loc[data_cleaned['pam50_Her2'] == 1, 'pam50'] = 'Her2'
    data_cleaned.loc[data_cleaned['pam50_Luminal A'] == 1, 'pam50'] = 'Luminal A'
    data_cleaned.loc[data_cleaned['pam50_Luminal B'] == 1, 'pam50'] = 'Luminal B'
    data_cleaned.loc[data_cleaned['pam50_Normal'] == 1, 'pam50'] = 'Normal'
    data_cleaned = data_cleaned.drop(
        ['pam50_Basal', 'pam50_Claudin', 'pam50_Her2', 'pam50_Luminal A', 'pam50_Luminal B', 'pam50_Normal'], axis=1)


    # data_cleaned['pCR_spectrum'] = 'NOS'
    new_data = pd.DataFrame({'pCR_spectrum': 'NOS'}, index=data_cleaned.index)
    data_cleaned = pd.concat([data_cleaned, new_data], axis=1)
    data_cleaned.loc[data_cleaned['pCR_spectrum_CR'] == 1, 'pCR_spectrum'] = 'CR'
    data_cleaned.loc[data_cleaned['pCR_spectrum_EPD'] == 1, 'pCR_spectrum'] = 'EPD'
    data_cleaned.loc[data_cleaned['pCR_spectrum_NCR'] == 1, 'pCR_spectrum'] = 'NCR'
    data_cleaned.loc[data_cleaned['pCR_spectrum_NE'] == 1, 'pCR_spectrum'] = 'NE'
    data_cleaned.loc[data_cleaned['pCR_spectrum_PD'] == 1, 'pCR_spectrum'] = 'PD'
    data_cleaned.loc[data_cleaned['pCR_spectrum_PR'] == 1, 'pCR_spectrum'] = 'PR'
    data_cleaned.loc[data_cleaned['pCR_spectrum_SD'] == 1, 'pCR_spectrum'] = 'SD'
    data_cleaned = data_cleaned.drop(
        ['pCR_spectrum_CR', 'pCR_spectrum_EPD', 'pCR_spectrum_NCR', 'pCR_spectrum_NE', 'pCR_spectrum_PD', 'pCR_spectrum_PR', 'pCR_spectrum_SD'], axis=1)


    # data_cleaned['RCB'] = 'NOS'
    new_data = pd.DataFrame({'RCB': 'NOS'}, index=data_cleaned.index)
    data_cleaned = pd.concat([data_cleaned, new_data], axis=1)
    data_cleaned.loc[data_cleaned['RCB_0'] == 1, 'RCB'] = '0'
    data_cleaned.loc[data_cleaned['RCB_1'] == 1, 'RCB'] = '1'
    data_cleaned.loc[data_cleaned['RCB_2'] == 1, 'RCB'] = '2'
    data_cleaned.loc[data_cleaned['RCB_3'] == 1, 'RCB'] = '3'
    data_cleaned.loc[data_cleaned['RCB_0/I'] == 1, 'RCB'] = '0/I'
    data_cleaned.loc[data_cleaned['RCB_II'] == 1, 'RCB'] = 'II'
    data_cleaned.loc[data_cleaned['RCB_III'] == 1, 'RCB'] = 'III'
    data_cleaned = data_cleaned.drop(
        ['RCB_0', 'RCB_1', 'RCB_2', 'RCB_3', 'RCB_0/I', 'RCB_II', 'RCB_III'], axis=1)


    # data_cleaned['menopausal_status'] = 'NOS'
    new_data = pd.DataFrame({'menopausal_status': 'NOS'}, index=data_cleaned.index)
    data_cleaned = pd.concat([data_cleaned, new_data], axis=1)
    data_cleaned.loc[data_cleaned['menopausal_status_post'] == 1, 'menopausal_status'] = 'post'
    data_cleaned.loc[data_cleaned['menopausal_status_pre'] == 1, 'menopausal_status'] = 'pre'
    data_cleaned = data_cleaned.drop(
        ['menopausal_status_post', 'menopausal_status_pre'], axis=1)


    # data_cleaned['HER2_IHC_score_preTrt'] = 'NOS'
    new_data = pd.DataFrame({'HER2_IHC_score_preTrt': 'NOS'}, index=data_cleaned.index)
    data_cleaned = pd.concat([data_cleaned, new_data], axis=1)
    data_cleaned.loc[data_cleaned['HER2_IHC_score_preTrt_0'] == 1, 'HER2_IHC_score_preTrt'] = '0'
    data_cleaned.loc[data_cleaned['HER2_IHC_score_preTrt_1'] == 1, 'HER2_IHC_score_preTrt'] = '1'
    data_cleaned.loc[data_cleaned['HER2_IHC_score_preTrt_2'] == 1, 'HER2_IHC_score_preTrt'] = '2'
    data_cleaned.loc[data_cleaned['HER2_IHC_score_preTrt_3'] == 1, 'HER2_IHC_score_preTrt'] = '3'
    data_cleaned.loc[data_cleaned['HER2_IHC_score_preTrt_ND'] == 1, 'HER2_IHC_score_preTrt'] = 'ND'
    data_cleaned.loc[data_cleaned['HER2_IHC_score_preTrt_NEG'] == 1, 'HER2_IHC_score_preTrt'] = 'NEG'
    data_cleaned = data_cleaned.drop(
        ['HER2_IHC_score_preTrt_0', 'HER2_IHC_score_preTrt_1', 'HER2_IHC_score_preTrt_2', 'HER2_IHC_score_preTrt_3', 'HER2_IHC_score_preTrt_ND', 'HER2_IHC_score_preTrt_NEG'], axis=1)


    # data_cleaned['ploidy'] = 'NOS'
    new_data = pd.DataFrame({'ploidy': 'NOS'}, index=data_cleaned.index)
    data_cleaned = pd.concat([data_cleaned, new_data], axis=1)
    data_cleaned.loc[data_cleaned['ploidy_aneuploid'] == 1, 'ploidy'] = 'aneuploid'
    data_cleaned.loc[data_cleaned['ploidy_diploid'] == 1, 'ploidy'] = 'diploid'
    data_cleaned.loc[data_cleaned['ploidy_multiploid'] == 1, 'ploidy'] = 'multiploid'
    data_cleaned = data_cleaned.drop(
        ['ploidy_aneuploid', 'ploidy_diploid', 'ploidy_multiploid'], axis=1)



    # data_cleaned['estrogen_receptor'] = 'NOS'
    new_data = pd.DataFrame({'estrogen_receptor': 'NOS'}, index=data_cleaned.index)
    data_cleaned = pd.concat([data_cleaned, new_data], axis=1)
    data_cleaned.loc[data_cleaned['estrogen_receptor_blocker_and_stops_production'] == 1, 'estrogen_receptor'] = 'block_and_stop'
    data_cleaned.loc[data_cleaned['estrogen_receptor_blocker_and_eliminator'] == 1, 'estrogen_receptor'] = 'block_and_eliminate'
    data_cleaned = data_cleaned.drop(
        ['estrogen_receptor_blocker_and_stops_production', 'estrogen_receptor_blocker_and_eliminator', 'estrogen_receptor_blocker'], axis=1)



    # data_cleaned['surgery'] = 'NOS'
    new_data = pd.DataFrame({'surgery': 'NOS'}, index=data_cleaned.index)
    data_cleaned = pd.concat([data_cleaned, new_data], axis=1)
    data_cleaned.loc[data_cleaned['surgery_breast preserving'] == 1, 'surgery'] = 'preserving'
    data_cleaned.loc[data_cleaned['surgery_mastectomy'] == 1, 'surgery'] = 'mastectomy'
    data_cleaned = data_cleaned.drop(
        ['surgery_breast preserving', 'surgery_mastectomy'], axis=1)


    # data_cleaned['therapy'] = 'NOS'
    new_data = pd.DataFrame({'therapy': 'NOS'}, index=data_cleaned.index)
    data_cleaned = pd.concat([data_cleaned, new_data], axis=1)
    data_cleaned.loc[data_cleaned['neoadjuvant_or_adjuvant_adj'] == 1, 'therapy'] = 'adj'
    data_cleaned.loc[data_cleaned['neoadjuvant_or_adjuvant_mixed'] == 1, 'therapy'] = 'mixed'
    data_cleaned.loc[data_cleaned['neoadjuvant_or_adjuvant_neo'] == 1, 'therapy'] = 'neo'
    data_cleaned.loc[data_cleaned['neoadjuvant_or_adjuvant_unspecified'] == 1, 'therapy'] = 'unspecified'
    data_cleaned = data_cleaned.drop(
        ['neoadjuvant_or_adjuvant_adj', 'neoadjuvant_or_adjuvant_mixed', 'neoadjuvant_or_adjuvant_neo', 'neoadjuvant_or_adjuvant_unspecified'], axis=1)
    
    
#     # data_cleaned['menopausal_status'] = 'NOS'
#     new_data = pd.DataFrame({'menopausal_status': 'NOS'}, index=data_cleaned.index)
#     data_cleaned = pd.concat([data_cleaned, new_data], axis=1)
#     data_cleaned.loc[data_cleaned['menopausal_status_pre'] == 1, 'menopausal_status'] = 'pre'
#     data_cleaned.loc[data_cleaned['menopausal_status_post'] == 1, 'menopausal_status'] = 'post'
#     data_cleaned = data_cleaned.drop(
#         ['menopausal_status_pre', 'menopausal_status_post'], axis=1)
# # ok


    if 'surgery' in columns:
        data_cleaned.loc[data_cleaned['surgery'] == 0, 'surgery'] = 'N'
        data_cleaned.loc[data_cleaned['surgery'] == 1, 'surgery'] = 'Y'

    if 'chemotherapy' in columns:
        data_cleaned.loc[data_cleaned['chemotherapy'] == 0, 'chemotherapy'] = 'N'
        data_cleaned.loc[data_cleaned['chemotherapy'] == 1, 'chemotherapy'] = 'Y'

    if 'hormone_therapy' in columns:
        data_cleaned.loc[data_cleaned['hormone_therapy'] == 0, 'hormone_therapy'] = 'N'
        data_cleaned.loc[data_cleaned['hormone_therapy'] == 1, 'hormone_therapy'] = 'Y'

    if 'radiotherapy' in columns:
        data_cleaned.loc[data_cleaned[
                             'radiotherapy'] == 0, 'radiotherapy'] = 'N'
        data_cleaned.loc[data_cleaned[
                             'radiotherapy'] == 1, 'radiotherapy'] = 'Y'  

    if 'no_treatment' in columns:
        data_cleaned.loc[data_cleaned['no_treatment'] == 0, 'no_treatment'] = 'N'
        data_cleaned.loc[data_cleaned['no_treatment'] == 1, 'no_treatment'] = 'Y'
        
    if 'other_treatment' in columns:
        data_cleaned.loc[data_cleaned['other_treatment'] == 0, 'other_treatment'] = 'N'
        data_cleaned.loc[data_cleaned['other_treatment'] == 1, 'other_treatment'] = 'Y'

# //// ok
    if 'metastasis' in columns:
        data_cleaned.loc[data_cleaned['metastasis'] == 0, 'metastasis'] = 'N'
        data_cleaned.loc[data_cleaned['metastasis'] == 1, 'metastasis'] = 'Y'

    if 'anthracycline' in columns:
        data_cleaned.loc[data_cleaned['anthracycline'] == 0, 'anthracycline'] = 'N'
        data_cleaned.loc[data_cleaned['anthracycline'] == 1, 'anthracycline'] = 'Y'

    if 'taxane' in columns:
        data_cleaned.loc[data_cleaned['taxane'] == 0, 'taxane'] = 'N'
        data_cleaned.loc[data_cleaned['taxane'] == 1, 'taxane'] = 'Y'
        
    if 'anti_estrogen' in columns:
        data_cleaned.loc[data_cleaned['anti_estrogen'] == 0, 'anti_estrogen'] = 'N'
        data_cleaned.loc[data_cleaned['anti_estrogen'] == 1, 'anti_estrogen'] = 'Y'

    if 'aromatase_inhibitor' in columns:
        data_cleaned.loc[data_cleaned['aromatase_inhibitor'] == 0, 'aromatase_inhibitor'] = 'N'
        data_cleaned.loc[data_cleaned['aromatase_inhibitor'] == 1, 'aromatase_inhibitor'] = 'Y'

    if 'anti_HER2' in columns:
        data_cleaned.loc[data_cleaned['anti_HER2'] == 0, 'anti_HER2'] = 'N'
        data_cleaned.loc[data_cleaned['anti_HER2'] == 1, 'anti_HER2'] = 'Y'
        
    if 'doxorubicin' in columns:
        data_cleaned.loc[data_cleaned['doxorubicin'] == 0, 'doxorubicin'] = 'N'
        data_cleaned.loc[data_cleaned['doxorubicin'] == 1, 'doxorubicin'] = 'Y'
        
    if 'epirubicin' in columns:
        data_cleaned.loc[data_cleaned['epirubicin'] == 0, 'epirubicin'] = 'N'
        data_cleaned.loc[data_cleaned['epirubicin'] == 1, 'epirubicin'] = 'Y'

    if 'docetaxel' in columns:
        data_cleaned.loc[data_cleaned['docetaxel'] == 0, 'docetaxel'] = 'N'
        data_cleaned.loc[data_cleaned['docetaxel'] == 1, 'docetaxel'] = 'Y'
        
    if 'capecitabine' in columns:
        data_cleaned.loc[data_cleaned['capecitabine'] == 0, 'capecitabine'] = 'N'
        data_cleaned.loc[data_cleaned['capecitabine'] == 1, 'capecitabine'] = 'Y'
        
    if 'fluorouracil' in columns:
        data_cleaned.loc[data_cleaned['fluorouracil'] == 0, 'fluorouracil'] = 'N'
        data_cleaned.loc[data_cleaned['fluorouracil'] == 1, 'fluorouracil'] = 'Y'
        
    if 'paclitaxel' in columns:
        data_cleaned.loc[data_cleaned['paclitaxel'] == 0, 'paclitaxel'] = 'N'
        data_cleaned.loc[data_cleaned['paclitaxel'] == 1, 'paclitaxel'] = 'Y'
        
    if 'cyclophosphamide' in columns:
        data_cleaned.loc[data_cleaned['cyclophosphamide'] == 0, 'cyclophosphamide'] = 'N'
        data_cleaned.loc[data_cleaned['cyclophosphamide'] == 1, 'cyclophosphamide'] = 'Y'
        
    if 'anastrozole' in columns:
        data_cleaned.loc[data_cleaned['anastrozole'] == 0, 'anastrozole'] = 'N'
        data_cleaned.loc[data_cleaned['anastrozole'] == 1, 'anastrozole'] = 'Y'
      
    if 'fulvestrant' in columns:
        data_cleaned.loc[data_cleaned['fulvestrant'] == 0, 'fulvestrant'] = 'N'
        data_cleaned.loc[data_cleaned['fulvestrant'] == 1, 'fulvestrant'] = 'Y'

    if 'gefitinib' in columns:
        data_cleaned.loc[data_cleaned['gefitinib'] == 0, 'gefitinib'] = 'N'
        data_cleaned.loc[data_cleaned['gefitinib'] == 1, 'gefitinib'] = 'Y'

    if 'trastuzumab' in columns:
        data_cleaned.loc[data_cleaned['trastuzumab'] == 0, 'trastuzumab'] = 'N'
        data_cleaned.loc[data_cleaned['trastuzumab'] == 1, 'trastuzumab'] = 'Y'
        
    if 'letrozole' in columns:
        data_cleaned.loc[data_cleaned['letrozole'] == 0, 'letrozole'] = 'N'
        data_cleaned.loc[data_cleaned['letrozole'] == 1, 'letrozole'] = 'Y'
    
    if 'methotrexate' in columns:
        data_cleaned.loc[data_cleaned['methotrexate'] == 0, 'methotrexate'] = 'N'
        data_cleaned.loc[data_cleaned['methotrexate'] == 1, 'methotrexate'] = 'Y'
    
    if 'cetuximab' in columns:
        data_cleaned.loc[data_cleaned['cetuximab'] == 0, 'cetuximab'] = 'N'
        data_cleaned.loc[data_cleaned['cetuximab'] == 1, 'cetuximab'] = 'Y'
    
    if 'carboplatin' in columns:
        data_cleaned.loc[data_cleaned['carboplatin'] == 0, 'carboplatin'] = 'N'
        data_cleaned.loc[data_cleaned['carboplatin'] == 1, 'carboplatin'] = 'Y'
    
    if 'biopsy_preTreat' in columns:
        data_cleaned.loc[data_cleaned['biopsy_preTreat'] == 0, 'biopsy_preTreat'] = 'N'
        data_cleaned.loc[data_cleaned['biopsy_preTreat'] == 1, 'biopsy_preTreat'] = 'Y'
    
    if 'pCR' in columns:
        data_cleaned.loc[data_cleaned['pCR'] == 0, 'pCR'] = 'N'
        data_cleaned.loc[data_cleaned['pCR'] == 1, 'pCR'] = 'Y'
    
    if 'near_pCR' in columns:
        data_cleaned.loc[data_cleaned['near_pCR'] == 0, 'near_pCR'] = 'N'
        data_cleaned.loc[data_cleaned['near_pCR'] == 1, 'near_pCR'] = 'Y'
        
    if 'died_from_cancer_if_dead' in columns:
        data_cleaned.loc[data_cleaned['died_from_cancer_if_dead'] == 0, 'died_from_cancer_if_dead'] = 'N'
        data_cleaned.loc[data_cleaned['died_from_cancer_if_dead'] == 1, 'died_from_cancer_if_dead'] = 'Y'
    
    if 'ER_preTrt' in columns:
        data_cleaned.loc[data_cleaned['ER_preTrt'] == 0, 'ER_preTrt'] = 'N'
        data_cleaned.loc[data_cleaned['ER_preTrt'] == 1, 'ER_preTrt'] = 'Y'
        
    if 'ESR1_preTrt' in columns:
        data_cleaned.loc[data_cleaned['ESR1_preTrt'] == 0, 'ESR1_preTrt'] = 'N'
        data_cleaned.loc[data_cleaned['ESR1_preTrt'] == 1, 'ESR1_preTrt'] = 'Y'
        
    if 'ERbb2_preTrt' in columns:
        data_cleaned.loc[data_cleaned['ERbb2_preTrt'] == 0, 'ERbb2_preTrt'] = 'N'
        data_cleaned.loc[data_cleaned['ERbb2_preTrt'] == 1, 'ERbb2_preTrt'] = 'Y'
        
    if 'Erbeta_preTrt' in columns:
        data_cleaned.loc[data_cleaned['Erbeta_preTrt'] == 0, 'Erbeta_preTrt'] = 'N'
        data_cleaned.loc[data_cleaned['Erbeta_preTrt'] == 1, 'Erbeta_preTrt'] = 'Y'
        
    if 'ERBB2_CPN_amplified' in columns:
        data_cleaned.loc[data_cleaned['ERBB2_CPN_amplified'] == 0, 'ERBB2_CPN_amplified'] = 'N'
        data_cleaned.loc[data_cleaned['ERBB2_CPN_amplified'] == 1, 'ERBB2_CPN_amplified'] = 'Y'
        
    if 'PR_preTrt' in columns:
        data_cleaned.loc[data_cleaned['PR_preTrt'] == 0, 'PR_preTrt'] = 'N'
        data_cleaned.loc[data_cleaned['PR_preTrt'] == 1, 'PR_preTrt'] = 'Y'
        
    if 'HER2_preTrt' in columns:
        data_cleaned.loc[data_cleaned['HER2_preTrt'] == 0, 'HER2_preTrt'] = 'N'
        data_cleaned.loc[data_cleaned['HER2_preTrt'] == 1, 'HER2_preTrt'] = 'Y'
        
    if 'cytokeratin5_pos' in columns:
        data_cleaned.loc[data_cleaned['cytokeratin5_pos'] == 0, 'cytokeratin5_pos'] = 'N'
        data_cleaned.loc[data_cleaned['cytokeratin5_pos'] == 1, 'cytokeratin5_pos'] = 'Y'


    return data_cleaned


data = pd.read_csv('processed_data.csv')
data_cleaned = postprocess(data)

data_cleaned.to_csv('dataset.csv', index=False)
