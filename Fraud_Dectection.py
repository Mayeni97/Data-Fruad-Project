import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#1a. imported payroll.CSV
Payroll_df = pd.read_csv('payroll.csv') 

# List of columns to drop
columns_to_drop = ['Project','Unnamed: 9', 'Unnamed: 11', 'Value', 'Unnamed: 13']

# Drop specified columns in payroll dataset, ignoring errors if columns do not exist
Payroll_df.drop(columns=columns_to_drop, errors='ignore', inplace=True)

# Saves filtered dataset into CSV
new_payroll_df = Payroll_df.to_csv('New payroll.csv', index= False)

