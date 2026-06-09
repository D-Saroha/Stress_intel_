from flask import Blueprint, jsonify, request

from camera_module.expression_detector import (
    analyze_expression
)


webcam_bp = Blueprint(
    "webcam_bp",
    __name__
)


@webcam_bp.route(
    "/webcam/analyze",
    methods=["POST"]
)
def webcam_analysis():

    try:

        data = request.get_json()

        image_data = data.get("image")

        if not image_data:

            return jsonify({
                "success": False,
                "message": "No image data provided"
            }), 400

        result = analyze_expression(
            image_data
        )

        return jsonify({
            "success": True,
            "data": result
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500