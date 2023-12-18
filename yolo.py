from ultralytics import YOLO
import numpy as np
import pyautogui
import cv2
import time
from PIL import Image

model = YOLO('/Users/mehmet/PycharmProjects/okey/runs/detect/train7/weights/best.pt')

while True:
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        results = model(screenshot)
        boxes = results[0].boxes
        for box in boxes:
            print(box.xyxy)
            print(box.cls.item())
            print(box.conf.item())
        cv2.imshow("Real-Time Detection", screenshot)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
