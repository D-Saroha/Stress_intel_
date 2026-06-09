import os
import joblib
import pandas as pd
import numpy as np

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
    # Load original dataset
    df = pd.read_csv(Config.RAW_DATA_PATH)
    
    # Mapping original columns to UI-friendly feature names
    mapping = {
        "anxiety_level": "anxiety_score",
        "sleep_quality": "sleep_hours",
        "study_load": "study_hours",
        "social_support": "social_interaction",
        "extracurricular_activities": "physical_activity",
        "future_career_concerns": "screen_time",
        "academic_performance": "diet_quality",
        "blood_pressure": "heart_rate"
    }
    
    # Check if we need to rename (in case it's already mapped)
    available_mapping = {k: v for k, v in mapping.items() if k in df.columns}
    df = df.rename(columns=available_mapping)
    
    # Ensure all required features are present
    for col in FEATURE_COLUMNS:
        if col not in df.columns:
            # Fallback for missing features in mapping
            df[col] = 0
            
    df = create_engineered_features(df)

    target = df[TARGET_COLUMN]
    features = df[FEATURE_COLUMNS + ["sleep_study_ratio", "activity_screen_balance", "wellness_score", "stress_risk_index"]]

    # Standardize target mapping (0=Low, 1=Medium, 2=High)
    # The dataset uses 0, 1, 2 already, but we ensure consistency
    encoded_target = target.astype(int)
    
    # Save a dummy label encoder for compatibility with existing predictor
    label_encoder = LabelEncoder()
    label_encoder.classes_ = np.array(["Low", "Medium", "High"])

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

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

    model.fit(X_train, y_train)

    os.makedirs(Config.MODEL_DIR, exist_ok=True)
    joblib.dump(model, Config.MODEL_PATH)
    joblib.dump(scaler, Config.SCALER_PATH)
    joblib.dump(label_encoder, Config.LABEL_ENCODER_PATH)

    print(f"Model training completed using {Config.RAW_DATA_PATH}.")
    print(f"Model saved to: {Config.MODEL_PATH}")



if __name__ == "__main__":
    train_model()