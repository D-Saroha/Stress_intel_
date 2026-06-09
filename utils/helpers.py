import numpy as np


def convert_numpy_types(obj):

    if isinstance(obj, np.integer):
        return int(obj)

    if isinstance(obj, np.floating):
        return float(obj)

    if isinstance(obj, np.ndarray):
        return obj.tolist()

    return obj


def format_prediction_response(
    prediction,
    probability,
    shap_values,
    feature_importance,
    clinical_report
):

    return {
        "prediction": prediction,
        "probability": probability,
        "shap_values": shap_values,
        "feature_importance": feature_importance,
        "clinical_report": clinical_report
    }