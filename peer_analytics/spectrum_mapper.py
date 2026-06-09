"""
Maps user data to a comparative stress spectrum.
"""

def map_to_spectrum(user_data):
    """
    Returns a position on the 0-100 spectrum based on multiple factors.
    """
    # Weighted calculation for spectrum placement
    # High anxiety, low sleep, high study hours push to the right (high)
    anxiety_norm = user_data.get("anxiety_score", 50) 
    sleep_norm = (12 - user_data.get("sleep_hours", 7)) * (100 / 8) # 4h -> 100, 12h -> 0
    study_norm = (user_data.get("study_hours", 6) / 12) * 100
    
    spectrum_pos = (anxiety_norm * 0.5 + sleep_norm * 0.3 + study_norm * 0.2)
    
    return min(100, max(0, round(spectrum_pos, 2)))
