import os


class Config:
    """
    Central configuration file for StressIntel PRO.
    """

    # =========================
    # BASE SETTINGS
    # =========================
    SECRET_KEY = "stressintel-pro-secret-key"

    DEBUG = True

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # =========================
    # DATA PATHS
    # =========================
    DATA_DIR = os.path.join(BASE_DIR, "data")

    RAW_DATA_PATH = os.path.join(
        DATA_DIR,
        "raw",
        "StressLevelDataset.csv"
    )

    PROCESSED_DATA_PATH = os.path.join(
        DATA_DIR,
        "processed",
        "cleaned_data.csv"
    )

    # =========================
    # MODEL PATHS
    # =========================
    MODEL_DIR = os.path.join(BASE_DIR, "models", "saved")

    MODEL_PATH = os.path.join(
        MODEL_DIR,
        "stress_model.pkl"
    )

    SCALER_PATH = os.path.join(
        MODEL_DIR,
        "scaler.pkl"
    )

    LABEL_ENCODER_PATH = os.path.join(
        MODEL_DIR,
        "label_encoder.pkl"
    )

    # =========================
    # LOG PATHS
    # =========================
    LOG_DIR = os.path.join(BASE_DIR, "logs")

    APP_LOG_PATH = os.path.join(
        LOG_DIR,
        "app.log"
    )

    ERROR_LOG_PATH = os.path.join(
        LOG_DIR,
        "error.log"
    )

    # =========================
    # MODEL SETTINGS
    # =========================
    RANDOM_STATE = 42

    TEST_SIZE = 0.2

    MODEL_NAME = "XGBoost"

    # =========================
    # SHAP SETTINGS
    # =========================
    MAX_SHAP_FEATURES = 10

    # =========================
    # REPORT SETTINGS
    # =========================
    REPORT_DISCLAIMER = (
        "This system provides AI-generated stress analysis "
        "and is not a substitute for professional medical advice."
    )