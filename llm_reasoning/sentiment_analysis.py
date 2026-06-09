"""
LLM-based sentiment and reasoning for the AI Deep Journal.
"""

from llm_reasoning.reasoning_templates import JOURNAL_ANALYSIS_PROMPT

def analyze_journal_sentiment(journal_text):
    """
    Simulates LLM-based journal analysis.
    In production, this would call an API like Gemini or OpenAI.
    """
    if not journal_text or len(journal_text.strip()) < 5:
        return {
            "sentiment": "Neutral",
            "summary": "Insufficient data to perform deep sentiment analysis.",
            "recommendations": ["Try writing a more detailed journal entry for better insights."]
        }

    # Simulation Logic based on keywords
    text_lower = journal_text.lower()
    
    if any(word in text_lower for word in ["tired", "exhausted", "sleep", "rest"]):
        sentiment = "Fatigued"
        summary = "The entry indicates significant physical exhaustion and possible sleep debt impacting mental clarity."
        recs = ["Implement a strict sleep hygiene protocol.", "Reduce late-night screen exposure."]
    elif any(word in text_lower for word in ["exam", "test", "study", "deadline", "assignment"]):
        sentiment = "Anxious (Academic)"
        summary = "Academic pressure is the primary driver of current stress levels, centered around upcoming deadlines."
        recs = ["Utilize time-blocking for assignments.", "Break large tasks into smaller milestones."]
    elif any(word in text_lower for word in ["lonely", "alone", "friend", "social"]):
        sentiment = "Socially Isolated"
        summary = "A lack of social connection is exacerbating feelings of stress and emotional vulnerability."
        recs = ["Schedule a brief social interaction today.", "Consider group study sessions."]
    else:
        sentiment = "Mildly Stressed"
        summary = "General feelings of being overwhelmed are present, though no specific source is dominant."
        recs = ["Practice 5 minutes of mindful breathing.", "Log your next mood spike for pattern matching."]

    return {
        "sentiment": sentiment,
        "summary": summary,
        "recommendations": recs
    }
