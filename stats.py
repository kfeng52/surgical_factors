import pandas as pd

# File path of your CSV file
file_path = "clean_data.csv"

# Use pandas to read the CSV file and load it into a DataFrame
df = pd.read_csv(file_path)


### FUNCTIONS

# Function to calculate the mean and median
def calculate_mean_median(df, column_name):
    column_data = df[column_name]
    mean = column_data.mean()
    median = column_data.median()
    print(f'The mean of {column_name} is {mean} and the meddian is {median}')
    return mean, median

### ANALYSIS 

print(f'The number of sample is {len(df)}')

demo_mean, demo_median = calculate_mean_median(df, )

'''

Demographic
Age
Male female distribution
Years in medical school

'''

