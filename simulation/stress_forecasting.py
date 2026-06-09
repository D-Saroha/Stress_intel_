"""
Logic for stress forecasting based on lifestyle modifications.
"""
import numpy as np

def forecast_stress_levels(data):
    """
    Predicts stress trajectory over a 7-day period.
    Simulates how current biomarkers would evolve under specific conditions.
    """
    # Base stress score derived from biomarkers
    base_stress = (data.get("anxiety_score", 50) * 0.4 + 
                   (120 - data.get("sleep_hours", 7) * 10) * 0.3 + 
                   data.get("study_hours", 6) * 5) / 10
    
    # Generate 7 points of trajectory
    trajectory = []
    current_stress = base_stress
    
    # Factors that influence daily change
    sleep_impact = (8 - data.get("sleep_hours", 7)) * 0.5
    study_impact = (data.get("study_hours", 6) - 5) * 0.2
    activity_impact = (30 - data.get("physical_activity", 30)) * 0.01
    
    daily_delta = sleep_impact + study_impact + activity_impact
    
    for i in range(7):
        # Add some randomness for realism
        noise = np.random.normal(0, 0.2)
        current_stress = max(0, min(10, current_stress + daily_delta + noise))
        trajectory.append(round(current_stress, 2))
        
    return trajectory
