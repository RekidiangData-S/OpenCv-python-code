import cv2

def main():
    
    path = "E:\RkD_Projects\Python-OpenCV3\Dataset\\"
    imgpath1 =  path + "4.2.01.tiff"
    img1 = cv2.imread(imgpath1, 1)

    
    output = cv2.resize( img1, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA )
   
    
    cv2.imshow('Output', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 
if __name__ == "__main__":
    main()