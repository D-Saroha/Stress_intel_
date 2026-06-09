from flask import Blueprint, jsonify, request
from services.analytics_service import get_peer_benchmarking

analytics_bp = Blueprint(
    "analytics_bp",
    __name__
)

@analytics_bp.route(
    "/analytics/peer",
    methods=["POST"]
)
def peer_analytics():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "message": "Missing user data"}), 400
            
        result = get_peer_benchmarking(data)
        return jsonify({
            "success": True,
            "data": result
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500