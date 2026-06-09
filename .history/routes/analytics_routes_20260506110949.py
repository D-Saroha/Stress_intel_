from flask import Blueprint, jsonify


analytics_bp = Blueprint(
    "analytics_bp",
    __name__
)


@analytics_bp.route(
    "/analytics",
    methods=["GET"]
)
def analytics():

    return jsonify({
        "success": True,
        "message": "Analytics endpoint working"
    })