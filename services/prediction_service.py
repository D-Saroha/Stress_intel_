from models.inference.predictor import predict_stress
from explainability.shap_engine import generate_shap_explanation
from services.report_service import create_comprehensive_report
from utils.helpers import format_prediction_response

def generate_prediction(data):
    # 1. Run ML Inference
    prediction_result = predict_stress(data)
    prediction = prediction_result["prediction"]
    probability = prediction_result["probability"]
    processed_features = prediction_result["processed_features"]
    prediction_encoded = prediction_result.get("prediction_encoded", 0)

    # 2. Run SHAP Explainability
    shap_result = generate_shap_explanation(processed_features, prediction_encoded)
    shap_values = shap_result["shap_values"]
    feature_importance = shap_result["feature_importance"]

    # 3. Generate Comprehensive Clinical Report (Bio + Journal)
    journal_text = data.get("journal_entry")
    report_data = {
        "prediction": prediction,
        "probability": probability,
        "feature_importance": feature_importance,
        "user_data": data
    }
    
    comprehensive_report = create_comprehensive_report(report_data, journal_text)

    # 4. Format final response
    response = format_prediction_response(
        prediction=prediction,
        probability=probability,
        shap_values=shap_values,
        feature_importance=feature_importance,
        clinical_report=comprehensive_report
    )

    return response