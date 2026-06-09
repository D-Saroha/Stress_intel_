import pandas as pd


def create_engineered_features(df):

    df = df.copy()

    df["sleep_study_ratio"] = (
        df["sleep_hours"] /
        (df["study_hours"] + 1)
    )

    df["activity_screen_balance"] = (
        df["physical_activity"] -
        df["screen_time"]
    )

    df["wellness_score"] = (
        df["sleep_hours"] +
        df["physical_activity"] +
        df["diet_quality"] +
        df["social_interaction"]
    ) / 4

    df["stress_risk_index"] = (
        df["anxiety_score"] +
        df["screen_time"] +
        df["heart_rate"]
    ) / 3

    return df