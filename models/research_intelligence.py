import json

class ResearchIntelligenceModel:
    def __init__(self):
        self.axes = {
            "Psychological": ["anxiety_level", "self_esteem", "depression", "mental_health_history"],
            "Academic": ["study_load", "academic_performance", "teacher_student_relationship", "future_career_concerns"],
            "Environmental": ["living_conditions", "safety", "basic_needs", "noise_level"],
            "Social": ["social_support", "peer_pressure", "bullying", "extracurricular_activities"],
            "Physiological": ["headache", "blood_pressure", "sleep_quality", "breathing_problem"]
        }

    def analyze(self, data):
        """
        Performs a multi-axial heuristic analysis of the 21-parameter dataset.
        Returns a structured clinical insight.
        """
        insights = []
        risks = []

        # 1. Axis-Specific Analysis
        # Psychological
        anxiety = int(data.get("anxiety_level", 0))
        depression = int(data.get("depression", 0))
        mh_history = int(data.get("mental_health_history", 0))
        
        if anxiety > 70 or depression > 60:
            risks.append("Critical Psychological Distress")
            insights.append("High anxiety/depression markers suggest immediate clinical intervention may be required.")
        elif mh_history == 1:
            insights.append("Presence of mental health history increases vulnerability to current stressors.")

        # Academic
        load = int(data.get("study_load", 0))
        perf = int(data.get("academic_performance", 0))
        if load > 8 and perf < 4:
            risks.append("Academic Burnout")
            insights.append("Significant mismatch between high study load and low performance indicates cognitive overload.")

        # Environmental
        safety = int(data.get("safety", 0))
        noise = int(data.get("noise_level", 0))
        if safety < 4:
            risks.append("Environmental Instability")
            insights.append("Low environmental safety is a major compounding factor for systemic stress.")

        # Physiological
        sleep = int(data.get("sleep_quality", 0))
        headache = int(data.get("headache", 0))
        if sleep < 3:
            insights.append("Severe sleep deprivation is likely impairing executive function and emotional regulation.")

        # 2. Synthesis
        risk_profile = " / ".join(risks) if risks else "Stable Research Profile"
        
        report = f"""[HEURISTIC CLINICAL REPORT]
Risk Profile: {risk_profile}

The diagnostic data indicates a multi-factorial stress response. { " ".join(insights[:3]) } 

Institutional recommendation: Implementation of targeted psychological support and academic workload optimization. This profile suggests a {'high' if risks else 'moderate'} probability of academic regression if left unaddressed."""

        return report.strip()
