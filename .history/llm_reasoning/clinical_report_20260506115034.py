from config import Config

from explainability.explanation_templates import (
    generate_feature_explanation
)


def generate_clinical_report(
    prediction,
    probability,
    feature_importance,
    user_data
):

    top_features = feature_importance[:3]

    report_sections = []

    report_sections.append(
        f"# StressIntel PRO Clinical Assessment\n"
    )

    report_sections.append(
        f"## Predicted Stress Level\n"
        f"**{prediction} Stress** "
        f"with confidence score of "
        f"**{probability}%**.\n"
    )

    report_sections.append(
        "## Behavioral & Physiological Findings\n"
    )

    for feature in top_features:

        feature_name = feature.get(
            "feature",
            "Unknown Feature"
        )

        importance = feature.get(
            "importance",
            0
        )

        explanation = generate_feature_explanation(
            feature_name,
            importance
        )

        report_sections.append(
            f"- {explanation}"
        )

    report_sections.append(
        "\n## Suggested Mitigation Actions\n"
    )

    if prediction.lower() == "high":

        report_sections.extend([
            "- Reduce prolonged academic overload.",
            "- Improve sleep recovery patterns.",
            "- Increase physical relaxation activity.",
            "- Consider mental health consultation."
        ])

    elif prediction.lower() == "medium":

        report_sections.extend([
            "- Maintain balanced academic scheduling.",
            "- Improve consistency in wellness habits.",
            "- Monitor anxiety and workload trends."
        ])

    else:

        report_sections.extend([
            "- Continue maintaining healthy routines.",
            "- Preserve current work-life balance.",
            "- Maintain consistent sleep and activity."
        ])

    report_sections.append(
        "\n---\n"
    )

    report_sections.append(
        Config.REPORT_DISCLAIMER
    )

    return "\n".join(
        report_sections
    )