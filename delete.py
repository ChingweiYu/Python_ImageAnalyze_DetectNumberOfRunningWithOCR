# -*- coding: cp950 -*-
import os

def main():
    try:
        for Tjpg in os.listdir("build/sample"):
            os.remove("build/sample/"+Tjpg)#�ɮ׸��|�M�W��
    except:
        print os.listdir("build/sample")

def filedir(FN):
    try:
        for Tjpg in os.listdir(FN):
            os.remove("./"+FN+"/"+Tjpg)#�ɮ׸��|�M�W��
    except:
        print os.listdir(FN)
