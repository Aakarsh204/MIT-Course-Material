import cv2
haar_cascade = 'cars.xml'
video = 'C:\\Users\\Student\\Desktop\\Aakarsh CV\\Cars.mp4'

cap = cv2.VideoCapture(video)
car_cascade = cv2.CascadeClassifier(haar_cascade)

while True:
    ret, img = cap.read()
    if not ret:
        break

    img = cv2.resize(img, (0, 0), fx=0.3, fy=0.3)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 255), 2)

    cv2.imshow('Video', img)

    if cv2.waitKey(1) == ord('s'):
        cv2.imwrite('C:\\Users\\Student\\Desktop\\Aakarsh CV\\CarDetected.jpg', img)
        break

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()