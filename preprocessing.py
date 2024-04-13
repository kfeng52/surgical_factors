import pandas as pd

# File path of your CSV file
file_path = "raw_survey_data_2024-04.csv"

# Use pandas to read the CSV file and load it into a DataFrame
df = pd.read_csv(file_path)



### FUNCTIONS

# Removes rows with certain values 
def remove_rows_with_value(df, column_name, value):
    return df[df[column_name] == value]

### ANALYSIS 
df = remove_rows_with_value(df, 'survey_questions_complete', 2)



file_path = 'clean_data.csv'
df.to_csv(file_path, index=False)  # Setting index=False to not write row indices to the CSV file
