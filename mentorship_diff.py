from functions import *

##Male vs Female  
df = create_binary_column(df, 'gender', 1, 'f_m')

# Mentor plots
# comparison_binary(df, 'my_mentor_is_a', separate_column='f_m', label_0='Female', label_1='Male', x_labels=['Male', 'Female', 'Other', 'No Mentor'])

# Getting the data
group_0 = df[df['f_m'] == 0]
group_1 = df[df['f_m'] == 1]
# Get all unique values in the specified column
unique_values = df['my_mentor_is_a'].dropna().unique()
unique_values.sort()
# Count the frequency of each value in the specified column for each group
value_counts_female = group_0['my_mentor_is_a'].value_counts().reindex(unique_values, fill_value=0)
value_counts_male = group_1['my_mentor_is_a'].value_counts().reindex(unique_values, fill_value=0)

def stats(panda_series):
    # Sum of all females 
    sum = panda_series.sum()
    # Male mentors
    print(f"The percent that have male mentors is: {panda_series[1]/sum * 100}%")
    # Female mentors
    print(f"The percent that have female mentors is: {panda_series[2]/sum * 100}%")
    # Other mentors
    print(f"The percent that have other mentors is: {panda_series[3]/sum * 100}%")
    # No mentors
    print(f"The percent that have no mentors is: {panda_series[4]/sum * 100}%\n")

# Females
stats(value_counts_female)

# Males
stats(value_counts_male)