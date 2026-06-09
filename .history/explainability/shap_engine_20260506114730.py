import shap
import numpy as np

from models.utils.model_loader import (
    load_model
)


model = load_model()

explainer = shap.TreeExplainer(
    model
)


def generate_shap_explanation(
    processed_features
):

    shap_values = explainer.shap_values(
        processed_features
    )

    if isinstance(shap_values, list):
        shap_values = shap_values[0]

    shap_values = np.array(
        shap_values
    )

    feature_importance = []

    for index, value in enumerate(
        shap_values[0]
    ):

        feature_importance.append({
            "feature_index": index,
            "importance": round(
                abs(float(value)),
                4
            )
        })

    feature_importance = sorted(
        feature_importance,
        key=lambda x: x["importance"],
        reverse=True
    )

    return {
        "shap_values": shap_values.tolist(),
        "feature_importance": feature_importance
    }