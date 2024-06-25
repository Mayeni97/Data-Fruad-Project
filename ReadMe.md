# Payroll and Positions Data Processing

## Overview
This script processes payroll and positions data from CSV files to analyze and filter information based on specific criteria such as date range and purpose codes. It performs data cleaning, merging, filtering, and computation of work durations. The resulting dataset is saved in CSV format for further analysis or reporting.

## Files
- **payroll.csv**: Original payroll data file.
- **positions.csv**: File containing position-related information.
- **New payroll.csv**: Filtered payroll data after dropping unnecessary columns.
- **Merged.csv**: Merged dataset combining filtered payroll and positions data.
- **Filtered.csv**: Final dataset after filtering by date and purpose codes, with computed work durations.

## Steps Performed
1. **Data Cleaning and Preparation**:
   - Imported `payroll.csv` and `positions.csv`.
   - Dropped unnecessary columns (`'Project', 'Unnamed: 9', 'Unnamed: 11', 'Value', 'Unnamed: 13'`) from `payroll.csv`.
   - Saved the cleaned payroll data to `New payroll.csv`.

2. **Data Merging**:
   - Merged cleaned payroll data (`New payroll.csv`) with positions data (`positions.csv`) based on employee names.
   - Saved the merged dataset to `Merged.csv`.

3. **Data Filtering**:
   - Converted the 'Date' column to datetime format.
   - Filtered data for the period between '2024-02-02' and '2024-05-31'.
   - Further filtered data based on specific purpose codes (`'CISC112828', 'CISC112822'`).

4. **Duration Calculation**:
   - Added a 'Duration' column to compute hours worked.
   - Adjusted for negative duration values by adding 12 hours.
   - Set 'Duration' to NaN where 'Start Time' or 'End Time' is missing.

5. **Output**:
   - Saved the final filtered dataset with computed durations to `Filtered.csv`.

## Requirements
- Python (3.x recommended)
- Libraries: `numpy`, `pandas`, `matplotlib` (for any plotting functions, though not explicitly used in this script)

## Notes
- Ensure CSV files (`payroll.csv` and `positions.csv`) are in the same directory as the script.
- The script assumes specific column names and formats for input files (`payroll.csv` and `positions.csv`). Modify as needed for different datasets.

## Usage
1. Place `payroll.csv` and `positions.csv` in the same directory as this script.
2. Run the script in a Python environment with required libraries installed.
3. Check outputs (`New payroll.csv`, `Merged.csv`, `Filtered.csv`) for cleaned, merged, and filtered datasets respectively.
