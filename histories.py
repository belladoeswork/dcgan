H1 = ['horTh', 'age', 'menostat', 'tsize', 'tgrade', 'pnodes', 'progrec', 'estrec', 'time', 'cens', 'hormon', 'meno', 'surgery', 'radTh']
A1 = 'Decision 1 Hormone Therapy (Y/N)'
S2 = ['Prescribed Chemo (Single/doublet/triplet/quadruplet/none/NOS)',
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
A2 = 'Decision 2 Surgery (Y/N)'
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
A3 = 'Decision 3 Radiation Therapy (Y/N)'
Y = ['cens']
decisions = [A1, A2, A3]
histories = [H1, H2, H3]
states = [S2, S3, Y]
action_values = [(-1, 1), (-1, 1), (-1, 1)]

# histories before preprocessing
H1_prepr = ['Age at Diagnosis (Calculated)',
            'Pathological Grade',
            'Gender',
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