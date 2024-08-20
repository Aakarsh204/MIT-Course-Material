import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("C:\\Users\\Student\\Desktop\\Aakarsh CV\\Tree.jpg")


img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Image', img1)

plt.figure(figsize=(20,20))

plt.subplot(221)
plt.title('Original Image')
plt.imshow(img)

img_hist = cv2.calcHist([img1], [0], None, [256], [0, 255])
plt.subplot(222)
plt.title('Original Histogram')
plt.plot(img_hist)

plt.subplot(223)
plt.hist(img1.ravel(), 256, [0, 255])
plt.title('Ravel Original')

final_img = cv2.equalizeHist(img1)

new_hist = cv2.calcHist([final_img], [0], None, [256], [0, 255])
plt.subplot(224)
plt.title('Equalized Histogram')
plt.plot(new_hist)

plt.show()

cv2.imshow('Equalized Image', final_img)
cv2.imwrite("C:\\Users\\Student\\Desktop\\Aakarsh CV\EqualizedTree.jpg", final_img)
cv2.waitKey(0)
cv2.destroyAllWindows()