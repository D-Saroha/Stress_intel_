"""
Engine to calculate percentile rankings within the cohort.
"""
import pandas as pd
from config import Config

def calculate_percentile(user_data):
    """
    Calculates the percentile of the user's stress indicators.
    """
    try:
        df = pd.read_csv(Config.RAW_DATA_PATH)
        
        # We'll use anxiety_score as a proxy for the percentile ranking
        user_anxiety = user_data.get("anxiety_score", 50)
        
        # Count how many have lower anxiety
        lower_count = len(df[df['anxiety_score'] < user_anxiety])
        
        percentile = (lower_count / len(df)) * 100
        return round(percentile, 1)
    except Exception:
        return 50.0 # Default fallback
