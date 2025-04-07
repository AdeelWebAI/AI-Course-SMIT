First of all we have to add to init poetry in my poetry 
--- poetry init 

after if we have to add open cv library using the command 

--- poetry add opencv-python
after it we have to import the both libraries opencv and numpy using the command 

import cv2
import numpy as np

1. Basic Image Operations
Resize: cv2.resize(img, (width, height))
Convert to grayscale: cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
Save an image: cv2.imwrite("output.jpg", img)

2. Drawing Shapes on Images
In OpenCV, functions like cv2.rectangle(), cv2.circle(), and cv2.line() are used for drawing shapes on images. Each function takes specific parameters, which I’ll explain below:

cv2.rectangle()
cv2.rectangle(image, pt1, pt2, color, thickness)

Parameters:

image: The image on which to draw the rectangle.
pt1: The top-left corner of the rectangle (x, y).
pt2: The bottom-right corner of the rectangle (x, y).
color: The color of the rectangle (B, G, R) in a tuple, e.g., (255, 0, 0) for blue.
thickness: Thickness of the rectangle border (in pixels). Use -1 to fill the rectangle.
Example:

cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), 3)



cv2.circle()
This function is used to draw a circle on an image.

Syntax:

cv2.circle(image, center, radius, color, thickness)
Parameters:

image: The image on which to draw the circle.
center: The center of the circle (x, y).
radius: The radius of the circle in pixels.
color: The color of the circle (B, G, R) in a tuple.
thickness: The thickness of the circle border (in pixels). Use -1 to fill the circle.
Example:

cv2.circle(img, (150, 150), 50, (255, 0, 0), -1)



cv2.line()
This function is used to draw a line on an image.

Syntax:

cv2.line(image, pt1, pt2, color, thickness)
Parameters:

image: The image on which to draw the line.
pt1: The starting point of the line (x, y).
pt2: The ending point of the line (x, y).
color: The color of the line (B, G, R) in a tuple.
thickness: The thickness of the line in pixels.
Example:

cv2.line(img, (50, 50), (200, 200), (0, 0, 255), 2)
