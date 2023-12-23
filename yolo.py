from ultralytics import YOLO
import numpy as np
import pyautogui
import cv2
import time

model = YOLO('/Users/mehmet/PycharmProjects/okey/runs/detect/train/weights/best.pt')

while True:
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    results = model.track(screenshot, show=False, tracker="bytetrack.yaml")

    time.sleep(10)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break



#model.train(data='/Users/mehmet/PycharmProjects/okey/okeyy-yolov8-v2/data.yaml', epochs=100)
"""    results_object = results[0]
    detected_objects = results_object.names
    for class_id, class_name in detected_objects.items():
        print(f"Class ID: {class_id}, Class Name: {class_name}")
"""