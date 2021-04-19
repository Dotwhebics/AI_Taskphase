# Object Detection

## Contours

Contours can be condidered to be edges from a programming point of view. Mathematically speaking contours and edges are slighly different. Contours can be thought of as lines joining points along the boundary.

In OpenCV the cv.findContours() function can be used to obtain the contours and the cv.drawContours can be used to draw the detected contours on an image.

## Hough Circles

OpenCV has a function, cv.HoughCircles to find the circles in an image. In the case of an video, this can be done frame by frame. Circles are detected using Hough Gradient Mathod that uses the information of the edge gradients. The detected circles are recorded using x-coordinate, y-coordinate and radius in that order. Each element of the matrix returned represents one circle and saves this data.

## Colour Space Transformations

Any image can be visualised or mathematically described in a huge number of ways. Each such representation is called a colour space. For example, it can be represented using one colour channel (grayscale) or three channels (BGR, HSV) etc. OpenCV reads images by default as BGR irrespective of the colour channel of the input image. 

The cv.cvtColor() function can be used to convert a passed image from one colour soace to another.

## Ball Detection

In the ball detection task, we first create a capture object of cv.VideoCapture() and read frames from the webcam. A mask with a desired colour range is created to segment out the ball. Then we find the contours and these help in drawing a boundary and centre. We also create a deque. The difference between a queue and a deque is the fact that appending in a queue is intuitively done at the end. But deque is a double ending queue so appending can be done from both sides. We save successive centre positions in the deque so the path can be traced.

![Ball Detection](https://user-images.githubusercontent.com/72495927/115219846-86a8bf80-a125-11eb-918a-088097f32595.gif)