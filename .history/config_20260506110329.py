import os


class Config:
    SECRET_KEY = "stressintel-secret-key"

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    DATA_DIR = os.path.join(BASE_DIR, "data")
    MODEL_DIR = os.path.join(BASE_DIR, "models", "saved")

    MODEL_PATH = os.path.join(MODEL_DIR, "stress_model.pkl")
    SCALER_PATH = os.path.join(MODEL_DIR, "scaler.pkl")
    LABEL_ENCODER_PATH = os.path.join(MODEL_DIR, "label_encoder.pkl")

    DEBUG = True