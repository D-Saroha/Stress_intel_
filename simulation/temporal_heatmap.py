"""
Generates data for the weekly risk density heatmap.
"""
import random

def generate_risk_heatmap(data):
    """
    Generates a 24 (hours) x 7 (days) grid of risk levels (0-3).
    Risk is calculated based on study hours and anxiety scores.
    """
    heatmap = []
    
    anxiety_base = data.get("anxiety_score", 50)
    study_hours = data.get("study_hours", 6)
    
    # 0: Monday, ..., 6: Sunday
    for day in range(7):
        day_data = []
        for hour in range(24):
            # Base risk from hour of day (peaks during study hours 9-17 and late night)
            hour_risk = 0
            if 9 <= hour <= 17:
                hour_risk = (study_hours / 10) * 2
            elif hour >= 22 or hour <= 2:
                hour_risk = (anxiety_base / 100) * 3
            
            # Weekend reduction
            if day >= 5:
                hour_risk *= 0.6
                
            # Add randomness
            final_risk = min(3, max(0, int(hour_risk + random.uniform(-0.5, 0.5))))
            day_data.append(final_risk)
        heatmap.append(day_data)
        
    return heatmap
