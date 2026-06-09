from utils.constants import FEATURE_COLUMNS


def validate_prediction_input(data):

    missing_fields = []

    for field in FEATURE_COLUMNS:

        if field not in data:
            missing_fields.append(field)

    return missing_fields