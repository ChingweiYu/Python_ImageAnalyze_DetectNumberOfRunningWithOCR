# -*- coding: cp950 -*-
import numpy as np
import cv2
import Image
import resize
import text_betsu as tb
import text_detect as td
import pic_colorcatch as pic
import os
import datetime
import facedetect
import samplelearning as sl
import delete
'''
name = '123'
'''
global errortime
errortime = [0,0,0,0]

def main(im_name):
    
    global errortime#0
    a=""
    '''
    if len(a)!=5:#1
        facedetect.main(im_name)
        resize.main_facedetect(im_name)
        #resize.main(im_name,0,0)
        pic.main(im_name)
        tb.main(im_name)
        a = td.main()
        #Ainn=a+" "
    '''
    if len(a)!=5:#1
        resize.main(im_name,0,0)
        pic.main(im_name)
        tb.main(im_name)
        a = td.main()
        #Ainn+=a+" "
        
    ''''''
    if len(a)!=5:#1
        errortime[0]+=1
        im = resize.main(im_name,-100,200)
        pic.main(im_name)
        tb.main(im_name)
        a = td.main()
        #print 'detect1',im_name,a
    
    if len(a)!=5:#1      
        im = resize.main(im_name,0,200)
        pic.main(im_name)
        tb.main(im_name)
        a = td.main()
    
    if len(a)!=5:#1        
        im = resize.main(im_name,100,200)
        pic.main(im_name)
        tb.main(im_name)
        a = td.main()
    if len(a)!=5:#1      
        im = resize.main(im_name,-100,0)
        pic.main(im_name)
        tb.main(im_name)
        a = td.main()
    if len(a)!=5:#1       
        im = resize.main(im_name,100,0)
        pic.main(im_name)
        tb.main(im_name)
        a = td.main()
    if len(a)!=5:#1       
        im = resize.main(im_name,-100,-200)
        pic.main(im_name)
        tb.main(im_name)
        a = td.main()
    if len(a)!=5:#1    
        im = resize.main(im_name,0,-200)
        pic.main(im_name)
        tb.main(im_name)
        a = td.main()
    if len(a)!=5:#1      
        im = resize.main(im_name,100,-200)
        pic.main(im_name)
        tb.main(im_name)
        a = td.main()
    ###
    if len(a)!=5:#2
        errortime[1]+=1
        im = resize.main_3(im_name)
        pic.main(im_name)
        tb.main(im_name)
        a = td.main()
        #print 'detect3',im_name,a
    
    if len(a)!=5:#3
        errortime[2]+=1
    
        im = resize.main_4(im_name)
        pic.main(im_name)
        tb.main(im_name)
        a = td.main()
        #print 'detect4',im_name,a
    ''''''
    if len(a)>5:#4
        img = cv2.imread('./inn/'+str(im_name))
        cv2.imwrite("G/"+str(im_name),img)
        
        #print 'detect4',im_name,a

    #sample learning
    #sl.main()
    print im_name,a
    return str(a)


successful=0
count=len(os.listdir("inn"))
DC=1
starttime=datetime.datetime.now()
delete.filedir("build/T")

for Tjpg in os.listdir("inn"):
    print ''
    print str(DC)+"/"+str(count)
    detectinn = main(Tjpg)
    img = cv2.imread('./inn/'+str(Tjpg))
    #if Tjpg[0:5]==detectinn:
    if len(detectinn)==5:
        successful+=1
        Scount=len(os.listdir("success"))+1
        nname = str(detectinn)+"("+str(Scount)+").jpg"
        cv2.imwrite("success/"+nname,img)
    else:
        
        cv2.imwrite("error/"+str(Tjpg),img)
        

    DC+=1

print errortime

R=successful/(float(count))*100
#main('2048_b0e6b36fbe10f376d15111260bb2fd42.jpg')
print successful,count
print R

print starttime
print datetime.datetime.now()
print datetime.datetime.now()-starttime
cv2.waitKey(0)
'''

img = img[c1+300:c1+800, c2-700:c2-200]
500x500
 if w > 4-60 and h > 20 -100



img = img[c1+200:c1+900, c2-800:c2-100]
700x700
if w > 0-15 and h > 10-25:

'''
