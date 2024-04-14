from functions import *


##Male vs Female  
df = create_binary_column(df, 'gender', 1, 'f_m')

# Family Compatibility 
comparison_binary(df, 'family_compatible', separate_column='f_m', label_0='Female', label_1='Male')

# Concerns about family is deterrent
comparison_binary(df, 'family_concerns_det', separate_column='f_m', label_0='Female', label_1='Male')

# Workload is deterrent 
comparison_binary(df, 'workload_det', separate_column='f_m', label_0='Female', label_1='Male')

# Number of extra years deterrent
comparison_binary(df, 'add_training_det', separate_column='f_m', label_0='Female', label_1='Male')

# Stress deterrent
comparison_binary(df, 'family_compatible', separate_column='f_m', label_0='Female', label_1='Male')

# Mentorship deterrent
comparison_binary(df, 'family_compatible', separate_column='f_m', label_0='Female', label_1='Male')

# Family/spouse barrier
comparison_binary(df, 'family_compatible', separate_column='f_m', label_0='Female', label_1='Male')

# Exposure enough
comparison_binary(df, 'family_compatible', separate_column='f_m', label_0='Female', label_1='Male')

# Equal gender representation training programs
comparison_binary(df, 'family_compatible', separate_column='f_m', label_0='Female', label_1='Male')

# Equal gender representation surgical programs 
comparison_binary(df, 'family_compatible', separate_column='f_m', label_0='Female', label_1='Male')