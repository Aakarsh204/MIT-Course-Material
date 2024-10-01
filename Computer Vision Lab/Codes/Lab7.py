import cv2

img1 = cv2.imread("C:\\Users\Student\Desktop\Aakarsh CV\Guitar1.jpg", 0)
img2 = cv2.imread("C:\\Users\Student\Desktop\Aakarsh CV\guitar2.jpg", 0)
img1, img2 = cv2.resize(img1, (900, 1000)), cv2.resize(img2, (940, 520))

sift = cv2.SIFT_create()
keypoints1, descriptors1 = sift.detectAndCompute(img1, None)
keypoints2, descriptors2 = sift.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
matches = bf.match(descriptors1, descriptors2)

matches = sorted(matches, key = lambda x: x.distance)
matched_img = cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches[:50], img2, flags=2)

cv2.imshow("Matches", matched_img)
cv2.waitKey(0)
cv2.destroyAllWindows()