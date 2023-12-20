from ultralytics import YOLO
import numpy as np
import pyautogui
import cv2
import time

model = YOLO('/Users/mehmet/PycharmProjects/okey/runs/detect/train7/weights/best.pt')
model.train(data='/Users/mehmet/PycharmProjects/okey/okeyy-yolov8-v2/data.yaml', epochs=100)

"""while True:
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    results = model.track(screenshot, show=True, tracker="botsort.yaml")
    time.sleep(10)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break
"""
