import os
import numpy as np
import cv2



    
def mse(a,b):
        a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
        b = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
        err = np.sum( (a.astype("float")-b.astype("float"))**2 )
        err /= float(a.shape[0]*a.shape[1])
        return err
def getnum(pic):
                min_a =999999999999
                min_ping=None
                agreecount=0
                for jpg in os.listdir("D"):
                        ref = cv2.imread("D/"+jpg)                       
                        if mse(ref,pic)<min_a:
                                min_a=mse(ref,pic)
                                if min_a<8500:
                                     agreecount+=1   
                                min_png = jpg               
                
                if min_a>10000:
                    #print min_a
                    return
                n = getcountsmaple(str(min_png[0]))
                if min_a>2500 and min_a < 4500 and agreecount > int(n/10):                   
                   #print min_png
                   cv2.imwrite("D/"+min_png[0]+"("+str(n+1)+")"+".jpg",pic)
                   cv2.imwrite("T/"+min_png[0]+"("+str(n+1)+")"+".jpg",pic)
                   #print min_a,min_png[0]
                   print "add sample"
                return min_png

def getcountsmaple(T):
    count = 0
    for Tjpg in os.listdir("D"):
        if Tjpg[0] == T:
            count+=1
    return count
def main():
    for Tjpg in os.listdir("sample"):    
        T=cv2.imread("sample/"+Tjpg)                
        s = getnum(T)
    
        #print 
        #print 
        #print
        #print Tjpg,s
        #print "--"
'''            
def main():
        
        answer=''
        for Tjpg in os.listdir("sample"):
                T=cv2.imread("sample/"+Tjpg)                
                s = getnum(T)
                if s!=None:
                        if s[0]!='e':
                                #print Tjpg,s
                                answer+=s[0]
        return answer
'''
