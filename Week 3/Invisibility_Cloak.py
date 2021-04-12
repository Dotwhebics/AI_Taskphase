# importing libraries
# OpenCV and Numpy for the main objective
import cv2 as cv
import numpy as np
# importing built in python module time for delay
import time

capture = cv.VideoCapture(0)  # VideoCapture object connected to webcam

# VideoWriter object to record frame by frame
fourcc = cv.VideoWriter_fourcc(*'XVID')
record = cv.VideoWriter('Invisibility_Cloak.avi', fourcc, 20.0, (640,480)) 

time.sleep(5)  # 5 seconds of relaxation for webcam to startup

for i in range(10):
    isTrue, background = capture.read()  # capturing background image 

# Loop to display the invisibility cloak in action!
while capture.isOpened():
    isTrue, frame = capture.read()

    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)  # convert in intaken BGR frame to HSV

    # Hue value of red is from 340 degrees to 20 degrees. We will split this range in two masks.

    # Hue range 0 degrees to 20 degrees (0 to 10 here cause uint8 can go only till 255)
    red1_lower = np.array([0, 120, 70])
    red1_upper = np.array([180, 255, 255])
    mask1 = cv.inRange(hsv_frame, red1_lower, red1_lower)  # Finding the red color in frame

    # Hue range 340 degrees to 360 degrees (170 to 180 here cause uint8 can go only till 255)
    red2_lower = np.array([170, 120, 70])
    red2_upper = np.array([180, 255, 255])
    mask2 = cv.inRange(hsv_frame, red2_lower, red2_upper)  # Finding the red color in frame 

    mask = mask1 + mask2  # combining the detected red pixels into single matrix 

    # Morphology transformations to reduce noise
    kernel = np.ones((3,3), np.uint8)
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel, iterations = 2)
    mask = cv.morphologyEx(mask, cv.MORPH_DILATE, kernel, iterations = 1)

    mask_inverted = cv.bitwise_not(mask)  # invertion of mask to find region without red 

    # Segment red area of current frame from the background image
    res1 = cv.bitwise_and(background, background, mask = mask)
    # Segment the area of current frame without red colour
    res2 = cv.bitwise_and(frame, frame, mask = mask_inverted)

    # Add the segments to obtain the desired display frame 
    final_frame = cv.addWeighted(res1, 1, res2, 1, 0) 

    # Write the output frame to recoring
    record.write(final_frame)
    
    # Display of the Live webcam feed 
    cv.imshow('Live Feed', final_frame)
    if cv.waitKey(1) == 27:  # stop the looping when esc is pressed
        break

capture.release()
record.release()
cv.destroyAllWindows()
