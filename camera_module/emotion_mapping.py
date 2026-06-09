"""
Maps detected expressions to stress indicators.
"""

EMOTION_STRESS_WEIGHTS = {
    "Anger": 0.8,
    "Fear": 0.9,
    "Sadness": 0.6,
    "Disgust": 0.5,
    "Surprise": 0.3,
    "Happiness": -0.4,
    "Neutral": 0.0
}

def get_stress_from_emotion(emotion):
    return EMOTION_STRESS_WEIGHTS.get(emotion, 0.0)
