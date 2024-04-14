from functions import *

##JR vs SR  
df = create_binary_column(df, 'med_year', 2, 'jr_sr')

# Family Compatibility 
comparison_binary(df, 'family_compatible', separate_column='jr_sr', label_0='JR', label_1='SR')

# Concerns about family is deterrent
comparison_binary(df, 'family_concerns_det', separate_column='jr_sr', label_0='JR', label_1='SR')

# Workload is deterrent 
comparison_binary(df, 'workload_det', separate_column='jr_sr', label_0='JR', label_1='SR')

# Number of extra years deterrent
comparison_binary(df, 'add_training_det', separate_column='jr_sr', label_0='JR', label_1='SR')

# Stress deterrent
comparison_binary(df, 'stress_levels_det', separate_column='jr_sr', label_0='JR', label_1='SR')

# Mentorship deterrent
comparison_binary(df, 'mentor_barrier', separate_column='jr_sr', label_0='JR', label_1='SR')

# Family/spouse barrier
comparison_binary(df, 'family_support', separate_column='jr_sr', label_0='JR', label_1='SR')

# Exposure enough
comparison_binary(df, 'enough_exposure', separate_column='jr_sr', label_0='JR', label_1='SR')

# Equal gender representation training programs
comparison_binary(df, 'equal_rep_res', separate_column='jr_sr', label_0='JR', label_1='SR')

# Equal gender representation surgical programs 
comparison_binary(df, 'equal_rep_atten', separate_column='jr_sr', label_0='JR', label_1='SR')


