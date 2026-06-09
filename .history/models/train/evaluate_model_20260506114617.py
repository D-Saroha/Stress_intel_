import pandas as pd

from sklearn.model_selection import (
    train_test_split
)

from config import Config

from utils.constants import (
    TARGET_COLUMN
)

from models.utils.feature_engineering import (
    create_engineered_features
)

from models.utils.model_loader import (
    load_model,
    load_scaler,
    load_label_encoder
)

from models.utils.metrics import (
    calculate_classification_metrics
)


def evaluate_model():

    df = pd.read_csv(
        Config.RAW_DATA_PATH
    )

    df = create_engineered_features(
        df
    )

    target = df[TARGET_COLUMN]

    features = df.drop(
        columns=[TARGET_COLUMN]
    )

    label_encoder = load_label_encoder()

    encoded_target = label_encoder.transform(
        target
    )

    scaler = load_scaler()

    scaled_features = scaler.transform(
        features
    )

    X_train, X_test, y_train, y_test = train_test_split(
        scaled_features,
        encoded_target,
        test_size=Config.TEST_SIZE,
        random_state=Config.RANDOM_STATE,
        stratify=encoded_target
    )

    model = load_model()

    predictions = model.predict(
        X_test
    )

    metrics = calculate_classification_metrics(
        y_test,
        predictions
    )

    return metrics


if __name__ == "__main__":

    evaluation_metrics = evaluate_model()

    print(evaluation_metrics)