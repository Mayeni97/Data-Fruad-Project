import pandas as pd
import matplotlib.pyplot as plt


#1a. imported payroll.CSV
Payroll_df = pd.read_csv('payroll.csv')
Postions_df = pd.read_csv('positions.csv') 

# List of columns to drop
columns_to_drop = ['Project','Unnamed: 9', 'Unnamed: 11', 'Value', 'Unnamed: 13']

# Drop specified columns in payroll dataset, ignoring errors if columns do not exist
Payroll_df.drop(columns=columns_to_drop, errors='ignore', inplace=True)

# Saves filtered dataset into CSV
new_payroll_df = Payroll_df.to_csv('New payroll.csv', index= False)
new_payroll_df = pd.read_csv('New payroll.csv')

# Merge payroll and position by name
merged_df = pd.merge(new_payroll_df, Postions_df, on= "Name")

# Save the merged dataframe to a new CSV file
merged_df.to_csv('Merged.csv', index= False)
