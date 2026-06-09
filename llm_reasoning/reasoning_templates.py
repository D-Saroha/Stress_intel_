"""
Reasoning templates for LLM-driven reports and journal analysis.
"""

JOURNAL_ANALYSIS_PROMPT = """
As a specialized AI Stress Analyst, analyze the following student journal entry:
"{journal_text}"

Identify:
1. Core emotional sentiment.
2. Hidden stressors (academic, social, physical).
3. Cognitive distortions (if any).

Provide a concise summary (max 3 sentences) and 2 specific recommendations based on the text.
"""

CLINICAL_INSIGHT_TEMPLATE = """
Based on the physiological biomarkers:
- {biomarkers}

And the ML model prediction of {prediction} ({probability}% confidence).

Generate a clinical interpretation focusing on the interaction between {top_features}.
"""

# Mapping feature names to human-readable explanations
FEATURE_EXPLANATIONS = {
    "sleep_hours": "Sleep duration is a critical recovery metric. Your current levels suggest {impact}.",
    "study_hours": "Academic workload intensity directly correlates with cognitive fatigue.",
    "heart_rate": "Elevated baseline heart rate may indicate sympathetic nervous system overactivity.",
    "anxiety_score": "Self-reported anxiety scores provide a baseline for psychological strain.",
    "physical_activity": "Movement is a primary buffer against cortisol buildup.",
    "screen_time": "High blue light exposure can disrupt circadian rhythms and mental clarity.",
    "diet_quality": "Nutritional intake directly impacts the body's resilience to stress.",
    "social_interaction": "Social bonding acts as a vital emotional buffer in student environments."
}
