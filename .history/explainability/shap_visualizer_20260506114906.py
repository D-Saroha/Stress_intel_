import os
import shap
import matplotlib.pyplot as plt

from config import Config

from models.utils.model_loader import (
    load_model
)


model = load_model()

explainer = shap.TreeExplainer(
    model
)


def generate_shap_summary_plot(
    processed_features,
    feature_names
):

    shap_values = explainer.shap_values(
        processed_features
    )

    output_path = os.path.join(
        "visualizations",
        "charts",
        "shap_summary_plot.png"
    )

    os.makedirs(
        os.path.dirname(output_path),
        exist_ok=True
    )

    shap.summary_plot(
        shap_values,
        processed_features,
        feature_names=feature_names,
        show=False
    )

    plt.savefig(
        output_path,
        bbox_inches="tight"
    )

    plt.close()

    return output_path