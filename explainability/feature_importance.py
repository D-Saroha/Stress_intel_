from utils.constants import FEATURE_COLUMNS


def map_feature_importance(
    feature_importance
):

    mapped_features = []

    for item in feature_importance:

        feature_index = item["feature_index"]

        if feature_index < len(FEATURE_COLUMNS):

            feature_name = FEATURE_COLUMNS[
                feature_index
            ]

        else:

            engineered_index = (
                feature_index -
                len(FEATURE_COLUMNS)
            )

            engineered_features = [
                "sleep_study_ratio",
                "activity_screen_balance",
                "wellness_score",
                "stress_risk_index"
            ]

            feature_name = engineered_features[
                engineered_index
            ]

        mapped_features.append({
            "feature": feature_name,
            "importance": item["importance"]
        })

    return mapped_features