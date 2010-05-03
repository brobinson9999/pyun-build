#!/usr/bin/python

import os
import shutil
import subprocess
import listDirRecursive
import copyAll
import bruteIO

def executeUnrealscriptTestCommandlets(sourceDirectory, modName, uccPath):
    testList = ""
    files = listDirRecursive.listDirRecursive(sourceDirectory, True)
    for filename in files:
        if (filename.endswith("Tests.uc")):
            testList = testList + " " + modName + "." + filename[0:-len(".uc")]

    if (not testList == ""):
        subprocess.call([uccPath, "UnrealUtilityLib.ParameterTestCommandlet", testList])
            