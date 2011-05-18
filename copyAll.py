#!/usr/bin/python

import os
import shutil
import listDirRecursive
import subprocess
import re

def copyAll(sourceRoot, destinationDirectory, onlyCopyNewerFiles=False, makeLinksInsteadOfCopying=False):
    fileList = listDirRecursive.listDirRecursive(sourceRoot, False)
    pathList = listDirRecursive.listDirRecursive(sourceRoot, True)
    
    linkString = ""
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
                if (makeLinksInsteadOfCopying and subprocess.mswindows):
                    #symbolic links mklink <newfile> <oldfile>
                    #hard links fsutil hardlink create <newfile> <oldfile> (must be on the same volume)
                    if (linkString <> ""):
                        linkString = linkString + " && "
                    if (sourcePath.find(" ") <> -1):
                        sourcePath = "\"" + sourcePath + "\""
                    if (destPath.find(" ") <> -1):
                        destPath = "\"" + destPath + "\""
                    linkString = linkString + "fsutil hardlink create " + destPath + " " + sourcePath
                    
                else:
                    shutil.copyfile(sourcePath, destPath)

    if (linkString <> ""):
        print linkString
        p = subprocess.Popen([linkString],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        outputTuple = p.communicate()
        outputText = outputTuple[0] + outputTuple[1]
        
        outputText = re.sub(r'\r\n', "\n", outputText)
        outputText = re.sub(r'Hardlink created for [a-zA-Z0-9_:\\<=> ]*\n', "", outputText)
        #outputText = re.sub(r'Compiling [a-zA-Z0-9_]*\n', "", outputText)
        #outputText = re.sub(r'Importing Defaults for [a-zA-Z0-9_]*\n', "", outputText)
         
        print outputText
 