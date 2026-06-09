from flask import Blueprint, jsonify, request
import base64
import cv2
import numpy as np
from llm_reasoning.ollama_service import OllamaService
from models.research_intelligence import ResearchIntelligenceModel
from models.visual_intelligence import VisualIntelligenceModel

research_bp = Blueprint("research_bp", __name__)
ollama = OllamaService()
research_model = ResearchIntelligenceModel()
visual_model = VisualIntelligenceModel()

@research_bp.route("/research/analyze", methods=["POST"])
def research_analyze():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "error": "No data provided"}), 400
            
        # 1. Get Textual Insight (Hybrid Approach)
        # Try Ollama first
        insight = ollama.analyze_research_data(data, "Institutional Risk Profile")
        
        # Check if Ollama failed
        llm_failed = False
        if any(err in insight for err in ["Connection Failed", "Ollama Error", "CLI Error"]):
            llm_failed = True
            # Fallback to Deterministic Research Intelligence Model
            insight = research_model.analyze(data)
            insight += "\n\n*(Note: Analysis generated via Deterministic Research Intelligence Model due to local LLM unavailability)*"

        # 2. Visual Impact Analysis (If image provided)
        visual_data = None
        image_b64 = data.get("image")
        if image_b64:
            try:
                # Decode image
                if "," in image_b64:
                    image_b64 = image_b64.split(",")[1]
                img_data = base64.b64decode(image_b64)
                nparr = np.frombuffer(img_data, np.uint8)
                frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                
                if frame is not None:
                    # Process via Visual Intelligence Model
                    annotated_frame, metadata = visual_model.classify_image_impact(frame)
                    
                    # Encode back to base64
                    _, buffer = cv2.imencode('.jpg', annotated_frame)
                    annotated_b64 = base64.b64encode(buffer).decode('utf-8')
                    
                    visual_data = {
                        "annotated_image": f"data:image/jpeg;base64,{annotated_b64}",
                        "metadata": metadata
                    }
            except Exception as ve:
                print(f"Visual Analysis Error: {str(ve)}")

        return jsonify({
            "success": True,
            "insight": insight,
            "llm_active": not llm_failed,
            "visual_analysis": visual_data
        })

    except Exception as e:
        return jsonify({
            "success": False, 
            "error": f"Internal Server Error: {str(e)}"
        }), 500
