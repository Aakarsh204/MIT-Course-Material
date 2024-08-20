import cv2
import numpy as np

img = cv2.imread("C:\\Users\Student\Desktop\Aakarsh CV\Eagle.jpg")

scale_percent = 35
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
cv2.imshow('Eagle', resized)

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Eagle', gray)

neg = cv2.bitwise_not(gray)
cv2.imshow('Negative Eagle', neg)

cv2.waitKey(0)
cv2.destroyAllWindows()