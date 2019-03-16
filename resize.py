# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np
import math
from PIL import Image, ImageStat


"""
This file contains functions to crop the white borders around the image

"""



def distaucarre(point, org=(0, 0)):
    return (math.pow(point[0] - org[0], 2) + math.pow(point[1] - org[1], 2))


# given a contour, returns the area of the smallest enclosing rectangle
def areaCnt(contour):
     rect = cv.minAreaRect(contour)
     return rect[1][0]*rect[1][1]



# calculates the brightness of an image
def brightness( cv_im ):
   cv_im = cv.cvtColor(cv_im,cv.COLOR_BGR2RGB)
   pil_im = Image.fromarray(cv_im)
   stat = ImageStat.Stat(pil_im)
   return stat.mean[0]



# true if the image is upside down
def isUpsideDown(img):
    width, height = img.shape[:2]
    
    # select a part of the image which is normally white
    y=int(height*0.08)
    x=int(width*0.2)
    h=int(height*0.05)
    w=int(width*0.2)
    sub_image = img[y:y+h, x:x+w]
    
    # if its brightness is less than the limit, it is upside down
    limit = 240
    return brightness(sub_image) < limit




# main function : crop the image to the enclosing rectangle (the size has already been normalized in p2j.py)
def resize(img):
    width, height = img.shape[:2]

    blurred = cv.GaussianBlur(img, (3, 3), 0)

    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 3, 2)
    
    #find all contours in the image
    major = cv.__version__.split('.')[0]
    if major == '3':
        _, contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    else:
        contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)


    #only keep the contour of maximal area to get rid of all marks outside of the rectangle 
    biggestContour=max(contours, key=lambda p: areaCnt(p))

    # minimal enclosing rectangle
    rect = cv.minAreaRect(biggestContour)
    
    #si il est a un angle faible on le garde (si l'angle est eleve le rectangle est souvent trop grand)
    angle=rect[2]
    #nb de degres d'ecart a l'horizontale autorise (eleve si la resolution est elevee)
    marge=7 
    if abs(angle) < marge or angle < -90+marge:
        #print('droit')
        box = cv.boxPoints(rect)
        
    #sinon on recherche les coins du contour (cette methode ne marche pas bien si l'angle est trop faible ou la resolution trop faible)
    else:
        a=min(biggestContour, key=lambda p: p[0][0])
        b=min(biggestContour, key=lambda p: p[0][1])
        c=max(biggestContour, key=lambda p: p[0][0])
        d=max(biggestContour, key=lambda p: p[0][1])
        box=[a[0].tolist(),b[0].tolist(),c[0].tolist(),d[0].tolist()]

    box = np.int0(box)
    #cv.drawContours(img,[np.int0(cv.boxPoints(rect))],0,(255,0,0),1)
    #cv.drawContours(img,[box],0,(0,0,255),1)
    #imd=img.copy()
    #width = 970
    #height = 620
    #imd = cv.resize(imd, (width, height))

    #cv.imshow('aa', imd)
    #cv.waitKey(0)

    box = box.tolist()
    
    # find which point is top right, top left...
    box = sorted(box,key=lambda l:l[1])
    box = sorted(box,key=lambda l:l[0])
    if distaucarre(box[0]) < distaucarre(box[1]):
        top_left = box[0]
        box.pop(0)
    else:
        top_left = box[1]
        box.pop(1)

    if distaucarre(box[1]) > distaucarre(box[2]):
        bottom_right = box[1]
        box.pop(1)
    else:
        bottom_right = box[2]
        box.pop(2)
    bottom_left = box[0]
    top_right = box[1]

    #resize the image according to the rectangle
    pts1 = np.float32([top_left, bottom_left, top_right, bottom_right])
    pts2 = np.float32([[0, 0], [0, width], [height, 0], [height, width]])
    M = cv.getPerspectiveTransform(pts1, pts2)
    img=cv.warpPerspective(img, M, (height, width))

        
    #if it is rotated 90 degrees 
    while isUpsideDown(img):
        pil_im = Image.fromarray(img)
        pil_im=pil_im.transpose(Image.ROTATE_90)
        img = np.array(pil_im) 
        # Convert RGB to BGR 
        img = img[:, :, ::-1].copy() 
        
    return img



# main for testing only
if __name__ == '__main__':
    pathJPG=r'Grille_Toeic-15-1.jpg'
    img1 = cv.imread(pathJPG)
        
    """
    import cProfile
    pr = cProfile.Profile()
    pr.enable()
    """
    img1 = resize(img1)
    """
    pr.disable()
    pr.print_stats(sort='cumtime')
    """

    width = 970
    height = 620
    resized = cv.resize(img1, (width, height))
    cv.imshow('resized', resized)
    cv.waitKey(0)

