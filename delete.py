# -*- coding: cp950 -*-
import os

def main():
    try:
        for Tjpg in os.listdir("build/sample"):
            os.remove("build/sample/"+Tjpg)#檔案路徑和名稱
    except:
        print os.listdir("build/sample")

def filedir(FN):
    try:
        for Tjpg in os.listdir(FN):
            os.remove("./"+FN+"/"+Tjpg)#檔案路徑和名稱
    except:
        print os.listdir(FN)
