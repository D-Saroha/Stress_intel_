def generate_recommendations(
    prediction,
    user_data
):

    recommendations = []

    sleep_hours = user_data.get(
        "sleep_hours",
        0
    )

    study_hours = user_data.get(
        "study_hours",
        0
    )

    physical_activity = user_data.get(
        "physical_activity",
        0
    )

    screen_time = user_data.get(
        "screen_time",
        0
    )

    anxiety_score = user_data.get(
        "anxiety_score",
        0
    )

    if sleep_hours < 6:

        recommendations.append(
            "Increase daily sleep duration to improve recovery and cognitive balance."
        )

    if study_hours > 8:

        recommendations.append(
            "Reduce continuous academic workload and include scheduled breaks."
        )

    if physical_activity < 3:

        recommendations.append(
            "Increase physical activity to support stress regulation."
        )

    if screen_time > 8:

        recommendations.append(
            "Limit excessive screen exposure to reduce mental fatigue."
        )

    if anxiety_score > 7:

        recommendations.append(
            "Monitor anxiety indicators and consider guided stress management practices."
        )

    if not recommendations:

        recommendations.append(
            "Current behavioral patterns appear balanced. Maintain consistency."
        )

    return recommendations