TARGET_COLUMN = "stress_level"

FEATURE_COLUMNS = [
    "sleep_hours",
    "study_hours",
    "physical_activity",
    "social_interaction",
    "screen_time",
    "diet_quality",
    "heart_rate",
    "anxiety_score"
]

STRESS_LABELS = {
    0: "Low",
    1: "Medium",
    2: "High"
}

RISK_COLORS = {
    "Low": "#34D399",
    "Medium": "#FBBF24",
    "High": "#EF4444"
}

CHART_COLORS = [
    "#1B264F",
    "#C1E6F1",
    "#F57E3E",
    "#F9A47C"
]