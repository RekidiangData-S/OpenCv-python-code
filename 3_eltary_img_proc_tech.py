import cv2
cap = cv2.VideoCapture("airplanes.mp4")

while True:
    ret, frame = cap.read()
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    

    if ret:
        blurred =  cv2.GaussianBlur(frame, (21,21), 0)
        ret, thresh = cv2.threshold(frame, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(frame, None, iterations=2)


        cv2.imshow("Demo", frame)
        cv2.imshow("Blurred", blurred)
        cv2.imshow("Threshold", thresh)
        cv2.imshow("Dilated", dilated)
    else:
        break
    k = cv2.waitKey(10)
    if k == ord('q'):
        break
cv2.destroyAllWindows()