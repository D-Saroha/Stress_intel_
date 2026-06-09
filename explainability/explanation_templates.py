def generate_feature_explanation(
    feature_name,
    importance
):

    if importance >= 1.5:

        severity = "strong"

    elif importance >= 0.7:

        severity = "moderate"

    else:

        severity = "mild"

    templates = {
        "sleep_hours":
            f"Sleep patterns showed a {severity} influence on recovery capacity.",
        "study_hours":
            f"Academic workload contributed a {severity} impact on neural fatigue.",
        "physical_activity":
            f"Physical activity levels demonstrated a {severity} role in cortisol regulation.",
        "social_interaction":
            f"Social engagement had a {severity} effect on emotional resilience.",
        "screen_time":
            f"Digital exposure contributed a {severity} influence on cognitive load.",
        "diet_quality":
            f"Nutritional biomarkers showed a {severity} correlation with metabolic stress.",
        "heart_rate":
            f"Physiological heart rate trends revealed a {severity} autonomic stress signal.",
        "anxiety_score":
            f"Psychological anxiety markers showed a {severity} contribution to predicted stress.",
        "sleep_study_ratio":
            f"The balance between rest and cognitive load was a {severity} factor.",
        "wellness_score":
            f"The integrated wellness index showed a {severity} predictive value."
    }

    return templates.get(
        feature_name,
        f"{feature_name} contributed a {severity} impact to the prediction."
    )