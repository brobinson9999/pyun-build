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
  
def buildUDKmod(ut3baseDir, modName, sourceDirectories, dependencies, nondependencies):
    destDir = os.path.join(udkbaseDir, "Src", modName, "classes")
    
    print "Creating a clean build directory for " + modName + "..."
    bruteIO.removeDirectory(destDir)
    os.makedirs(destDir)
    
    # Copy source code.
    for sourceDirectory in sourceDirectories:
        print "Copying files from " + sourceDirectory + " to " + destDir + "..."
        copyAll.copyAll(sourceDirectory, destDir)

    # Set up the editor.ini so that this package will be included in the next compile.
    print "Setting up UDKEngine.ini..."
    UDKEngineINIPath = os.path.join(udkbaseDir, "Config", "UDKEngine.ini")
    shutil.copyfile(UDKEngineINIPath, UDKEngineINIPath + ".bak")    
    addModToUTEditorINI(UDKEngineINIPath, modName, dependencies)

    # Doesn't actually run the UDK compile - it doesn't interact nicely, and runs in it's own thread.
    # If we run it here, and we are building multiple projects, multiple instances can end up running
    # simultaneously.
