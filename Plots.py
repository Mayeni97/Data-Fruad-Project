import pandas as pd
import seaborn as sns

# Load the CSV files
instructors_stats = pd.read_csv('instructors_stats.csv')
person_total_hours = pd.read_csv('person_total_hours.csv')
weekly_hours_stats = pd.read_csv('weekly_hours_stats.csv')
violations_df = pd.read_csv('weekly_hours_violations.csv')

import matplotlib.pyplot as plt

# Pie Chart: Distribution of Total Hours Worked by Individuals
person_total_hours_top10 = person_total_hours.head(10)  # Selecting top 10 for better visualization
labels = person_total_hours_top10['Name']
sizes = person_total_hours_top10['Total Hours']

plt.figure(figsize=(10, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Total Hours Worked by Top 10 Individuals')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

# Histogram: Distribution of the Mean Weekly Hours
mean_weekly_hours = weekly_hours_stats['Mean']

plt.figure(figsize=(10, 6))
plt.hist(mean_weekly_hours, bins=10, edgecolor='black')
plt.title('Distribution of Mean Weekly Hours')
plt.xlabel('Mean Weekly Hours')
plt.ylabel('Frequency')
plt.show()

# Bar Chart: Mean Hours of Different Instructors
instructor_names = instructors_stats['Spring Instructor']
mean_hours = instructors_stats['Mean']

plt.figure(figsize=(12, 6))
plt.bar(instructor_names, mean_hours, color='skyblue', edgecolor='black')
plt.title('Mean Hours of Different Instructors')
plt.xlabel('Instructor')
plt.ylabel('Mean Hours')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y')
plt.show()

violations_df['Date'] = pd.to_datetime(violations_df['Date'])

# Create a scatter plot for the 'Duration' over 'Date' for each 'Name'
plt.figure(figsize=(12, 6))
sns.scatterplot(data=violations_df, x='Date', y='Duration', hue='Name', palette='tab10')
plt.title('Scatter Plot of Duration over Date by Name')
plt.xlabel('Date')
plt.ylabel('Duration')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.show()

# Create a box plot for the 'Duration' grouped by 'Name'
plt.figure(figsize=(12, 6))
sns.boxplot(x='Name', y='Duration', data=violations_df)
plt.title('Box Plot of Duration by Name')
plt.xlabel('Name')
plt.ylabel('Duration')
plt.xticks(rotation=45)
plt.show()