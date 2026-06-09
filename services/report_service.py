"""
Service to orchestrate clinical report generation.
"""

from llm_reasoning.clinical_report import generate_clinical_report
from llm_reasoning.sentiment_analysis import analyze_journal_sentiment

def create_comprehensive_report(prediction_data, journal_text=None):
    """
    Orchestrates the creation of a clinical report, including journal analysis.
    """
    # 1. Generate base clinical report from biomarkers
    report_markdown = generate_clinical_report(
        prediction=prediction_data["prediction"],
        probability=prediction_data["probability"],
        feature_importance=prediction_data["feature_importance"],
        user_data=prediction_data.get("user_data", {})
    )
    
    # 2. Add Journal Analysis if available
    journal_insight = None
    if journal_text:
        journal_insight = analyze_journal_sentiment(journal_text)
        
        journal_section = f"\n## AI Deep Journal Insights\n"
        journal_section += f"**Sentiment:** {journal_insight['sentiment']}\n\n"
        journal_section += f"{journal_insight['summary']}\n\n"
        journal_section += "**Journal Recommendations:**\n"
        for rec in journal_insight['recommendations']:
            journal_section += f"- {rec}\n"
            
        # Append before disclaimer (which is usually at the end)
        report_parts = report_markdown.split("---")
        if len(report_parts) > 1:
            report_markdown = report_parts[0] + journal_section + "\n---\n" + report_parts[1]
        else:
            report_markdown += journal_section

    return {
        "report_md": report_markdown,
        "journal_insight": journal_insight
    }
