import cv2
import numpy as np


image = cv2.imread('img.jpeg')
cv2.resize(image, (300, 600))
resized= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original', resized)


if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()