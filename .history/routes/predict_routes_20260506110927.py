from flask import Blueprint, jsonify, request

from services.prediction_service import generate_prediction
from utils.validators import validate_prediction_input


predict_bp = Blueprint(
    "predict_bp",
    __name__
)


@predict_bp.route(
    "/predict",
    methods=["POST"]
)
def predict():

    try:

        data = request.get_json()

        if not data:
            return jsonify({
                "success": False,
                "message": "No input data provided"
            }), 400

        missing_fields = validate_prediction_input(data)

        if missing_fields:
            return jsonify({
                "success": False,
                "missing_fields": missing_fields
            }), 400

        result = generate_prediction(data)

        return jsonify({
            "success": True,
            "data": result
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500