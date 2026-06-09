import joblib

from config import Config


def load_model():

    model = joblib.load(
        Config.MODEL_PATH
    )

    return model


def load_scaler():

    scaler = joblib.load(
        Config.SCALER_PATH
    )

    return scaler


def load_label_encoder():

    label_encoder = joblib.load(
        Config.LABEL_ENCODER_PATH
    )

    return label_encoder