#!/usr/bin/python

import os
import subprocess

# you may need to update these with your own paths, if you use them

def executePythonFile(filePath, workingDirectory):
    subprocess.call(["python", filePath], cwd=workingDirectory, shell=True)

def executeLispFile(filePath, workingDirectory, loadIndirectly=False):
    if (loadIndirectly):
        subprocess.call([os.path.join("C:\\", "cygwin", "bin", "clisp.exe"), "-q", "-x", "(load \"" + filePath.replace("\\", "/") + "\")"], cwd=workingDirectory, shell=True)
    else:
        subprocess.call([os.path.join("C:\\", "cygwin", "bin", "clisp.exe"), filePath], cwd=workingDirectory, shell=True)
