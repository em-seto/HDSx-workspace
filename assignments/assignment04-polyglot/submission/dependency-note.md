# Dependency note
- The r analysis uses the tidyverse package, including readr for importing the csv dataset and dplyr for filtering, grouping, and summarizing observations
- the analysis is written in a quarto (.qmd) document and rendered to html

# Python dependencies
- the python analysis uses:
1. pandas for importing and analysing the nhanes dataset
2. sys (python standard library) to locate and import the local helpers.py module
3. jupyter notebook to execute the python code

helpers.py contains a reusable function that calculates bmi summary statistics by income group and gender

# Reproducibility
- r and python use the same local dataset: examples/nhanes-equity/data/nhanes_equity_v6.csv
- both analyses remove observations with missing bmi, income group, or gender values before calculating the grouped summaries
- the results were compared using parity-table.csv
- all 5 parity checks matched, including the summary statistics rounded to 2 decimal places
- the analysis is descriptive and does not account for the nhanes complex survey design - the results should not be interpreted as population-representative estimates