import pandas as pd

from xgboost import XGBClassifier

from sklearn.model_selection import (
    train_test_split,
    GridSearchCV
)

from sklearn.preprocessing import (
    StandardScaler,
    LabelEncoder
)

from config import Config

from utils.constants import (
    TARGET_COLUMN
)

from models.utils.feature_engineering import (
    create_engineered_features
)


def perform_hyperparameter_tuning():

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
        random_state=Config.RANDOM_STATE
    )

    parameter_grid = {
        "n_estimators": [100, 200],
        "max_depth": [4, 6, 8],
        "learning_rate": [0.01, 0.05, 0.1],
        "subsample": [0.8, 1.0]
    }

    grid_search = GridSearchCV(
        estimator=model,
        param_grid=parameter_grid,
        cv=3,
        scoring="accuracy",
        verbose=1,
        n_jobs=-1
    )

    grid_search.fit(
        X_train,
        y_train
    )

    print("Best Parameters:")
    print(grid_search.best_params_)

    print("\nBest Score:")
    print(grid_search.best_score_)


if __name__ == "__main__":
    perform_hyperparameter_tuning()