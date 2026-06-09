from flask import Blueprint, jsonify, request
from camera_module.face_capture import preprocess_face_frame
from camera_module.expression_detector import detect_stress_markers

webcam_bp = Blueprint(
    "webcam_bp",
    __name__
)

@webcam_bp.route(
    "/webcam/analyze",
    methods=["POST"]
)
def analyze_webcam():
    try:
        data = request.get_json()
        image_b64 = data.get("image")
        
        if not image_b64:
            return jsonify({"success": False, "message": "No image data provided"}), 400
            
        processed_frame = preprocess_face_frame(image_b64)
        markers = detect_stress_markers(processed_frame)
        
        return jsonify({
            "success": True,
            "data": markers
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500