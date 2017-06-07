# -*- coding: cp950 -*-
import numpy as np
import cv2
import os

def mse(a,b):
	try:
		a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
		b = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
		err = np.sum( (a.astype("float")-b.astype("float"))**2 )
		err /= float(a.shape[0]*a.shape[1])
	except:
		err = 1
        return err
def getnum(pic):
                min_a =999999999999
                min_ping=None
                for jpg in os.listdir("build/D"):
			if jpg == "Thumbs.db":
				pass			
			else:
		                ref = cv2.imread("build/D/"+jpg)
		                if mse(ref,pic)<min_a:
		                        min_a=mse(ref,pic)
		                        min_png = jpg
                #print min_ping           
                if min_a>10000:
                        #return '------'+str(min_a)
                        return 
                  
                #return min_png,min_a
                return min_png

        
#p1=cv2.imread("build/sample/w4.jpg")
#p2=cv2.imread("build/sample/w2.jpg")
#print mse(p1,p2)
def main():
        
        answer=''
	imgs = os.listdir("build/sample1")
	imgs.sort()
        for Tjpg in imgs:
		#print Tjpg
		T=cv2.imread("build/sample1/"+Tjpg)
                s = getnum(T)
                if s!=None:
                        if s[0]!='e':
                                #print Tjpg,s
                                answer+=s[0]
        return answer
