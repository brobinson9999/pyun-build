#!/usr/bin/python

import os
import shutil
import subprocess
import listDirRecursive
import copyAll
import bruteIO
import string

def addToStringIfNotPresent(baseString, stringToAdd):
    if (string.find(baseString, stringToAdd) == -1):
        return baseString + stringToAdd;
    else:
        return baseString
    
def executeUnrealscriptTestCommandlets(sourceDirectory, modName, systemDirectory, uccPath):
    testConfigFileContents = bruteIO.readFile(os.path.join(systemDirectory, "ConfigTestMutator.ini"))

    testList = ""
   
    testConfigFileContents = addToStringIfNotPresent(testConfigFileContents, "[UnrealUtilityLib.ConfigTestMutator]\n")
    files = listDirRecursive.listDirRecursive(sourceDirectory, True)
    for filename in files:
        if (filename.endswith("Tests.uc")):
            testList = testList + " " + modName + "." + filename[0:-len(".uc")]
            testConfigFileContents = addToStringIfNotPresent(testConfigFileContents, "testNames=\"" + modName + "." + filename[0:-len(".uc")] + "\"\n")

    bruteIO.writeFile(os.path.join(systemDirectory, "ConfigTestMutator.ini"), testConfigFileContents)

    if (not testList == ""):
        subprocess.call([uccPath, "UnrealUtilityLib.ParameterTestCommandlet", testList])