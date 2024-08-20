import cv2
import numpy as np

img = cv2.imread("C:/Users/Student/Desktop/Aakarsh CV/Eagle.jpg")

scale_percent = 35
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

c = 45.6
log = c * (np.log(gray + 1))
log = log.astype(np.uint8)

cv2.imshow('LogEagle', log)

cv2.waitKey(0)
cv2.destroyAllWindows()