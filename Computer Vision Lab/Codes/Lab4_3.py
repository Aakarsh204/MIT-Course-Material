import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("C:\\Users\Student\Desktop\Aakarsh CV\Coins.jpg", cv2.IMREAD_GRAYSCALE)

laplacian_sharpened = cv2.Laplacian(img, cv2.CV_64F)

cv2.imshow('Sharpened', laplacian_sharpened)
cv2.imshow('Original', img)
if cv2.waitKey(0) == ord('s'):
    cv2.imwrite("C:\\Users\Student\Desktop\Aakarsh CV\CoinEdge.jpg", laplacian_sharpened)
cv2.destroyAllWindows()