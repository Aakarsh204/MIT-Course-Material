import cv2

img = cv2.imread("C:\\Users\\aakar\\Documents\\CVLab\\Images\\Blueberries.jpg")

angle = 45
h, w = img.shape[:2]

rotation_matrix = cv2.getRotationMatrix2D((w/2, h/2), angle, 1)
rotated_img = cv2.warpAffine(img, rotation_matrix, (w, h))

cv2.imshow("Rotated image", rotated_img)
cv2.waitKey(0)
#cv2.imwrite("C:\\Users\\aakar\\Documents\\CVLab\\Images\\RotatedBlueberries.jpg", rotated_img)
cv2.destroyAllWindows()