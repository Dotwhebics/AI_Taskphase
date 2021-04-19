import numpy as np
import cv2 as cv
import time
import imutils
from collections import deque

capture = cv.VideoCapture(0)

path = deque(maxlen=60)

time.sleep(5)

while capture.isOpened():
    isTrue, frame = capture.read()

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower = np.array([110,50,50], np.uint8)
    upper = np.array([130,255,255], np.uint8)

    mask = cv.inRange(hsv, lower, upper)
    mask = cv.erode(mask, None, iterations = 5)
    mask = cv.dilate(mask, None, iterations = 5)

    contours = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    center = None

    if len(contours) > 0:
        c = max(contours, key = cv.contourArea)
        ((x,y), rad) = cv.minEnclosingCircle(c)
        M = cv.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"])) 

        if rad > 20:
            cv.circle(frame, (int(x), int(y)), int(rad),(0, 255, 255), 4)
            cv.circle(frame, center, 5, (0, 0, 255), -1)

    path.appendleft(center)

    for i in range(1, len(path)):
        if path[i-1] is None or path[i] is None:
            continue
        thickness = int(np.sqrt(20/float(i+1)) * 2.5)
        cv.line(frame, path[i-1], path[i], (0,0,255), thickness)

    cv.imshow("Live feed", frame)
    if cv.waitKey(1) == 27:
        break

capture.release()
cv.destroyAllWindows()