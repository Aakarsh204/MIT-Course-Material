import cv2

cap = cv2.VideoCapture('C:\\Users\Student\Desktop\Aakarsh CV\Rowing.mp4')

while cap.isOpened():
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end). Exiting ...")
        break

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

print("Frame Width : {}", cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("Frame Height : {}", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f"FPS : {cap.get(cv2.CAP_PROP_FPS)}")
print("Brightness : {}", cap.get(cv2.CAP_PROP_BRIGHTNESS))
print("Contrast : {}", cap.get(cv2.CAP_PROP_CONTRAST))
print("Saturation : {}", cap.get(cv2.CAP_PROP_SATURATION))
print("Saturation : {}", cap.get(cv2.CAP_PROP_HUE))

cap.release()
cv2.destroyAllWindows()