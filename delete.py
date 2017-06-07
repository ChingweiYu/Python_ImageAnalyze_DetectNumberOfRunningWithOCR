# -*- coding: cp950 -*-
import os

def main():
    try:
        for Tjpg in os.listdir("build/sample1"):
            os.remove("build/sample1/"+Tjpg)#檔案路徑和名稱
    except:
        pass

def filedir(FN):
    try:
        for Tjpg in os.listdir(FN):
            os.remove("./"+FN+"/"+Tjpg)#檔案路徑和名稱
    except:
        print os.listdir(FN)
