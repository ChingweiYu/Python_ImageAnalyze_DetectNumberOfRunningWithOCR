import cv2
import numpy as np
import sys
import delete
def to_hsv(r,g,b):
    color = np.uint8([[[b,g,r]]])
    hsv_color = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
    return hsv_color
def main(name):
    '''
    '''
    delete.filedir("build/B")
    img = cv2.imread('build/R/'+name)
    #img = cv2.imread('R/123.jpg')
    
    img = np.asarray(img)
    
    # Take each frame
    #frame =np.asarray(img)

    # Convert BGR to HSV
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # define range of blue color in HSV
    # lower_blue  = np.array([G, B, R], dtype = "uint8")
    lower_blue  = np.array([0, 0, 0], dtype = "uint8")
    upper_blue  = np.array([170, 170, 170], dtype = "uint8")
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(img, lower_blue, upper_blue)
    
    '''
    lower_blue  = np.array([0, 0, 0], dtype = "uint8")
    upper_blue  = np.array([170,170 ,170], dtype = "uint8")
    mask = cv2.inRange(img, lower_blue, upper_blue)
    mask = cv2.bitwise_and(img,img, mask= mask)

    lower_blue  = np.array([0, 0, 0], dtype = "uint8")
    upper_blue  = np.array([50,50 ,50], dtype = "uint8")
    mask = cv2.inRange(mask, lower_blue, upper_blue)
    '''

    
    
    # Bitwise-AND mask and original image
    #res = cv2.bitwise_and(frame,frame, mask= mask)
    
    #cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    #cv2.imshow('res',res)
    cv2.imwrite('build/B/'+name,mask)

