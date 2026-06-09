import json
from models.research_intelligence import ResearchIntelligenceModel
from models.visual_intelligence import VisualIntelligenceModel
import numpy as np
import cv2

def test_models():
    print("Testing ResearchIntelligenceModel...")
    rm = ResearchIntelligenceModel()
    test_data = {
        "anxiety_level": 85,
        "depression": 20,
        "study_load": 9,
        "academic_performance": 3,
        "safety": 8,
        "sleep_quality": 2
    }
    insight = rm.analyze(test_data)
    print("Insight Generated:")
    print(insight)
    assert "Critical Psychological Distress" in insight or "Academic Burnout" in insight
    
    print("\nTesting VisualIntelligenceModel...")
    vm = VisualIntelligenceModel()
    # Create a dummy frame (black image)
    frame = np.zeros((480, 640, 3), dtype=np.uint8)
    # Draw a white circle to represent a 'face' (though Haar won't detect it)
    cv2.circle(frame, (320, 240), 100, (255, 255, 255), -1)
    
    annotated, meta = vm.classify_image_impact(frame)
    print("Metadata Generated:", meta)
    assert "impact_score" in meta
    
    print("\nAll tests passed!")

if __name__ == "__main__":
    test_models()
