import Image
import cv2
import numpy as np
import os
import array
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
def main(name):
    img = cv2.imread(name)
    im = Image.open(name)
    #x = np.array([1,2,3], dtype=np.int64)
    img = np.array(img, dtype=np.int64)
    print im.size[0],im.size[1]
    L0=[]
    L1=[]
    L2=[]
    L3=[]
    L4=[]
    L5=[]
    L6=[]
    L7=[]
    L8=[]
    L9=[]
    
    
    for x in range(im.size[1]):
        for y in range(im.size[0]):
            a=img[x,y][0]+img[x,y][1]+img[x,y][2]
            if L0==[]:
                L0=[x,y,a]
            if a>L0[2] and img[x,y][0]>200 and img[x,y][1]>200 and img[x,y][2]>200:  
                L9=L8
                L8=L7
                L7=L6
                L6=L5
                L5=L4
                L4=L3
                L3=L2
                L2=L1
                L1=L0
                L0=[x,y,a]
    '''
    print L0
    print L1
    print L2
    print L3
    print L4
    print L5
    print L6
    print L7
    print L8
    print L9
    '''
    
    Location=[(L0[0]+L1[0]+L2[0]+L3[0]+L4[0]+L5[0]+L6[0]+L7[0]+L8[0]+L9[0])/10,(L0[1]+L1[1]+L2[1]+L3[1]+L4[1]+L5[1]+L6[1]+L7[1]+L8[1]+L9[1])/10]
    return Location
    
                
