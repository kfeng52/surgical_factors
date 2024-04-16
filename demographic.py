from functions import *


# Number of samples
print(f'The number of sample is {len(df)}')

# Age 
age_mean, age_median, age_std = calculate_stats(df, 'age')

# Gender 
single_column(df, 'gender', ['Female', 'Male', 'Non-binary'])

# Ethnicity
list_ethnicity = ['race_culture___1', 'race_culture___2', 'race_culture___3', 'race_culture___4', 'race_culture___5', 'race_culture___6', 'race_culture___8', 'race_culture___9', 'race_culture___11', 'race_culture___13', 'race_culture___14', 'race_culture___15', 'race_culture___16', 'race_culture___999', 'race_culture___17', 'race_culture___18'
]
names_ethnicity = ['East Asian', 'South Asian', 'Southeast Asian', 'Black African', 'Black Caribbean', 'Black North American','Indian Caribbean', 'Indigenous', 'Latin American', 'Middle Eastern', 'White European', 'White North American', 'Mixed Heritage', 'Other', 'Prefer not to answer', 'Do not know']
multi_columns(df, list_ethnicity, names_ethnicity, plot_show=True)

# Med Year 
single_column(df, 'med_year', ['Year 1', 'Year 2', 'Year 3', 'Year 4', 'Other'], plot_show=True)
#single_column(df[df['med_year'] != 999], 'med_year', ['Year 1', 'Year 2', 'Year 3', 'Year 4'], plot_show=True)

# Have Children
single_column(df, 'children', ['No', 'Yes'])

# Intend to purse surgerical specialty 
single_column(df, 'specialty', ['No', 'Yes'])