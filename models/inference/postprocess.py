from utils.constants import STRESS_LABELS


def decode_prediction(
    prediction,
    label_encoder
):

    decoded_label = label_encoder.inverse_transform(
        [prediction]
    )[0]

    if isinstance(decoded_label, str):
        return decoded_label

    return STRESS_LABELS.get(
        decoded_label,
        "Unknown"
    )


def extract_probability(probabilities):
    max_probability = max(probabilities)
    return round(float(max_probability), 4)