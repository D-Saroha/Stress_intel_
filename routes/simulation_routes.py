from flask import Blueprint, jsonify, request
from services.simulation_service import run_simulation

simulation_bp = Blueprint(
    "simulation_bp",
    __name__
)

@simulation_bp.route(
    "/simulation/run",
    methods=["POST"]
)
def simulation_run():
    try:
        data = request.get_json()
        base_data = data.get("baseData")
        modifications = data.get("modifications")
        
        if not base_data or not modifications:
            return jsonify({"success": False, "message": "Missing simulation parameters"}), 400
            
        result = run_simulation(base_data, modifications)
        return jsonify({
            "success": True,
            "data": result
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500