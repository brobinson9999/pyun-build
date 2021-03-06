#!/usr/bin/python

from buildUTMod import *

def addModToUTEditorINI(UTEditorINIPath, modName, dependencies):
    fileData = bruteIO.readFile(UTEditorINIPath)
    searchString = "ModPackagesInPath="

    result = "";
    for dependency in dependencies:
        if (fileData.find("modPackages=" + dependency) == -1):
            fileData = fileData.replace(searchString, "modPackages=" + dependency + "\n" + searchString)
    if (fileData.find("modPackages=" + modName) == -1):
        fileData = fileData.replace(searchString, "modPackages=" + modName + "\n" + searchString)

    bruteIO.removeFile(UTEditorINIPath)
    bruteIO.writeFile(UTEditorINIPath, fileData)
  
def buildUT3mod(ut3baseDir, modName, sourceDirectories, dependencies, nondependencies):
    destDir = os.path.join(ut3baseDir, "Src", modName, "classes")
    
    print "Creating a clean build directory for " + modName + "..."
    bruteIO.removeDirectory(destDir)
    os.makedirs(destDir)
    
    # Copy source code.
    for sourceDirectory in sourceDirectories:
        print "Copying files from " + sourceDirectory + " to " + destDir + "..."
        copyAll.copyAll(sourceDirectory, destDir)

    # Set up the editor.ini so that this package will be included in the next compile.
    print "Setting up UTEditor.ini..."
    UTEditorINIPath = os.path.join(ut3baseDir, "Config", "UTEditor.ini")
    shutil.copyfile(UTEditorINIPath, UTEditorINIPath + ".bak")    
    addModToUTEditorINI(UTEditorINIPath, modName, dependencies)

    # Doesn't actually run the UT3 compile - it doesn't interact nicely, and runs in it's own thread.
    # If we run it here, and we are building multiple projects, multiple instances can end up running
    # simultaneously.
