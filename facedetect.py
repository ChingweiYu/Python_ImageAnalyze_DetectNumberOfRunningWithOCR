#!/usr/bin/env python

import numpy as np
import cv2
import Image
# local modules
from video import create_capture
from common import clock, draw_str




def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30), flags = cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
        print (x1, y1), (x2, y2)

def main(name):
    import sys, getopt
    
    args, video_src = getopt.getopt(sys.argv[1:], '', ['cascade=', 'nested-cascade='])
    try:
        video_src = video_src[0]
    except:
        video_src = 0
    args = dict(args)
    cascade_fn = args.get('--cascade', "./xml/data/haarcascades/haarcascade_frontalface_alt.xml")
    
    #nested_fn  = args.get('--nested-cascade', "./xml/data/haarcascades/haarcascade_eye.xml")
   

    cascade = cv2.CascadeClassifier(cascade_fn)
    #nested = cv2.CascadeClassifier(nested_fn)

    
    img = cv2.imread('./inn/'+name)
        
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
       
    gray = cv2.equalizeHist(gray)

    #t = clock()
    rects = detect(gray, cascade)        
    #vis = img.copy()
    #draw_rects(vis, rects, (0, 255, 0))
    cv2.imwrite('./facedetectoutput/'+name,img)
    
        
    for x1, y1, x2, y2 in rects:
        #print x1, y1, x2, y2
        yd=y2-y1
        xd=x2-x1
        if xd>x1:
            xd = 0
        cv2.imwrite('./facedetectoutput/'+name,img[y1+yd*3:y1+yd*5,x1-xd:x2+xd])
        
        #cv2.imwrite('./facedetectoutput/1_'+name,img[y1:y2,x1:x2])
        #cv2.imwrite('./facedetectoutput/2_'+name,img[100:500,300:700])
        #cv2.imwrite('./facedetectoutput/3_'+name,img)

    #dt = clock() - t

    #draw_str(vis, (20, 20),'tt')
    #cv2.imshow('inn', vis)
    #cv2.imwrite('./inn.jpg',vis)

    
