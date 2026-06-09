"""
Module for face capture and frame preprocessing.
"""
import cv2
import numpy as np
import base64

def preprocess_face_frame(base64_string):
    """
    Decodes base64 image and prepares it for expression detection.
    """
    try:
        # Remove header if present
        if "," in base64_string:
            base64_string = base64_string.split(",")[1]
            
        img_data = base64.b64decode(base64_string)
        nparr = np.frombuffer(img_data, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if frame is None:
            return None
            
        # Convert to grayscale for typical detectors
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        return gray
    except Exception:
        return None
