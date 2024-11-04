import cv2 
cap = cv2.VideoCapture(r'C:\Users\Dr Poonam Pandey\Desktop\Win28\PCV\video.mp4')
bg_subtract = cv2.createBackgroundSubtractorMOG2(history = 100 , varThreshold=50)
while cap.isOpened():
    ret , frame = cap.read()
    if not ret:
        break
    fg_mask = bg_subtract.apply(frame)
    _, thresh = cv2.threshold(fg_mask,200,255,cv2.THRESH_BINARY)
    contours , _ = cv2.findContours(thresh ,cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE )
    for contour in contours:
        if cv2.contourArea(contour)>1000:
            x,y,w,h = cv2.boundingRect(contour)
            cv2.rectangle(frame , (x,y) , (x+w,y+h),(0,255,0),2)
    cv2.imshow("object", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()