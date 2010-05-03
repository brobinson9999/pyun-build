#!/usr/bin/python

#from buildUTMod import *

import os
import sys
import listDirRecursive
import subprocessExecute

def executeDynamicSourceFiles(sourceDirectory, deleteWhenDone=False):
    files = listDirRecursive.listDirRecursive(sourceDirectory, True)
    for filename in files:
        filepath = os.path.join(sourceDirectory, filename)
        if (filepath.endswith(".py")):
            print "Executing Python file " + filename
            subprocessExecute.executePythonFile(filepath, ".")
        elif (filepath.endswith(".lisp")):
            print "Executing Common Lisp file " + filename
            subprocessExecute.executeLispFile(filepath, ".", loadIndirectly=True)
    
    if deleteWhenDone:
        for filename in files:
            filepath = os.path.join(sourceDirectory, filename)
            if (not filename.endswith(".uc")):
                removeFile(filepath)
                
if len(sys.argv) < 1:
    print "Syntax: executeDynamicSourceFiles <directory>"
    sys.exit(0)

executeDynamicSourceFiles(sys.argv[1])