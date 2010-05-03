#!/usr/bin/python

import os

def listDirRecursive(sourceRoot, storeRelativePath):
    result = []
    listDirRecursiveAppend(sourceRoot, "", result, storeRelativePath)
    return result

def listDirRecursiveAppend(sourceRoot, relativePathBase, result, storeRelativePath):
    # Iterate through all files in the sourceRoot directory
    fileList = os.listdir(sourceRoot)
    for fileName in fileList:
        # Build Path
        sourcePath = os.path.join(sourceRoot, fileName)
        relativePath = os.path.join(relativePathBase, fileName)
        
        # Add to result list
        # 20081223: Should I be getting directories here or only files?
        if (storeRelativePath):
            result.append(relativePath)
        else:
            result.append(fileName)

        # Recurse to subdirectories
        if (os.path.isdir(sourcePath)):
            listDirRecursiveAppend(sourcePath, relativePath, result, storeRelativePath)
