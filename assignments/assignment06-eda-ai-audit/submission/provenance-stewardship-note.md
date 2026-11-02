# Data Provenance and Stewardship Note

## Data Provenance

This analysis used the `nhanes_equity_v6.csv` dataset provided in the HDSx course repository under `examples/nhanes-equity/data/`.

The dataset is a classroom NHANES-derived resource used for educational purposes. It was not independently downloaded from the NHANES website for this assignment.

## Data Handling

The analysis was restricted to participants aged 20–80, inclusive, resulting in 57,137 observations.

Missingness was examined for Age, BMI, and IncomeGroup before creating Table 1.

- Age: 0 missing values
- BMI: 1,009 missing values
- IncomeGroup: 5,395 missing values

Participants with missing IncomeGroup were excluded from the grouped summary because they could not be assigned to an income category. Missing BMI values were excluded only from BMI calculations.

The analysis used the provided classroom dataset without modifying the original CSV.

## Limitations

The analysis is descriptive and unweighted. Therefore, the results should not be interpreted as nationally representative estimates of the US population.

Differences in average BMI across income groups do not establish a causal relationship between income and BMI.

Missing values may also affect the interpretation of the results, particularly for IncomeGroup.

## Responsible Data Use

The dataset was used for educational analysis. Results are reported in aggregate rather than as individual participant records.

The analysis avoids unsupported statistical or causal claims and documents the source of the data, missingness, and analytical limitations to support transparency and reproducibility.
