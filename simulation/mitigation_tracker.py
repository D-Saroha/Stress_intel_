"""
Tracks impact of mitigation actions.
"""

def calculate_mitigation_impact(completed_actions):
    """
    Calculates estimated reduction in stress score based on actions.
    """
    action_weights = {
        "mit-1": 0.15, # Digital Detox
        "mit-2": 0.10, # Breathing
        "mit-3": 0.20, # Sleep Hygiene
        "mit-4": 0.10, # Stretching
        "mit-5": 0.05  # Hydration
    }
    
    total_reduction = sum(action_weights.get(action, 0) for action in completed_actions)
    
    return round(total_reduction, 2)
