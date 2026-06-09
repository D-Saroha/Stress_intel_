import shap
import numpy as np

from models.utils.model_loader import (
    load_model
)


model = load_model()

explainer = shap.TreeExplainer(
    model
)


from utils.constants import FEATURE_COLUMNS

from utils.constants import FEATURE_COLUMNS

from utils.constants import ALL_MODEL_FEATURES

def generate_shap_explanation(processed_features, prediction_index=0):
    shap_results = explainer.shap_values(processed_features)

    if isinstance(shap_results, list):
        # Use the SHAP values for the predicted class
        if prediction_index < len(shap_results):
            shap_values = shap_results[prediction_index]
        else:
            shap_values = shap_results[0]
    else:
        shap_values = shap_results

    feature_importance = []
    
    if len(shap_values.shape) > 1:
        sample_shap = shap_values[0]
    else:
        sample_shap = shap_values

    for index, value in enumerate(sample_shap):
        # Use the full list of features used during training
        feature_name = ALL_MODEL_FEATURES[index] if index < len(ALL_MODEL_FEATURES) else f"feature_{index}"
        
        scalar_value = value if np.isscalar(value) else value[0]
        
        feature_importance.append({
            "feature": feature_name,
            "importance": round(float(scalar_value), 4)
        })

    feature_importance = sorted(
        feature_importance,
        key=lambda x: abs(x["importance"]),
        reverse=True
    )

    return {
        "shap_values": shap_values.tolist(),
        "feature_importance": feature_importance
    }

