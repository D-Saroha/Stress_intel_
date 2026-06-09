from models.inference.preprocess_input import (
    preprocess_input
)

from models.inference.postprocess import (
    decode_prediction,
    extract_probability
)

from models.utils.model_loader import (
    load_model,
    load_label_encoder
)


model = load_model()

label_encoder = load_label_encoder()


def predict_stress(data):

    processed_features = preprocess_input(
        data
    )

    prediction_encoded = model.predict(
        processed_features
    )[0]

    prediction_probabilities = model.predict_proba(
        processed_features
    )[0]

    prediction = decode_prediction(
        prediction_encoded,
        label_encoder
    )

    probability = extract_probability(
        prediction_probabilities
    )

    return {
        "prediction": prediction,
        "probability": probability,
        "processed_features": processed_features
    }