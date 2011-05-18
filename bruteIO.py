#!/usr/bin/python

import os
import shutil

def removeFile(target):
    if (os.path.isfile(target)):
        os.remove(target)
        
def removeDirectory(target):
    if (os.path.isdir(target)):
        shutil.rmtree(target)

def readFile(path):
    file = open(path, "r")
    fileData = file.read()
    file.close()
    return fileData

def writeFile(path, contents):
    file = open(path, "w")
    file.write(contents)
    file.close()

def ensureDirExists(path):
    dirPath = os.path.normpath(os.path.dirname(path))
    if (not os.path.exists(dirPath)): os.makedirs(dirPath)
    