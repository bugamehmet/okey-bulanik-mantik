import pyautogui
from roboflow import Roboflow
import numpy as np
import cv2

def taslari_bul(api_key, project_name, model_version, confidence_threshold=60, overlap_threshold=50):
    rf = Roboflow(api_key=api_key)
    project = rf.workspace().project(project_name)
    model = project.version(model_version).model

    screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR)
    predictions = model.predict(screenshot, confidence=confidence_threshold, overlap=overlap_threshold).json()

    detected_classes = [prediction.get('class') for prediction in predictions.get('predictions', [])]
    return detected_classes
