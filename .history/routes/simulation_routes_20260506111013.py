from flask import Blueprint, jsonify


simulation_bp = Blueprint(
    "simulation_bp",
    __name__
)


@simulation_bp.route(
    "/simulate",
    methods=["GET"]
)
def simulate():

    return jsonify({
        "success": True,
        "message": "Simulation endpoint working"
    })