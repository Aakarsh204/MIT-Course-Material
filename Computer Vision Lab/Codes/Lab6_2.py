import cv2

img = cv2.imread("C:\\Users\\aakar\\Documents\\CVLab\\Images\\Blueberries.jpg")

rows, cols = img.shape[:2]
small_img = cv2.resize(img, (250, 250), interpolation=cv2.INTER_AREA)
cv2.imshow("Small Image", small_img)

large_img = cv2.resize(img, None, fx=1.3, fy=1.3, interpolation=cv2.INTER_CUBIC)
cv2.imshow("Large Image", large_img)
cv2.waitKey(0)
cv2.destroyAllWindows()