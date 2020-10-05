# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 22:14:36 2020

@author: rkies
"""
from skimage import io
import matplotlib.pyplot as plt

def main():
    
    path = "E:\RkD_Projects\Python-OpenCV3\Dataset\\"
    imgpath =  path + "4.2.05.tiff"
    
    
    image = io.imread(imgpath)
    ax = plt.hist(image.ravel(), bins = 256)
    plt.show()
    
    
if __name__ == "__main__":
    main()

