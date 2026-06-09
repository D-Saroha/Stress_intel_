TARGET_COLUMN = "stress_level"

# Features for the basic assessment
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

# Names for all features used in model (including engineered)
ALL_MODEL_FEATURES = FEATURE_COLUMNS + [
    "sleep_study_ratio",
    "activity_screen_balance",
    "wellness_score",
    "stress_risk_index"
]

# Original Dataset Columns (21 features)
DATASET_COLUMNS = [
    "anxiety_level", "self_esteem", "mental_health_history", "depression",
    "headache", "blood_pressure", "sleep_quality", "breathing_problem",
    "diet_quality", "living_conditions", "safety", "basic_needs",
    "academic_performance", "study_load", "teacher_student_relationship",
    "future_career_concerns", "social_support", "peer_pressure",
    "extracurricular_activities", "bullying", "noise_level"
]

STRESS_LABELS = {
    0: "Low",
    1: "Medium",
    2: "High"
}

# High-Fidelity Sunset Palette
RISK_COLORS = {
    "Low": "#F59E0B",    # Amber
    "Medium": "#9D174D", # Berry
    "High": "#4C0519"    # Darkest Berry
}

CHART_COLORS = [
    "#F59E0B", # Amber
    "#9D174D", # Berry
    "#831843", # Deep Pink
    "#4C0519"  # Darkest Berry
]