# -*- coding: cp950 -*-
import os

def main():
    try:
        for Tjpg in os.listdir("build/sample1"):
            os.remove("build/sample1/"+Tjpg)#�ɮ׸��|�M�W��
    except:
        pass

def filedir(FN):
    try:
        for Tjpg in os.listdir(FN):
            os.remove("./"+FN+"/"+Tjpg)#�ɮ׸��|�M�W��
    except:
        print os.listdir(FN)
