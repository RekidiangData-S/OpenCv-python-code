# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2

def main():
    
    imgpath = "F:\Python-OpenCV3\Dataset\\4.2.04.tiff"
    img = cv2.imread(imgpath)
    
    outpath = "F:\Python-OpenCV3\Dataset\\4.2.04.jpg"
    
    cv2.imshow('Lena', img)
    cv2.imwrite(outpath, img)
    cv2.waitKey(0)
    cv2.destroyWindow('Lena')
    
    
    
if __name__ == "__main__":
    main()