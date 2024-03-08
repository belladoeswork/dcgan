# H1= Pre-Treatment Data
# S= Treatment data
# A= Action/Decision/Treament Choice
# Y= Outcome


'biopsy_preTreat', 'tumor_size_cm_preTrt_preSurgery', 'tumor_size_cm_secondAxis_preTrt_preSurgery', 'preTrt_lymph_node_status', 'preTrt_totalLymphNodes', 'preTrt_numPosLymphNodes', 'preTrt_numPosLymphNodesRemoved', 'preTrt_posDichLymphNodes', 'tumor_stage_preTrt', 'nuclear_grade_preTrt', 'ER_preTrt', 'PR_preTrt', 'HER2_preTrt', 'ER_fmolmg_preTrt', 'Erbeta_preTrt', 'ESR1_preTrt', 'ERbb2_preTrt', 'ERBB2_CPN_amplified', 'PR_percentage_preTrt', 'PR_fmolmg_preTrt', 'HER2_IHC_score_preTrt', 'age', 'race', 'menopausal_status', 'HER2_fish_cont_score_preTrt', 'pam50', 'hist_grade', 'cytokeratin5_pos', 'ploidy', 'S_phase', 'DNA_index', 'menopausal_status', 'Clinical AJCC Stage', 'top2atri_preTrt', 'topoihc_preTrt', 'surgery', 'tumor_stage_postTrt', 'tumor_size_cm_postTrt', 'postTrt_numPosLymphNodes', 'postTrt_lymph_node_status', 'postTrt_totalLymphNodes', 'postTrt_numPosLymphNodes', 'RCB', 'other_treatment', 'metastasis', 'metastasis_months', 'RFS', 'DFS', 'chemotherapy', 'anthracycline', 'taxane', 'doxorubicin', 'epirubicin', 'docetaxel', 'capecitabine', 'fluorouracil', 'paclitaxel', 'cyclophosphamide', 'methotrexate', 'carboplatin', 'near_pCR', 'pCR', 'cetuximab', 'gefitinib', 'tamoxifen', 'aromatase_inhibitor', 'fulvestrant', 'anastrozole', 'letrozole', 'anti_estrogen', 'estrogen_receptor_blocker', 'estrogen_receptor_blocker_and_stops_production', 'estrogen_receptor_blocker_and_eliminator', 'anti_HER2', 'radiotherapy', 'trastuzumab', 'no_treatment', 'OS', 'died_from_cancer_if_dead'





H1 = ['biopsy_preTreat', 
      'tumor_size_cm_preTrt_preSurgery', 'tumor_size_cm_secondAxis_preTrt_preSurgery', 
      'preTrt_lymph_node_status', 'preTrt_totalLymphNodes', 'preTrt_numPosLymphNodes', 'preTrt_posDichLymphNodes', 'tumor_stage_preTrt', 'nuclear_grade_preTrt', 'ER_preTrt', 'PR_preTrt', 'HER2_preTrt', 'ER_fmolmg_preTrt', 'Erbeta_preTrt', 'ESR1_preTrt', 'ERbb2_preTrt',  'ERBB2_CPN_amplified', 'PR_percentage_preTrt', 'PR_fmolmg_preTrt', 'HER2_IHC_score_preTrt',
      'age', 'Race', 'menopausal_status', 'HER2_fish_cont_score_preTrt',
      'pam50', 'hist_grade', 'cytokeratin5_pos', 'ploidy', 'S_phase', 'top2atri_preTrt', 'topoihc_preTrt'
]

A1 = 'surgery'
S2 = ['tumor_stage_postTrt', 'tumor_size_cm_postTrt',  'postTrt_numPosLymphNodes',  'postTrt_lymph_node_status', 'postTrt_totalLymphNodes', 'RCB', 'other_treatment', 'metastasis', 'metastasis_months', 'RFS', 'DFS']


H2 = H1 + [A1] + S2

A2 = 'chemotherapy'
S3 =  ['anthracycline', 'taxane', 'RFS', 'DFS',
'doxorubicin', 'epirubicin', 'docetaxel', 'capecitabine', 'fluorouracil', 'paclitaxel', 'cyclophosphamide', 'methotrexate', 'carboplatin', 'near_pCR', 'pCR', 'metastasis', 'metastasis_months', 'cetuximab', 'gefitinib', 'other_treatment' ]


H3 = H2 + [A2] + S3

A3 = 'hormone_therapy'
S4 = ['tamoxifen', 'aromatase_inhibitor',  'fulvestrant', 'anastrozole','letrozole', 'anti_estrogen', 
      'estrogen_receptor_blocker', 'estrogen_receptor_blocker_and_stops_production', 'estrogen_receptor_blocker_and_eliminator', 'anti_HER2', 'other_treatment', 'metastasis', 'metastasis_months', 'RFS', 'DFS'
    ]

H4 = H3 + [A3] + S4

A4 = 'radiotherapy'
S5 = ['trastuzumab', 'metastasis', 'metastasis_months', 'other_treatment', 'RFS', 'DFS']
    

H5 = H4 + [A4] + S5

A5 = 'no_treatment'
# S6 = ['tumor_size_cm_postTrt', 'RFS', 'DFS']
    
Y = [ 'OS','died_from_cancer_if_dead']

decisions = [A1, A2, A3, A4, A5]
histories = [H1, H2, H3, H4, H5 ]
states = [S2, S3, S4, S5, Y]

action_values = [(-1, 1), (-1, 1), (-1, 1)]





# #  need

# RFS_S - 0,1
# DFS_S - 0,1
# postTrt_numPosLymphNodes_C - 0,17
# postTrt_numPosLymphNodes_R - 0,17
# postTrt_numPosLymphNodes_H - 0,17