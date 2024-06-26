# Payroll and Position Data Processing

## Overview
This project involves processing and analyzing payroll and position data. The process includes importing CSV files, merging datasets, filtering data, calculating descriptive statistics, and identifying specific patterns such as weekly hours violations and holiday work entries.

## Setup and Usage

### Prerequisites
Ensure you have the following Python packages installed:
- numpy
- pandas
- matplotlib

You can install these packages using pip:
```bash
pip install numpy pandas matplotlib
```

### Files
- `payroll.csv`: The main payroll data file.
- `positions.csv`: The positions data file.
- `New payroll.csv`: The filtered payroll data.
- `Merged.csv`: The merged payroll and positions data.
- `Filtered.csv`: The filtered and processed data.
- `instructors_stats.csv`: Statistics for each instructor.
- `person_total_hours.csv`: Total hours worked by each person.
- `weekly_hours_stats.csv`: Descriptive statistics for weekly hours worked.
- `weekly_hours_violations.csv`: Instances where weekly hours exceed 10.
- `holiday_entries.csv`: Work entries on designated holidays.

### Step-by-Step Guide

#### Step 1: Data Import and Initial Processing
The first script imports the payroll and position data, filters unnecessary columns, merges the datasets, and processes the time data. The full code for this step can be found [here](https://github.com/Mayeni97/Data-Fruad-Project/blob/Main/Fraud_Dectection.py).

#### Step 2: Data Analysis and Reporting
The second script loads the filtered data, calculates descriptive statistics, identifies weekly hours violations, and records work on holidays. The full code for this step can be found [here](https://github.com/Mayeni97/Data-Fruad-Project/blob/Main/Data_Analysis.py).

### Outputs
1. `New payroll.csv`: Filtered payroll data.
2. `Merged.csv`: Merged payroll and positions data.
3. `Filtered.csv`: Filtered and processed data.
4. `instructors_stats.csv`: Descriptive statistics for each instructor.
5. `person_total_hours.csv`: Total hours worked by each person.
6. `weekly_hours_stats.csv`: Descriptive statistics for weekly hours worked.
7. `weekly_hours_violations.csv`: Instances where weekly hours exceed 10.
8. `holiday_entries.csv`: Work entries on designated holidays.

### Notes
- Ensure the date formats in the CSV files match the expected formats in the scripts.
- Update the list of designated holidays as per your requirements.
