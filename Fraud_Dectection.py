import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#1a. imported payroll.CSV
Payroll_df = pd.read_csv('payroll.csv')
Positions_df = pd.read_csv('positions.csv') 

# List of columns to drop
columns_to_drop = ['Project','Unnamed: 9', 'Unnamed: 11', 'Value', 'Unnamed: 13']

# Drop specified columns in payroll dataset, ignoring errors if columns do not exist
Payroll_df.drop(columns=columns_to_drop, errors='ignore', inplace=True)

# Saves filtered dataset into CSV
new_payroll_df = Payroll_df.to_csv('New payroll.csv', index= False)
new_payroll_df = pd.read_csv('New payroll.csv')

# Merge payroll and position by name
merged_df = pd.merge(new_payroll_df, Positions_df, on= "Name")

# Save the merged dataset to a new CSV file
merged_df.to_csv('Merged.csv', index= False)
merged_df =  pd.read_csv("Merged.csv")

# Checks if the data has correct format
merged_df["Date"] = pd.to_datetime(merged_df['Date'])

# Filter by date
filtered_df = merged_df[(merged_df['Date'] >= '2024-02-02') & (merged_df['Date'] <= '2024-05-31')]

# Filter by purpose codes
filtered_df = filtered_df[(filtered_df['Speed Type'] == 'CISC112828') | (filtered_df['Speed Type'] == 'CISC112822')]

# Adding Duration columns to the dataset
#filtered_df.insert(9, "Duration", 0)

# Saved the the new dataset in a CSV file

# Ensure 'Start Time' and 'End Time' are in datetime format
filtered_df['Start Time'] = pd.to_datetime(filtered_df['Start Time'], format='%I:%M %p', errors='coerce')
filtered_df['End Time'] = pd.to_datetime(filtered_df['End Time'], format='%I:%M %p', errors='coerce')

# Adjust end time by adding 24 hours if start time is greater than end time
filtered_df["End Time"] = filtered_df.apply(lambda row: row["End Time"] + pd.Timedelta(days=1) if row["Start Time"] > row["End Time"] else row["End Time"], axis=1)

# Total Hours worked
filtered_df["Duration"] = ((filtered_df["End Time"] - filtered_df["Start Time"]).dt.total_seconds() / 3600).round(3)

# Saved the the new dataset in a CSV file
filtered_df.to_csv('Filtered.csv', index= False)


