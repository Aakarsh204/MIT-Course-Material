import cv2
import numpy as np

img = cv2.imread("C:\\Users\Student\Desktop\Aakarsh CV\ManNoise.jpg", cv2.IMREAD_GRAYSCALE)
scale_percent = 250
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

median_filtered = cv2.medianBlur(img, 59)

cv2.imshow('Denoised', median_filtered)
cv2.imshow('Noisy', img)
if cv2.waitKey(0) == ord('s'):
    cv2.imwrite("C:\\Users\Student\Desktop\Aakarsh CV\ManDenoised.jpg", median_filtered)
cv2.destroyAllWindows()