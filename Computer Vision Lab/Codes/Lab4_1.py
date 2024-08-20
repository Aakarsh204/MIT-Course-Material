import cv2
import numpy as np

img = cv2.imread("C:\\Users\Student\Desktop\Aakarsh CV\MouseNoise.jpg", cv2.IMREAD_GRAYSCALE)
scale_percent = 150
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

kernel = np.ones((5, 5), np.float32) / 25

mean_filtered = cv2.filter2D(img, -1, kernel)
laplacian_sharpened = cv2.Laplacian(mean_filtered, cv2.CV_64F)

cv2.imshow('Sharpened', laplacian_sharpened)
cv2.imshow('Denoised', mean_filtered)
cv2.imshow('Noisy', img)
if cv2.waitKey(0) == ord('s'):
    cv2.imwrite("C:\\Users\Student\Desktop\Aakarsh CV\MouseDenoised.jpg", mean_filtered)
cv2.destroyAllWindows()