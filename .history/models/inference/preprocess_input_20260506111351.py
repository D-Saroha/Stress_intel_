import pandas as pd

from models.utils.feature_engineering import (
    create_engineered_features
)

from models.utils.model_loader import (
    load_scaler
)

from utils.constants import FEATURE_COLUMNS


def preprocess_input(data):

    input_df = pd.DataFrame([{
        feature: data[feature]
        for feature in FEATURE_COLUMNS
    }])

    input_df = create_engineered_features(
        input_df
    )

    scaler = load_scaler()

    processed_features = scaler.transform(
        input_df
    )

    return processed_features