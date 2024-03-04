# H1= Pre-Treatment Data
# S= Treatment data
# A= Action/Decision/Treament Choice
# Y= Outcome


H1 = ['biopsy_preTreat', 'tumor_size_cm_preTrt_preSurgery', 'tumor_size_cm_secondAxis_preTrt_preSurgery', 'preTrt_lymph_node_status', 'preTrt_totalLymphNodes', 'preTrt_numPosLymphNodes', 'preTrt_numPosLymphNodesRemoved', 'tumor_stage_preTrt', 'nuclear_grade_preTrt', 'ER_preTrt', 'PR_preTrt', 'HER2_preTrt', 'age', 'race', 'menopausal_status', 'pam50', 'hist_grade', 'cytokeratin5_pos', 'ploidy', 'top2atri_preTrt', 'topoihc_preTrt', 'S_phase', 'DNA_index', 'menopausal_status', 'Clinical AJCC Stage', 'biopsy_postTrt_days'
]

A1 = 'surgery'
S2 = ['tumor_size_cm_postTrt',  'postTrt_numPosLymphNodes', 'RCB', 'metastasis', 'metastasis_months', 'RFS', 'DFS']

H2 = H1 + [A1] + S2

A2 = 'chemotherapy'
S3 =  ['anthracycline', 'taxane', 'other',
   'tumor_size_cm_postTrt',  'postTrt_numPosLymphNodes', 'RFS', 'DFS',
'doxorubicin', 'epirubicin', 'docetaxel', 'capecitabine', 'fluorouracil', 'paclitaxel', 'cyclophosphamide', 'methotrexate', 'carboplatin', 'near_pCR', 'pCR', 'metastasis', 'metastasis_months' ]

H3 = H2 + [A2] + S3

A3 = 'hormone_therapy'
S4 = ['anti_estrogen', 'aromatase_inhibitor', 'estrogen_receptor_blocker', 'estrogen_receptor_blocker_and_stops_production', 'estrogen_receptor_blocker_and_eliminator', 'anti_HER2', 'tamoxifen', 'letrozole', 'tumor_size_cm_postTrt', 'postTrt_numPosLymphNodes', 'RFS', 'DFS', 'cetuximab', 'gefitinib', 'trastuzumab', 'fulvestrant',  'anastrozole' ]

H4 = H3 + [A3] + S4

A4 = 'radiotherapy'
S5 = ['tumor_size_cm_postTrt', 'postTrt_numPosLymphNodes', 'RFS', 'DFS']

H5 = H4 + [A4] + S5

A5 = 'no_treatment'
S6 = ['tumor_size_cm_postTrt', 'RFS', 'DFS']
    
Y = ['died_from_cancer_if_dead']

decisions = [A1, A2, A3, A4, A5]
histories = [H1, H2, H3, H4, H5 ]
states = [S2, S3, S4, S5, S6, Y]

action_values = [(-1, 1), (-1, 1), (-1, 1)]





# #  need

# RFS_S - 0,1
# DFS_S - 0,1
# postTrt_numPosLymphNodes_C - 0,17
# postTrt_numPosLymphNodes_R - 0,17
# postTrt_numPosLymphNodes_H - 0,17