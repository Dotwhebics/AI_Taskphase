# Chrome Dino Game

The Dino game that apears in the Chrome browser whenever internet connection fails had become an iconic game. While connected to the internet the Dino game can be loaded using the url

> chrome://dino

To automate the Dino game the primary requirement is a library that can take screenshots of the screen and also have the capability of controlling the keyboard and mouse. Pyautogui is one such library used in this task. Pyautogui is capable with handling gui interactions using a keyboard and mouse following the python script. The rest of the image processing is handled by OpenCV.

We begin by taking a screenshot using the screenshot() function provided by pyautogui. This screenshot is saved to a file and read using opencv's imread() function. From here OpenCV is in charge of the decisions. 

By trial and error, pixel values have been obtained to draw a rectangle in front of the running dino. It is interesting to note that during the game, it is not the dino moving forward, rather the landscape moving backward. Thus it is possible to isolate a region right in front of the dino.

We calculate the white pixels inside this rectange. In case an obstacle approaches the dino, it will enter the rectangle area thus reducing the white pixels. This is an indication to jump. We again make use of pyautogui to press the space bar and jump.

The process of taking screenshots, reading it and deciding on when to jump is iterative. 