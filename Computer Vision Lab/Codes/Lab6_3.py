import numpy as np
import cv2

img = cv2.imread("C:\\Users\\aakar\\Documents\\CVLab\\Images\\Blueberries.jpg")

rows, cols = img.shape[:2]
M = np.float32([[1, 0, 100], [0, 1, 100]])
translated_img = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow("Image", translated_img)
cv2.waitKey(0)
#cv2.imwrite("C:\\Users\\aakar\\Documents\\CVLab\\Images\\TranslatedBlueberries.jpg", translated_img)
cv2.destroyAllWindows()