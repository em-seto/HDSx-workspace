# Visual Audit Note

## Plot Question

How does mean BMI differ across income groups and NHANES survey cycles?

## Issues Checked

| Issue | Category | Why it matters | Correction |
|---|---|---|---|
| The original graph only included the first and last NHANES cycles. | Correctness | Excluding intermediate cycles hides fluctuations and makes it difficult to understand changes over time. | Included all available NHANES cycles in the corrected graph. |
| The y-axis was restricted to BMI values between 24 and 28. | Design | A narrow y-axis can exaggerate the visual differences between income groups. | Removed the fixed y-axis limits so the graph displays the observed values without clipping. |
| The title claimed that low income drives rising obesity. | Interpretation | The graph only shows descriptive associations and cannot establish that income causes obesity. | Changed the title to "Mean BMI by Income Group Across NHANES Cycles." |
| The subtitle claimed that BMI increased steadily across every cycle. | Interpretation | The original graph only displayed two cycles, so it could not support a claim about steady increases. | Included all cycles and replaced the subtitle with a neutral description. |

## Final Caption

Mean body mass index (BMI, kg/m²) across NHANES survey cycles, grouped by income category. Data were obtained from the NHANES equity dataset. Observations with missing BMI, income group, or survey cycle information were excluded. Values represent unweighted group means. The graph shows descriptive differences and trends but does not establish causation or account for potential confounding factors.

## AI-Use Check

I used ChatGPT to help identify misleading elements in the original visualization, revise the R code, and improve the graph's labels and interpretation. I checked the revised graph against the original code and visually reviewed the output to confirm that all available survey cycles were included. I also verified that the revised title and caption describe the data without making unsupported causal claims.
