# -*- coding: cp950 -*-
import numpy as np
import cv2
import Image
import delete as de


def main(name):
    #im = cv2.imread('a.jpg')
    de.main()
    im = cv2.imread("build/B/"+name)
    imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    ret,thresh = cv2.threshold(imgray,127,255,0)

    im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    cnts = sorted([(c, cv2.boundingRect(c)[0]) for c in contours], key=lambda x:x[1])
    arr = []
    num = 1
    Lcode='w'
    for index, (c, _) in enumerate(cnts):
            (x, y, w, h) = cv2.boundingRect(c)
            try:
                # �u�N�e���j�� �ƭ� �����Ʀr�d�s
                #if w > 4 and h > 25 and w<60 and h<100:
                if w > 4 and h > 25 and w<60 and h<100:
                
                    add = True
                    '''
                    for i in range(0, len(arr)):
                        # �o��O�n����p 0�B9 ���A�i��|�����X����I�A����I�L�󱵪�ݩ���
                        
                        if abs(cnts[index][1] - arr[i][0]) <= 4:
                            add = False
                            break
                       
                    if x==1 and y==1:
                            add =False
                    
                    for x2,y2,w2,h2 in arr:
                            if x>x2 and y>y2 and x+w<x2+w2 and y+h<y+h2:
                                 add =False
                    '''
                    if add:
                        arr.append((x, y, w, h))
                        #print y-1,y+h+1,x-1,x+w+1
                        #print x,y,w,h
                        roi = im[y-1:y+h+1, x-1:x+w+1]
                        roi = cv2.resize(roi,(50,50))
                        if num == 10:
                            num=1
                            Lcode+='w'
                        cv2.imwrite('build/sample/'+Lcode+str(num)+".jpg",roi)
                        num=num+1
            except IndexError:
                    pass

