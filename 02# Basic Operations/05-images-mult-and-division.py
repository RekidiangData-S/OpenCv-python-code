# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 08:44:50 2020

@author: rkies
"""

import cv2
import matplotlib.pyplot as plt

def main():
    
    path = "F:\Python-OpenCV3\Dataset\\"
    
    imgpath1 =  path + "4.2.01.tiff"
    imgpath2 =  path + "4.2.04.tiff"
    
    img1 = cv2.imread(imgpath1, 1)
    img2 = cv2.imread(imgpath2, 1)
    
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    
    mult = img1 + img2
    
    div = img1 / img2
   
    
    titles = ['Liquid Drop', 'Lena', 'multiplication', 'division']
    images = [img1, img2, mult, div]
    
    print()
    
    for i in range(4):
        plt.subplot(1, 4, i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()  
 
if __name__ == "__main__":
    main()