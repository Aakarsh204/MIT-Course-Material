import numpy as np
import cv2

img = cv2.imread("C:\\Users\\aakar\\Documents\\CVLab\\Images\\Blueberries.jpg")

rows, cols = img.shape[:2]
M = np.float32([[1, 0.5, 0], [0, 1, 0], [0, 0, 1]])
sheared_img = cv2.warpPerspective(img, M, (int(cols*1.2), int(rows*1.2)))

cv2.imshow("Image", sheared_img)
cv2.waitKey(0)
#cv2.imwrite("C:\\Users\\aakar\\Documents\\CVLab\\Images\\ShearedBlueberries.jpg", sheared_img)
cv2.destroyAllWindows()