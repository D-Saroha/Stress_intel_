"""
Service to handle SHAP explainability requests.
"""

from explainability.shap_engine import generate_shap_explanation

def get_shap_analysis(processed_features):
    """
    Retrieves SHAP values and feature importance.
    """
    try:
        result = generate_shap_explanation(processed_features)
        return {
            "success": True,
            "shap_values": result["shap_values"],
            "feature_importance": result["feature_importance"]
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
