#!/usr/bin/python

import os
import subprocess

# you may need to update these with your own paths, if you use them

def executePythonFile(filePath, workingDirectory):
    subprocess.call(["python", filePath], cwd=workingDirectory, shell=True)

def executeLispFile(filePath, workingDirectory, loadIndirectly=False):
#    pathToLisp = os.path.join("C:\\", "cygwin", "bin", "clisp.exe")
    pathToLisp = os.path.join("C:", "Program Files", "clisp-2.47", "clisp.exe")
    if (loadIndirectly):
        subprocess.call([pathToLisp, "-q", "-x", "(load \"" + filePath.replace("\\", "/") + "\")"], cwd=workingDirectory, shell=False)
    else:
        subprocess.call([pathToLisp, filePath], cwd=workingDirectory, shell=False)
