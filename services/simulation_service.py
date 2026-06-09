"""
Service for stress forecasting and simulation lab.
"""

from simulation.stress_forecasting import forecast_stress_levels
from simulation.temporal_heatmap import generate_risk_heatmap

def run_simulation(base_data, modifications):
    """
    Runs a stress forecast based on modified parameters.
    """
    # Merge base data with modifications
    simulated_data = base_data.copy()
    simulated_data.update(modifications)
    
    # Forecast stress trajectory (e.g. over 7 days)
    trajectory = forecast_stress_levels(simulated_data)
    
    # Generate temporal heatmap data for these parameters
    heatmap = generate_risk_heatmap(simulated_data)
    
    return {
        "trajectory": trajectory,
        "heatmap": heatmap,
        "summary": "Simulation engine initialized with modified parameters."
    }
