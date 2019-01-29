import cv2 as cv
import numpy as np
import math
import pickle

def loading() :
    const = {
        "mask" :  [],
        "circles" :  [],
    }

    for i in range(190, 201, 1) :
        print(str(i) +"/200")
        path = 'Mask/mask'+str(i)+".png"
        img3 = cv.imread(path, 0)
        width, height = img3.shape[:2]
        ret, mask = cv.threshold(img3, 170, 255, cv.THRESH_BINARY)
        circles = cv.HoughCircles(mask, cv.HOUGH_GRADIENT, 1, 100, param1=50, param2=10, minRadius=38, maxRadius=50)

        const["mask"] = mask
        const["circles"] = circles

        path = 'Mask/mask'+str(i)+".pckl"
        f = open(path, 'wb')
        pickle.dump(const, f)
        f.close()
