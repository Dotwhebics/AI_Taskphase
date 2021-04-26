import cv2 as cv
import numpy as np
import pyautogui as auto
import time

auto.click(480, 540)
auto.keyDown('space')
time.sleep(0.05)
auto.keyUp('space')

time.sleep(2)


ss = auto.screenshot('screenshot.png')
pic = cv.imread('screenshot.png')
height = int(np.size(pic, 0) * 0.6)
width = int(np.size(pic, 1) * 0.6)
pic = cv.resize(pic, (width, height))
cv.rectangle(pic, (75,225), (150,260), (255,0,0), 2)
img = pic[225:260, 75:150]
measure = np.sum(img == 255)

while True:
    ss = auto.screenshot('screenshot.png')
    pic = cv.imread('screenshot.png')
    
    height = int(np.size(pic, 0) * 0.6)
    width = int(np.size(pic, 1) * 0.6)
    pic = cv.resize(pic, (width, height))
    cv.rectangle(pic, (75,225), (150,260), (255,0,0), 2)
    width = int(width / 2)
    pic = pic[0:height, 0:width]
    img = pic[225:260, 75:150]
    white = np.sum(img == 255)
    
    # print(measure, white)

    if measure > white:
        auto.keyDown('space')
        time.sleep(0.05)
        # print("jump")
        auto.keyUp('space')
        # time.sleep(0.1)
        
    cv.imshow("Box", pic)                   
    if cv.waitKey(1) == 27:
        break