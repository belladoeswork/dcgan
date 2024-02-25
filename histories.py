H1 = ['age',
      'ERBB2_CPN_amplified',
      'race',
      'menopausal_status', 

      
      'tumor_stage_preTrt', 'nuclear_grade_preTrt', 'metastasis_stage_preTrt', 'ER_preTrt', 'ER_percentage_preTrt', 'ER_expr_preTrt', 'ER_fmolmg_preTrt', 'ESR1_preTrt', 'ERbb2_preTrt', 'Erbeta_preTrt', 'PR_preTrt', 'PR_percentage_preTrt', 'PR_expr_preTrt', 'PR_fmolmg_preTrt', 'HER2_preTrt', 'HER2_IHC_score_preTrt', 'HER2_expr_preTrt', 'HER2_fish_cont_score_preTrt', 'top2atri_preTrt', 'topoihc_preTrt',
      
      
      'tumor_size_cm_preTrt_preSurgery', 'tumor_size_cm_secondAxis_preTrt_preSurgery'
      
      
      
      
      'preTrt_lymph_node_status', 'preTrt_totalLymphNodes', 'preTrt_numPosLymphNodes', 'preTrt_numPosLymphNodesRemoved', 'preTrt_posDichLymphNodes'
      
      
      ['tumor_size_cm_preTrt_preSurgery', 'tumor_size_cm_secondAxis_preTrt_preSurgery', 'tumor_size_cm_preTrt_preSurgeryMin', 'preTrt_lymph_node_status', 'preTrt_totalLymphNodes', 'preTrt_numPosLymphNodes', 'preTrt_numPosLymphNodesRemoved', 'preTrt_posDichLymphNodes', 'tumor_stage_preTrt', 'tumor_stage_preTrtMin', 'tumor_stage_preTrtMax', 'nuclear_grade_preTrt', 'metastasis_stage_preTrt', 'ER_preTrt', 'ER_percentage_preTrt', 'ER_expr_preTrt', 'ER_fmolmg_preTrt', 'ESR1_preTrt', 'ERbb2_preTrt', 'Erbeta_preTrt', 'PR_preTrt', 'PR_percentage_preTrt', 'PR_expr_preTrt', 'PR_fmolmg_preTrt', 'HER2_preTrt', 'HER2_IHC_score_preTrt', 'HER2_expr_preTrt', 'HER2_fish_cont_score_preTrt', 'top2atri_preTrt', 'topoihc_preTrt']
      
      'HPV/P16 status',
      'T-category',
      'N-category',
      'N-category_8th_edition',
      'AJCC 7th edition',
      'AJCC 8th edition',
      'Smoking status at Diagnosis (Never/Former/Current)',
      'Smoking status (Packs/Year)',
      'Aspiration rate Pre-therapy',
      'Num Affected Lymph nodes',
      'R Laterality',
      'L Laterality',
      'BOT subsite',
      'Tonsil subsite',
      'Soft Palate subsite',
      'GPS subsite',
      'White/Caucasian',
      'Hispanic/Latino',
      'African American/Black',
      'Asian',
      'Native American']

A1 = 'Decision 1 (surgery) Y/N'
S2 = ['surgery_type (breast preserving/mastectomy )',
                'Chemo Modification (Y/N)',
                'Dose modified',
                'Dose delayed',
                'Dose cancelled',
                'Regimen modification',
                'DLT (Y/N)',
                'DLT_Dermatological',
                'DLT_Neurological',
                'DLT_Gastrointestinal',
                'DLT_Hematological',
                'DLT_Nephrological',
                'DLT_Vascular',
                'DLT_Infection (Pneumonia)',
                'DLT_Other',
                'DLT_Grade',
                'No imaging (0=N, 1=Y)',
                'CR Primary',
                'CR Nodal',
                'PR Primary',
                'PR Nodal',
                'SD Primary',
                'SD Nodal']
H2 = H1 + [A1] + S2
A2 = 'Decision 2 (CC / RT alone)'
S3 =  ['CC Platinum',
                'CC Cetuximab',
                'CC Others',
                'CC modification (Y/N)',
                'CR Primary 2',
                'CR Nodal 2',
                'PR Primary 2',
                'PR Nodal 2',
                'SD Primary 2',
                'SD Nodal 2',
                'DLT_Dermatological 2',
                'DLT_Neurological 2',
                'DLT_Gastrointestinal 2',
                'DLT_Hematological 2',
                'DLT_Nephrological 2',
                'DLT_Vascular 2',
                'DLT_Other 2']
H3 = H2 + [A2] + S3
A3 = 'Decision 3 Neck Dissection (Y/N)'
Y = ['Overall Survival (4 Years)', 'Feeding tube 6m', 'Aspiration rate Post-therapy', 'Dysphagia']

Y: "RFS","Relapse-Free Survival. NOTE: in keeping with 1 as a ""healthy"" status (like pCR) in this database, 1=did NOT relapse (survived/was healthy), and 0=relapsed."
"RFS_months_or_MIN_months_of_RFS","Months until RFS or minimum months of RFS (in the case that a clinical trial only stated the minimum number of RFS months for all patients)"
"DFS","Disease-Free Survival. NOTE: in keeping with 1 as a ""healthy"" status (like pCR) in this database, 1=did NOT have disease (survived/was healthy), and 0= did have disease."
"DFS_months_or_MIN_months_of_DFS","Months until DFS or minimum months of DFS (in the case that a clinical trial only stated the minimum number of DFS months for all patients)"
"OS","Overall Survival (was the patient alive at the end of the trial?) NOTE: in keeping with 1 as a ""healthy"" status (like pCR) in this database, 1=did survive (survived/was healthy), and 0=did NOT survive."
"OS_months_or_MIN_months_of_OS","Months of OS or minimum months of OS (in the case that a clinical trial only stated the minimum number of OS months for all patients)"
"OS_up_until_death","Was the OS variable measured up until a patients' death? 1=YES. 0=NO. 0 indicates that perhaps the trial only followed patients for say 5 or 10 years (see OS_months_or_MIN_months_of_OS for patients in a certain clinical trial to see the maximum length of time a certain trial followed a patient.)"



decisions = [A1, A2, A3]
histories = [H1, H2, H3]
states = [S2, S3, Y]
action_values = [(-1, 1), (-1, 1), (-1, 1)]

# histories before preprocessing
H1_prepr = ['age',
            'nuclear_grade_preTrt',
            'metastasis_stage_preTrt',
            
            'HPV/P16 status',
            'T-category',
            'N-category',
            'N-category_8th_edition',
            'AJCC 7th edition',
            'AJCC 8th edition',
            'Smoking status at Diagnosis (Never/Former/Current)',
            'Smoking status (Packs/Year)',
            'Aspiration rate Pre-therapy',
            'Affected Lymph node',
            'Tm Laterality (R/L)',
            'Tumor subsite (BOT/Tonsil/Soft Palate/Pharyngeal wall/GPS/NOS)',
            'Race']
S2_prepr = ['Prescribed Chemo (Single/doublet/triplet/quadruplet/none/NOS)',
                'Chemo Modification (Y/N)',
                'Modification Type (0= no dose adjustment, 1=dose modified, 2=dose delayed, 3=dose cancelled, 4=dose delayed & modified, 5=regimen modification, 9=unknown)',
                'DLT (Y/N)',
                'DLT_Type',
                'DLT_Dermatological',
                'DLT_Neurological',
                'DLT_Gastrointestinal',
                'DLT_Hematological',
                'DLT_Nephrological',
                'DLT_Vascular',
                'DLT_Infection (Pneumonia)',
                'DLT_Grade',
                'No imaging (0=N, 1=Y)',
                'CR Primary',
                'CR Nodal',
                'PR Primary',
                'PR Nodal',
                'SD Primary',
                'SD Nodal']
H2_prepr = H1_prepr + [A1] + S2_prepr
S3_prepr =  ['CC Regimen(0= none, 1= platinum based, 2= cetuximab based, 3= others, 9=unknown)',
                'CC modification (Y/N)',
                'CR Primary 2',
                'CR Nodal 2',
                'PR Primary 2',
                'PR Nodal 2',
                'SD Primary 2',
                'SD Nodal 2',
                'DLT 2']
H3_prepr = H2_prepr + [A2] + S3_prepr


#surgery data breast preserving / mastectomy
'methotrexate',



'tumor_size_cm_preTrt_preSurgery', 'tumor_size_cm_secondAxis_preTrt_preSurgery', 'tumor_size_cm_preTrt_preSurgeryMin',
'months_from_surgery_measured_RCB', 'surgery_type'

#preTrt data
'biopsy_preTreat'
'tumor_size_cm_preTrt_preSurgery', 'tumor_size_cm_secondAxis_preTrt_preSurgery', 'tumor_size_cm_preTrt_preSurgeryMin', 'preTrt_lymph_node_status', 'preTrt_totalLymphNodes', 'preTrt_numPosLymphNodes', 'preTrt_numPosLymphNodesRemoved', 'preTrt_posDichLymphNodes', 'tumor_stage_preTrt', 'tumor_stage_preTrtMin', 'tumor_stage_preTrtMax', 'nuclear_grade_preTrt', 'metastasis_stage_preTrt', 'ER_preTrt', 'ER_percentage_preTrt', 'ER_expr_preTrt', 'ER_fmolmg_preTrt', 'ESR1_preTrt', 'ERbb2_preTrt', 'Erbeta_preTrt', 'PR_preTrt', 'PR_percentage_preTrt', 'PR_expr_preTrt', 'PR_fmolmg_preTrt', 'HER2_preTrt', 'HER2_IHC_score_preTrt', 'HER2_expr_preTrt', 'HER2_fish_cont_score_preTrt', 'top2atri_preTrt', 'topoihc_preTrt'

#postTrt data
'biopsy_postTrt_days', 'pCR_postTrt_days', 'tumor_size_cm_postTrt', 'postTrt_lymph_node_status', 'postTrt_totalLymphNodes', 'postTrt_numPosLymphNodes', 'tumor_stage_postTrt'

#pCR - Pathological complete response
'pCR_postTrt_days', 'pCR', 'near_pCR', 'pCR_spectrum'

#RCB - Residual Cancer Burden
'RCB'

#RFS - Relapse-Free Survival
'RFS'
 
#DFS - Disease-Free Survival
'DFS'

#OS - Overall Survival
'OS'

#ER - Estrogen Receptor
'ER_preTrt', 'ER_percentage_preTrt', 'ER_fmolmg_preTrt', 'estrogen_receptor_blocker_and_stops_production', 'estrogen_receptor_blocker_and_eliminator', 'estrogen_receptor_blocker_and_stops_production',
'estrogen_receptor_blocker'


#ERBB2 - Erb-B2 Receptor Tyrosine Kinase 2
'ERbb2_preTrt', 'ERBB2_CPN_amplified'

#PR - Progesterone Receptor
'PR_preTrt', 'PR_percentage_preTrt', 'PR_expr_preTrt', 'PR_fmolmg_preTrt'
 
#HER2 - Human Epidermal Growth Factor Receptor 2
'HER2_preTrt', 'HER2_IHC_score_preTrt', 'HER2_fish_cont_score_preTrt', 'anti_HER2'


#ESR1 - Estrogen Receptor 1
'ESR1_preTrt'

#Erbeta - Estrogen Receptor Beta
'Erbeta_preTrt'

#top2atri - Topoisomerase II Alpha
'top2atri_preTrt', 

#topoihc - Topoisomerase IHC
'topoihc_preTrt'

#AJCC - American Joint Committee on Cancer
'clinical_AJCC_stage'
 
#metastasis - Did the tumor metastasize?
'metastasis', 'metastasis_months'

#dead - Did the patient die?
'dead', 'died_from_cancer_if_dead'

#biopsy - Did the patient have a biopsy?
'biopsy_preTreat'

#treatments
'neoadjuvant_or_adjuvant'
- this seems to be surgery
neo=before the main ttt
adj=after the main ttt

#stand alone ttt
'gefitinib'
'fulvestrant'

# pre surgery ttt
'docetaxel'
'epirubicin'
'aromatase_inhibitor'
'anti_estrogen'
'anthracycline'

#after surgery ttt
'anastrozole'
'capecitabine'
'docetaxel'
'epirubicin'
'tamoxifen'
'estrogen_receptor_blocker'
'aromatase_inhibitor'
'anti_estrogen'
'anthracycline'


#before chemo
'capecitabine'

#treatment for chemo
'chemotherapy'
'taxaneGeneral' 
'taxane'
'carboplatin'
'cetuximab'
'methotrexate'
'letrozole'
'trastuzumab'
'cyclophosphamide'
'paclitaxel'
'fluorouracil'
'doxorubicin'

# other treatment -> like radiotherapy
'other',
'cetuximab'
'radiotherapyClass'

#no treatment
'no_treatment', 

# hormone therapy
'hormone_therapy'
'hormone_therapyClass'


# post menopausal drug
'postmenopausal_only'


#  drug administration
'oral'
'intramuscular'
'intarvenous'


#tumor dna index
'DNA_index'

#tumor chromosome
'ploidy'

#measurements of tumor
'S_phase'

# tumor positive?
'cytokeratin5_pos'