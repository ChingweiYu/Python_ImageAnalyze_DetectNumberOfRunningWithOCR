from PIL import Image
import cv2
import numpy as np
import os
import delete
'''
for jpg in os.listdir("."):
    try:
        im = Image.open( jpg )
        print im.format, im.size, im.mode, 
        T = im.resize( (50,50),Image.BILINEAR)
        T.save(jpg)
    except:
        print ''
        print '***'
        print jpg
        print '***'

'''
def main(name,u,r):
    delete.filedir("build/S")
    delete.filedir("build/R")
    img = cv2.imread('./inn/'+name)
    im = Image.open('./inn/'+name)
    c1=int(im.size[0])/2
    c2=int(im.size[1])/2
    img = img[c1+100+u:c1+600+u, c2-700+r:c2-200+r]
    cv2.imwrite('build/S/'+name,img)
    im_ = Image.open('build/S/'+name)
    T = im_.resize( (250,250),Image.BILINEAR)
    T.save('build/R/'+name)
    #T.save('R/1_ '+name)
'''
def main_facedetect(name):
    delete.filedir("S")
    delete.filedir("R")
    img = cv2.imread('./facedetectoutput/'+name)
    cv2.imwrite('S/'+name,img)
    im_ = Image.open('S/'+name)
    T = im_.resize( (250,250),Image.BILINEAR)
    T.save('R/'+name)
    #T.save('R/1_ '+name)

def main_2(name):
    delete.filedir("build/S")
    delete.filedir("build/R")
    img = cv2.imread('./inn/'+name)
    im = Image.open('./inn/'+name)
    c1=int(im.size[0])/2
    c2=int(im.size[1])/2
    img = img[c1+200:c1+900, c2-800:c2-100]
    cv2.imwrite('build/S/'+name,img)
    im_ = Image.open('build/S/'+name)
    T = im_.resize( (250,250),Image.BILINEAR)
    T.save('build/R/'+name)
    #T.save('R/2_ '+name)
 '''
def main_3(name):
    delete.filedir("build/S")
    delete.filedir("build/R")
    img = cv2.imread('./inn/'+name)
    im = Image.open('./inn/'+name)
    c1=int(im.size[0])
    c2=int(im.size[1])
    img = img[(c2*3/8):(c2*5/8), 0:c1]
    cv2.imwrite('build/S/'+name,img)
    
    im_ = Image.open('build/S/'+name)
    T = im_.resize( (750,500),Image.BILINEAR)
    T.save('build/R/'+name)
    #T.save('R/3_ '+name)
    
def main_4(name):
    delete.filedir("build/S")
    delete.filedir("build/R")
    img = cv2.imread('./inn/'+name)
    im = Image.open('./inn/'+name)
    c1=int(im.size[0]) #w
    c2=int(im.size[1]) #h
    #print c1,c2
    #img = img[w,h]
    img = img[(c2*1/4):(c2*3/4), (c1*1/4):(c1*3/4)]
    cv2.imwrite('build/S/'+name,img)
    im_ = Image.open('build/S/'+name)
    T = im_.resize( (500,1500),Image.BILINEAR)
    #T.save('R/4_ '+name)
    T.save('build/R/'+name)
