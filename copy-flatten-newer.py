#!/usr/bin/python

import sys
import copyAll

if len(sys.argv) < 2:
    print "Syntax: copy-flatten-newer from-path to-path"
    sys.exit(0)

fromDir = sys.argv[1]
toDir = sys.argv[2]

# necessary if using Windows Python under Cygwin
fromDir = fromDir.replace('/', '\\')
toDir = toDir.replace('/', '\\')

copyAll.copyAll(fromDir, toDir, onlyCopyNewerFiles=True)
