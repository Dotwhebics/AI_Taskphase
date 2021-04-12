# OpenCV

OpenCV stands for Open Source Computer Vision library. This is an Open Source developed library. The OpenCV project begain back in 1999 under the initiative of Intel Research. The library is written mainly using C++.

The library provides high performance computer vision function for the programming languages C++, Python and Java which basically makes it a very coomonly used library as these languages contitute the maximum chunk of users.  It is also available for MATLAB/OCTAVE which are high performance numerical computing softwares.

OpenCV relies on another numberical computing library called NumPy (Numberical Python). The image pixels are stored as martrices. NumPy provides data types that indicate that the stored values belog to an image (like np.uint8). Since OpenCV is connected closely to NumPy, it also provides an easier way to integrate with libraries like SciPy (Scientific Python) and Matplotlib.

## Masking and Invisibility Cloak
Masking is a way of combining two images covering parts of one image by another, or just extracting a part of an image.
In OpenCV, masking is done with the help of the bitwise operators that the library offers. When bitwise operations are performed on two images, bascially the pixel value matrices of the images are operated on to generate a result matrix that holds the pixel values of the output image.

In the task of Making an Invisibility Cloak, we first capture the background and then mask it with the live fed frame obtained from the webcam. The mask frame keeps changing as the loop runs iteratively until it encounters a break. The background image remains a single frame.

First, we capture the background image iteratively. The last captured image is stored as background. Then we begin taking live feed from the webcam and whenever red colour is detected (identified as mask as it lies in the specified HSV values). This area (red area) is cut out from the present frame and the blanked out area is filled with the captured background frame. The background has to have absolutely no motion for the desired affect to look real.

PS : The camera does not see through the person in the task. It is just output of some computation.