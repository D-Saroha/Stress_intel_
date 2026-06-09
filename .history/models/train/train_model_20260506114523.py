import os
import joblib
import pandas as pd

from xgboost import XGBClassifier

from sklearn.model_selection import (
    train_test_split
)

from sklearn.preprocessing import (
    StandardScaler,
    LabelEncoder
)

from config import Config

from utils.constants import (
    FEATURE_COLUMNS,
    TARGET_COLUMN
)

from models.utils.feature_engineering import (
    create_engineered_features
)


def train_model():

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

    label_encoder = LabelEncoder()

    encoded_target = label_encoder.fit_transform(
        target
    )

    scaler = StandardScaler()

    scaled_features = scaler.fit_transform(
        features
    )

    X_train, X_test, y_train, y_test = train_test_split(
        scaled_features,
        encoded_target,
        test_size=Config.TEST_SIZE,
        random_state=Config.RANDOM_STATE,
        stratify=encoded_target
    )

    model = XGBClassifier(
        n_estimators=200,
        max_depth=6,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=Config.RANDOM_STATE
    )

    model.fit(
        X_train,
        y_train
    )

    os.makedirs(
        Config.MODEL_DIR,
        exist_ok=True
    )

    joblib.dump(
        model,
        Config.MODEL_PATH
    )

    joblib.dump(
        scaler,
        Config.SCALER_PATH
    )

    joblib.dump(
        label_encoder,
        Config.LABEL_ENCODER_PATH
    )

    print("Model training completed.")
    print(f"Model saved to: {Config.MODEL_PATH}")


if __name__ == "__main__":
    train_model()