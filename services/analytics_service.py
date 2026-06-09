"""
Service for peer analytics and cohort benchmarking.
"""

from peer_analytics.percentile_engine import calculate_percentile
from peer_analytics.cohort_analysis import get_cohort_stats
from peer_analytics.spectrum_mapper import map_to_spectrum

def get_peer_benchmarking(user_data):
    """
    Computes comparative metrics against the student cohort.
    """
    # 1. Calculate percentile based on anxiety score and heart rate
    percentile = calculate_percentile(user_data)
    
    # 2. Get cohort averages
    cohort_stats = get_cohort_stats()
    
    # 3. Map to spectrum position (0-100)
    spectrum_position = map_to_spectrum(user_data)
    
    return {
        "percentile": percentile,
        "cohort_stats": cohort_stats,
        "spectrum_position": spectrum_position,
        "comparison": {
            "user": user_data,
            "peer_avg": cohort_stats["averages"]
        }
    }
