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
    predictions = model.predict(screenshot, confidence=40, overlap=30).json()

    detected_classes = []

    for prediction in predictions['predictions']:
        detected_class = prediction.get('class')

        if detected_class is not None:
            detected_classes.append(detected_class)
            #print(f"Detected Class: {detected_class}.")
        else:
            print("No 'class' key found in the prediction.")

    print("Detected Classes:", detected_classes)

    time.sleep(10)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break
