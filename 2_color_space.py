import cv2
cap = cv2.VideoCapture("airplanes.mp4")

while True:
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    if ret:
        cv2.imshow("BGR", frame)
        cv2.imshow("Gray", gray)
        cv2.imshow("HSV", hsv)
        cv2.imshow("RGB", rgb)
    else:
        break
    k = cv2.waitKey(10)
    if k == ord('q'):
        break
cv2.destroyAllWindows()