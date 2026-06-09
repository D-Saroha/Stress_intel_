from models.inference.predictor import predict_stress

from explainability.shap_engine import generate_shap_explanation

from llm_reasoning.clinical_report import generate_clinical_report

from utils.helpers import format_prediction_response


def generate_prediction(data):

    prediction_result = predict_stress(data)

    prediction = prediction_result["prediction"]

    probability = prediction_result["probability"]

    processed_features = prediction_result["processed_features"]

    shap_result = generate_shap_explanation(
        processed_features
    )

    shap_values = shap_result["shap_values"]

    feature_importance = shap_result["feature_importance"]

    clinical_report = generate_clinical_report(
        prediction=prediction,
        probability=probability,
        feature_importance=feature_importance,
        user_data=data
    )

    response = format_prediction_response(
        prediction=prediction,
        probability=probability,
        shap_values=shap_values,
        feature_importance=feature_importance,
        clinical_report=clinical_report
    )

    return response