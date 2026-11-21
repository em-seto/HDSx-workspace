# Testing Log — Assignment 7

## Test 1: Initial Dashboard Render

**Selected income group:** Low Income (<1.3)

**Action:** Rendered `dashboard.qmd` using the Quarto render command.

**Result:** The dashboard generated an HTML file successfully. The visualization displayed the selected Low Income group.

**Status:** Passed.

## Test 2: Alternative Income Group

**Selected income group:** Middle Income

**Action:** Changed the `selected_income` value from Low Income to Middle Income and rendered the dashboard again.

**Result:** The HTML file was regenerated. I visually confirmed that the plot and its title displayed Middle Income. The summary table contained the expected columns: `Cycle`, `n`, and `mean_bmi`. I did not independently verify the numerical values in the table.

**Status:** Passed for rendering and plot/title updates; numerical table values not independently verified.

## Test 3: Restore Original Selection

**Selected income group:** Low Income (<1.3)

**Action:** Changed `selected_income` back to Low Income and rendered the dashboard again.

**Result:** Confirmed that the source file selected Low Income and that the final visualization displayed Low Income.

**Status:** Passed.

## Final Checks

- The dashboard source file and rendered HTML are present in the submission folder.
- The Interpretation section was adapted for public-health analysts.
- The original data processing and calculations were preserved.
- The dashboard continues to describe unweighted patterns rather than causal relationships.

## Remaining Verification

The exact numerical table values were not independently checked against a separate calculation. No render warnings or errors were reported in this log because the full render output was not retained for review.
