from flask import Blueprint, jsonify


report_bp = Blueprint(
    "report_bp",
    __name__
)


@report_bp.route(
    "/report",
    methods=["GET"]
)
def report():

    return jsonify({
        "success": True,
        "message": "Report endpoint working"
    })