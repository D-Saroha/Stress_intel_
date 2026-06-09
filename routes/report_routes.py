from flask import Blueprint, jsonify, request, render_template
import datetime
import random


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

@report_bp.route("/report/research", methods=["POST"])
def research_report():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "error": "No data provided"}), 400
            
        # Prepare report data
        report_id = f"{random.randint(1000, 9999)}"
        date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        return render_template(
            "research_report.html",
            report_id=report_id,
            date=date_str,
            data=data.get("user_data"),
            insight=data.get("insight"),
            visual_analysis=data.get("visual_analysis")
        )
    except Exception as e:
        return f"Error generating report: {str(e)}", 500