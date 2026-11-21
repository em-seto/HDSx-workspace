# Privacy Check — Assignment 7

## Data Source

The dashboard uses the prepared NHANES Health Equity classroom dataset (`nhanes_equity_v6.csv`) provided for the course.

The analysis is limited to adults aged 20–80 within a selected income group.

## Privacy Considerations

**1. Aggregate data presentation**

The dashboard displays aggregated descriptive statistics rather than individual-level records. The summary table contains NHANES cycle, observation count (`n`), and mean BMI (`mean_bmi`).

**2. No direct personal identifiers**

The dashboard does not intentionally display names, addresses, contact information, or other direct personal identifiers.

**3. Small-cell considerations**

I reviewed the observation counts (`n`) in the dashboard's summary table. The smallest displayed count was 1,089 observations.

No unusually small cells were identified in the displayed aggregate summary. This reduces concerns about disclosure through small observation counts, although it does not eliminate all potential privacy risks.

**4. Responsible interpretation**

The dashboard clearly states that the findings are descriptive and unweighted. The results should not be presented as nationally representative estimates or causal evidence.

**5. Data handling**

The dashboard uses the course-provided classroom dataset. No row-level data were included in the audience-facing table or plot, and no row-level records were provided to an external AI tool as part of this adaptation.

## Privacy Conclusion

The dashboard is designed to communicate aggregate descriptive information without displaying individual-level records. Before public distribution, the observation counts and rendered HTML should be reviewed to confirm that no sensitive information is inadvertently disclosed.
