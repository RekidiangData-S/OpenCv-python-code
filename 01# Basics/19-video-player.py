import cv2

def main():
    windowName = "OpenCV Video Player"
    cv2.namedWindow(windowName)
    
    filename = 'F:\Python-OpenCV3\Dataset\\Output.avi'
    cap = cv2.VideoCapture(filename)
    
    
    while (cap.isOpened()):
    
        ret, frame = cap.read()
        
        print(ret)
        
        if ret:
            lecture_speed = 33
            cv2.imshow(windowName, frame)
            if cv2.waitKey(lecture_speed) == 27:
                break
        else:
            break

    cv2.destroyAllWindows()    
    cap.release()

if __name__ == "__main__":
    main()