import pandas as pd


def summarise_bmi(data):
    """Summarise BMI by income group and gender after removing missing values."""
    filtered = data.dropna(subset=["BMI", "IncomeGroup", "Gender"])

    summary = (
        filtered.groupby(["IncomeGroup", "Gender"], as_index=False)
        .agg(
            n=("BMI", "count"),
            mean_bmi=("BMI", "mean"),
            median_bmi=("BMI", "median"),
            sd_bmi=("BMI", "std"),
        )
        .sort_values(["IncomeGroup", "Gender"])
        .reset_index(drop=True)
    )

    return summary
