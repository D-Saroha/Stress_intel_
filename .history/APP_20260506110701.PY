from flask import Flask, jsonify
from flask_cors import CORS

from config import Config

# Route Blueprints
from routes.predict_routes import predict_bp
from routes.analytics_routes import analytics_bp
from routes.simulation_routes import simulation_bp
from routes.report_routes import report_bp


def create_app():
    """
    Application Factory for StressIntel PRO
    """

    app = Flask(__name__)

    # Load Configurations
    app.config.from_object(Config)

    # Enable CORS
    CORS(app)

    # ====================================
    # REGISTER BLUEPRINTS
    # ====================================
    app.register_blueprint(
        predict_bp,
        url_prefix="/api"
    )

    app.register_blueprint(
        analytics_bp,
        url_prefix="/api"
    )

    app.register_blueprint(
        simulation_bp,
        url_prefix="/api"
    )

    app.register_blueprint(
        report_bp,
        url_prefix="/api"
    )

    # ====================================
    # ROOT ROUTE
    # ====================================
    @app.route("/")
    def home():

        return jsonify({
            "project": "StressIntel PRO",
            "status": "running",
            "model": "XGBoost + SHAP",
            "version": "1.0"
        })

    # ====================================
    # HEALTH CHECK
    # ====================================
    @app.route("/health")
    def health():

        return jsonify({
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