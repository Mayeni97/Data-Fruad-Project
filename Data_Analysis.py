import pandas as pd
import numpy as np

# Loaded filtered.csv file
filtered_df = pd.read_csv('Filtered.csv')

# Convert 'Date' column to datetime
filtered_df['Date'] = pd.to_datetime(filtered_df['Date'])

# Extract week number and year
filtered_df['Week'] = filtered_df['Date'].dt.isocalendar().week
filtered_df['Year'] = filtered_df['Date'].dt.year

# Calculate overall descriptive statistics for total hours worked (Duration)
total_hours_mean = filtered_df['Duration'].mean()
total_hours_median = filtered_df['Duration'].median()
total_hours_mode = filtered_df['Duration'].mode()[0]
total_hours_std = filtered_df['Duration'].std()

total_hours_stats = {
    'Mean': total_hours_mean,
    'Median': total_hours_median,
    'Mode': total_hours_mode,
    'Standard Deviation': total_hours_std
}

# Calculate descriptive statistics for each instructor
instructors_stats = filtered_df.groupby('Spring Instructor')['Duration'].agg([
    ('Mean', 'mean'),
    ('Median', 'median'),
    ('Mode', lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan),
    ('Standard Deviation', 'std')
]).reset_index()

# Save instructor statistics to a file
instructors_stats_file = 'instructors_stats.csv'
instructors_stats.to_csv(instructors_stats_file, index=False)

# Calculate total hours worked by each person
person_total_hours = filtered_df.groupby('Name')['Duration'].sum().reset_index()
person_total_hours.columns = ['Name', 'Total Hours']

# Save total hours worked by each person to a file
person_total_hours_file = 'person_total_hours.csv'
person_total_hours.to_csv(person_total_hours_file, index=False)

# Calculate weekly hours worked for each person
weekly_hours = filtered_df.groupby(['Name', 'Year', 'Week'])['Duration'].sum().reset_index()

# Calculate overall descriptive statistics for weekly hours worked
weekly_hours_mean = weekly_hours['Duration'].mean()
weekly_hours_median = weekly_hours['Duration'].median()
weekly_hours_mode = weekly_hours['Duration'].mode()[0]
weekly_hours_std = weekly_hours['Duration'].std()

weekly_hours_stats = {
    'Mean': weekly_hours_mean,
    'Median': weekly_hours_median,
    'Mode': weekly_hours_mode,
    'Standard Deviation': weekly_hours_std
}

# Save weekly hours statistics to a file
weekly_hours_stats_file = 'weekly_hours_stats.csv'
weekly_hours_stats_df = pd.DataFrame([weekly_hours_stats])
weekly_hours_stats_df.to_csv(weekly_hours_stats_file, index=False)


