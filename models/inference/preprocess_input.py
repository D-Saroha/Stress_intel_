import pandas as pd

from models.utils.feature_engineering import (
    create_engineered_features
)

from models.utils.model_loader import (
    load_scaler
)

from utils.constants import FEATURE_COLUMNS


def preprocess_input(data):
    # 1. Create base dataframe
    input_df = pd.DataFrame([{
        feature: data[feature]
        for feature in FEATURE_COLUMNS
    }])

    # 2. Add engineered features
    input_df = create_engineered_features(input_df)

    # 3. Ensure columns are in the EXACT order as training
    expected_columns = FEATURE_COLUMNS + [
        "sleep_study_ratio", 
        "activity_screen_balance", 
        "wellness_score", 
        "stress_risk_index"
    ]
    
    input_df = input_df[expected_columns]

    # 4. Scale features
    scaler = load_scaler()
    processed_features = scaler.transform(input_df)

    return processed_features