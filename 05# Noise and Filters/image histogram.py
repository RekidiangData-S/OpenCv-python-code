# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 22:20:42 2020

@author: rkies
"""

from skimage import io
import matplotlib.pyplot as plt

def main():
    
    path = "E:\RkD_Projects\Python-OpenCV3\Dataset\\"
    image =  path + "4.2.05.tiff"
    image = io.imread(image)
    
    _ = plt.hist(image.ravel(), bins = 256, color = 'orange', )
    _ = plt.hist(image[:, :, 0].ravel(), bins = 256, color = 'red', alpha = 0.5)
    _ = plt.hist(image[:, :, 1].ravel(), bins = 256, color = 'Green', alpha = 0.5)
    _ = plt.hist(image[:, :, 2].ravel(), bins = 256, color = 'Blue', alpha = 0.5)
    _ = plt.xlabel('Intensity Value')
    _ = plt.ylabel('Count')
    _ = plt.legend(['Total', 'Red_Channel', 'Green_Channel', 'Blue_Channel'])
    plt.show()
    
    
if __name__ == "__main__":
    main()
