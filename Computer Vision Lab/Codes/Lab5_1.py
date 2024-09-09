import cv2

img = cv2.imread("C:\\Users\\aakar\\Documents\\Image Processing\\Data\\MathWorks Images\\coins1.jpg")
scale_percent = 35
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray,(7,7),0)

sobelx = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=3)
sobel_edges = cv2.bitwise_or(sobelx, sobely)

canny_edges = cv2.Canny(blur, 100, 200)

cv2.imshow("Canny Edges", canny_edges)
cv2.imshow("Sobel Edges", sobel_edges)
cv2.waitKey(0)
#cv2.imwrite("C:\\Users\\aakar\\Documents\\CVLab\\Images\\CannyCoins.jpg", canny_edges)
#cv2.imwrite("C:\\Users\\aakar\\Documents\\CVLab\\Images\\SobelCoins.jpg", sobel_edges)
cv2.destroyAllWindows()