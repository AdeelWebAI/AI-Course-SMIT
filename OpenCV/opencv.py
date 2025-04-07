import cv2
import numpy as np


image = cv2.imread('img.jpeg')
cv2.resize(image, (300, 600))
resized= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# cv2.imwrite('scaled.jpg', resized)

# cv2.rectangle(resized, (110, 110), (400, 400), (255, 0, 0), 5)
# cv2.circle(resized, (110, 110),100, (255, 0, 0), 5)
# cv2.line(resized, (50, 50), (250, 250), (555, 555, 0), 5)


cv2.imshow('Original', resized)


if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()