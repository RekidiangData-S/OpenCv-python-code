import cv2
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow("Demo", frame)
    else:
        break
    k = cv2.waitKey(10)
    if k == ord('q'):
        break
cv2.destroyAllWindows()
