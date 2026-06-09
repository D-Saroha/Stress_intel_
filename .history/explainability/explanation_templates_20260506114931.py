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
            f"Sleep duration showed a {severity} influence on the stress prediction.",

        "study_hours":
            f"Academic workload contributed a {severity} impact on stress levels.",

        "physical_activity":
            f"Physical activity patterns demonstrated a {severity} relationship with stress.",

        "social_interaction":
            f"Social interaction levels had a {severity} effect on emotional balance.",

        "screen_time":
            f"Screen exposure contributed a {severity} influence on stress indicators.",

        "diet_quality":
            f"Diet quality showed a {severity} correlation with mental wellness.",

        "heart_rate":
            f"Heart rate trends revealed a {severity} physiological stress signal.",

        "anxiety_score":
            f"Anxiety markers showed a {severity} contribution to predicted stress."
    }

    return templates.get(
        feature_name,
        f"{feature_name} contributed a {severity} impact to the prediction."
    )