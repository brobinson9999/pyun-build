#!/usr/bin/python

import os
import shutil
import listDirRecursive

def copyAll(sourceRoot, destinationDirectory, onlyCopyNewerFiles=False):
    fileList = listDirRecursive.listDirRecursive(sourceRoot, False)
    pathList = listDirRecursive.listDirRecursive(sourceRoot, True)
    
    for i in range(0,len(fileList)):
        # Build Path
        sourcePath = os.path.join(sourceRoot, pathList[i])

        # Copy Files
        if (os.path.isfile(sourcePath)):
            destPath = os.path.join(destinationDirectory, fileList[i])
            copyFile = True
            if (onlyCopyNewerFiles and os.path.exists(destPath)):
                if (os.path.getmtime(sourcePath) <= os.path.getmtime(destPath)):
                    copyFile = False
                
            if (copyFile):
                #print "Copying " + sourcePath + " to " + destPath + "."
                shutil.copyfile(sourcePath, destPath)
