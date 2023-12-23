from roboflow import Roboflow
import numpy as np
import pyautogui
import cv2
import time

rf = Roboflow(api_key="lduRM9gO46HC7HCEGxTj")
project = rf.workspace().project("okeyy")
model = project.version(4).model

while True:
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    predictions = model.predict(screenshot, confidence=60, overlap=50).json()

    detected_classes = []

    for prediction in predictions['predictions']:
        detected_class = prediction.get('class')

        detected_classes.append(detected_class)
        #print(f"Detected Class: {detected_class}.")
        #confidence = prediction.get('confidence')

    print("Detected Classes:", detected_classes)

    time.sleep(10)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break
