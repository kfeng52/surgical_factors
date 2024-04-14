import pandas as pd
import matplotlib.pyplot as plt

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

def plot_frequency(df, column_name):
    # Count the frequency of each value in the column
    value_counts = df[column_name].value_counts()

    # Create the bar plot
    plt.bar(value_counts.index, value_counts.values)

    # Add text on top of each bar
    for i, v in zip(range(len(value_counts)), value_counts.values):
        plt.text(i, v, str(v), ha='center', va='bottom')

    # Remove gridlines
    plt.grid(False)

    # Show the plot
    plt.show()

def plot_value_counts_bar(df, column_name):
    """
    Plots a bar plot of the frequency of each count of a column in a DataFrame.
    
    Parameters:
        df (DataFrame): The DataFrame containing the data.
        column_name (str): The name of the column for which frequency is to be plotted.
    """
    # Get value counts
    value_counts = df[column_name].value_counts()
    
    # Plot bar plot
    plt.bar(value_counts.index, value_counts.values, color='blue', alpha=0.7)
    
    # Add count above each bar
    for i, v in enumerate(value_counts.values):
        plt.text(i, v + 0.1, str(v), ha='center')
    
    plt.xlabel(column_name)
    plt.ylabel('Frequency')
    plt.title('Bar Plot of Frequency of ' + column_name)
    plt.xticks(value_counts.index)  # Ensure x-axis ticks are aligned with bars
    plt.grid(False)  # Remove grid lines
    plt.show()


### ANALYSIS 

# Number of samples
print(f'The number of sample is {len(df)}')

#demo_mean, demo_median = calculate_mean_median(df, )

plot_value_counts_bar(df, 'gender')




'''
Demographic
Age
Male female distribution
Years in medical school

'''




