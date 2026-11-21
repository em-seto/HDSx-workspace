# Reproducibility Note — Assignment 7

## Data Source

The dashboard uses the course-provided NHANES Health Equity classroom dataset (`nhanes_equity_v6.csv`).

The dataset is loaded from the repository's `examples/nhanes-equity/data/` directory.

## Software and Dependencies

The dashboard is written in Quarto using R.

The required R packages are:
- `tidyverse` for data manipulation and visualization.
- `knitr` for rendering the summary table.

Quarto is used to render the dashboard as a standalone HTML document.

## Reproduction Steps

1. Open the `HDSx-workspace` repository in GitHub Codespaces.
2. Ensure that Quarto, R, and the required R packages are available.
3. From the repository root, run:

   `quarto render assignments/assignment07-dashboard/submission/dashboard.qmd`

4. Open the generated `dashboard.html` file to view the dashboard.

## Income Group Selection

The dashboard uses a static control value defined by `selected_income` in the Quarto source file.

The default selection is `"Low Income (<1.3)"`.

To reproduce the dashboard for another income group, change `selected_income` to a valid value such as `"Middle Income"` or `"High Income (>3.5)"`, save the file, and render it again.

## Reproducibility Considerations

The dashboard retains the original starter's data processing, age restrictions, missing-data exclusions, and descriptive BMI calculations.

Only the audience-facing Interpretation section was modified.

The analysis is descriptive and unweighted. Reproducing the dashboard requires access to the same prepared classroom dataset and a compatible R and Quarto environment.
