#!/usr/bin/python

# similar to make's wildcard operator, but getting all files in all subdirectories

import sys
import listDirRecursive
import os
import string

if len(sys.argv) < 1:
    print "Syntax: wildcard.py <root-directory>"
    sys.exit(0)

rootdirectory = sys.argv[1]
files = listDirRecursive.listDirRecursive(rootdirectory, True)

stringresult = ""
for file in files:
    if (stringresult <> ""):
        stringresult = stringresult + " "
    stringresult = stringresult + string.replace(os.path.join(rootdirectory, file), " ", "\\ ")
    
print stringresult
