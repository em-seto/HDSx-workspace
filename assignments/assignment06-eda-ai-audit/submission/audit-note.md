# Table 1 Audit Note

## Cohort

The intended cohort includes adults aged 20–80 (inclusive) from the classroom NHANES dataset. The original starter incorrectly used `Age > 20` and `Age < 80`, excluding participants aged exactly 20 and 80. I corrected this using `Age >= 20` and `Age <= 80`.

The corrected analysis cohort includes 57,137 participants.

## Missingness

I examined missing values for Age, BMI, and IncomeGroup before generating Table 1.

- Age: 0 missing values (0%)
- BMI: 1,009 missing values (1.77%)
- IncomeGroup: 5,395 missing values (9.44%)

The original starter used `na.omit()`, which unnecessarily removes participants with missing values in any column. Instead, I excluded missing values only when necessary for the relevant calculations.

## Planted Issues

| Issue | Category | Why it matters | Corrected approach |
|---|---|---|---|
| The cohort used `Age > 20` and `Age < 80`. | Correctness | Excludes participants exactly aged 20 and 80. | Use `Age >= 20` and `Age <= 80`. |
| The starter used `na.omit()` on the entire dataset. | Correctness | Removes participants with missing values in unrelated variables. | Examine missingness and exclude values only when necessary. |
| The starter used `var()` instead of `sd()`. | Correctness | Variance is not the same as standard deviation, making the table misleading. | Use `sd()` for BMI and age. |
| The starter included a hard-coded Windows file path. | Reproducibility | The file path may not work on other computers. | Use a repository-relative file path. |
| The starter claimed the data was freshly downloaded from NHANES. | Stewardship | Incorrectly describes the origin of the classroom dataset. | Identify the source as the provided classroom NHANES dataset. |
| The interpretation claimed statistically significant differences without testing. | Interpretation | Descriptive statistics alone cannot establish statistical significance. | Report descriptive differences without claiming significance. |
| The interpretation claimed that income determines BMI. | Interpretation | Observed associations do not establish causation. | Use noncausal language. |
| The starter described the results as publication-ready. | Stewardship | Missingness, provenance, and analytical limitations were not adequately addressed. | Acknowledge limitations and avoid overstating the results. |

## AI-Use Check

I used chatgpt to help identify errors in the starter code, develop corrected R code, and organize the audit findings.

I verified the corrections by rendering the Quarto document, examining the missingness counts, and reviewing the generated Table 1 CSV. I also checked that the code used inclusive age boundaries, calculated standard deviations rather than variances, and avoided unsupported claims of statistical significance or causation.
