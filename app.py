from flask import Flask, jsonify, render_template
from flask_cors import CORS

from config import Config

# Route Blueprints
from routes.predict_routes import predict_bp
from routes.analytics_routes import analytics_bp
from routes.simulation_routes import simulation_bp
from routes.report_routes import report_bp
from routes.webcam_routes import webcam_bp
from routes.research_routes import research_bp


def create_app():
    """
    Application Factory for StressIntel PRO
    """

    app = Flask(__name__, 
                template_folder="frontend/templates",
                static_folder="frontend/static")

    # Load Configurations
    app.config.from_object(Config)

    # Enable CORS
    CORS(app)

    # ====================================
    # REGISTER BLUEPRINTS
    # ====================================
    app.register_blueprint(predict_bp, url_prefix="/api")
    app.register_blueprint(analytics_bp, url_prefix="/api")
    app.register_blueprint(simulation_bp, url_prefix="/api")
    app.register_blueprint(report_bp, url_prefix="/api")
    app.register_blueprint(webcam_bp, url_prefix="/api")
    app.register_blueprint(research_bp, url_prefix="/api")

    # ====================================
    # PAGE ROUTES (Frontend)
    # ====================================
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/dashboard")
    def dashboard():
        return render_template("dashboard.html")

    @app.route("/simulation-lab")
    def simulation_lab():
        return render_template("simulation_lab.html")

    @app.route("/peer-analytics")
    def peer_analytics():
        return render_template("peer_analytics.html")

    @app.route("/mitigation-planner")
    def mitigation_planner():
        return render_template("mitigation_planner.html")

    @app.route("/research-lab")
    def research_lab():
        return render_template("research_lab.html")

    @app.route("/about")
    def about():
        return render_template("about.html")

    # ====================================
    # HEALTH CHECK
    # ====================================
    @app.route("/health")
    def health():
        return jsonify({
            "project": "StressIntel PRO",
            "server": "active",
            "api": "working"
        })

    return app


# ====================================
# APPLICATION ENTRY
# ====================================
app = create_app()

if __name__ == "__main__":
    app.run(
        debug=Config.DEBUG,
        host="0.0.0.0",
        port=5000
    )