#!/usr/bin/python

from buildUTMod import *

def buildUT2k4modINI(filePath,modName,modTitle="DummyBuild",modLogo="DummyBuildLogo",modDesc="DummyBuildDesc",modCmdLine="DummyBuildCmdLine",modURL="DummyURL"):
    fileData = "[MOD]\nModTitle=" + modTitle + "\nModLogo=" + modLogo + "\nModDesc=" + modDesc + "\nModCmdLine=" + modCmdLine + "\nModURL=" + modURL + "\n"

    bruteIO.removeFile(filePath)
    bruteIO.writeFile(filePath, fileData)
    
def buildUT2k4modSystemINI(baseINIPath, filePath, modName, dependencies, nondependencies):
    fileData = bruteIO.readFile(baseINIPath)
    
    editPackagesString = ""
    for dependency in dependencies:
        editPackagesString = editPackagesString + "EditPackages=" + dependency + "\n"
    editPackagesString = editPackagesString + "EditPackages=" + modName + "\n"
    
    searchString = "CutdownPackages=Core"
    modifiedFileData = fileData.replace(searchString, editPackagesString + searchString)

    for nondependency in nondependencies:
        modifiedFileData = modifiedFileData.replace("EditPackages=" + nondependency, "")

    bruteIO.removeFile(filePath)
    bruteIO.writeFile(filePath, modifiedFileData)

def buildUT2k4mod(ut2004baseDir, modName, sourceDirectories, dependencies, nondependencies, exportcache=True, deleteAfterBuild=False,modTitle="DummyBuild",modLogo="DummyBuildLogo",modDesc="DummyBuildDesc",modCmdLine="DummyBuildCmdLine",modURL="DummyURL"):
    systemDirectory = os.path.join(ut2004baseDir, "System")
    modSystemDirectory = os.path.join(ut2004baseDir, modName, "System")

    # Clear old files and directories.
    print "Clearing old files and directories..."
    baseModPath = os.path.join(ut2004baseDir, modName)
    bruteIO.removeFile(os.path.join(systemDirectory, modName + ".u"))
    bruteIO.removeDirectory(baseModPath)

    # Create needed directories and files.
    print "Creating environment for " + modName + "..."
    sourceCodeDestinationDirectory = os.path.join(baseModPath, modName, "classes")
    os.makedirs(sourceCodeDestinationDirectory)
    os.makedirs(modSystemDirectory)

    buildUT2k4modINI(os.path.join(ut2004baseDir, modName, "UT2k4mod.ini"), modTitle, modLogo, modDesc, modCmdLine, modURL)
    buildUT2k4modSystemINI(os.path.join(systemDirectory, "UT2004.ini"), os.path.join(modSystemDirectory, modName + ".ini"), modName, dependencies, nondependencies)

    # Copy source code.
    for sourceDirectory in sourceDirectories:
        print "Copying files from " + sourceDirectory + "..."
        copyAll.copyAll(sourceDirectory, sourceCodeDestinationDirectory)

    # Do the actual compile.
    # We don't need to pipe stdin for any reason - it is a workaround. If it isn't specified as a pipe Python attempts to duplicate
    # the input handle and in some circumstances that can fail.
    print "Compiling " + modName + "..."
    uccPath = os.path.join(systemDirectory, "UCC.exe")
    p = subprocess.Popen([uccPath + " make -mod=" + modName],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
#    p = subprocess.Popen([uccPath, "make", "-mod=" + modName],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    outputTuple = p.communicate()
    outputText = outputTuple[0] + outputTuple[1]

    import re
    outputText = re.sub(r'\r\n', "\n", outputText)
    outputText = re.sub(r'Analyzing...\n', "", outputText)
    outputText = re.sub(r'-*[a-zA-Z0-9_]* - Release-*\n', "", outputText)
    outputText = re.sub(r'Parsing [a-zA-Z0-9_]*\n', "", outputText)
    outputText = re.sub(r'Compiling [a-zA-Z0-9_]*\n', "", outputText)
    outputText = re.sub(r'Importing Defaults for [a-zA-Z0-9_]*\n', "", outputText)
    
    print outputText
    
    compileReturnCode = p.returncode
    if (compileReturnCode != 0):
        return False
    
    print "Deploying " + modName + "..."
    shutil.copyfile(os.path.join(modSystemDirectory, modName + ".u"), os.path.join(systemDirectory, modName + ".u"))

    print "Running Tests..."
    executeUnrealscriptTestCommandlets(sourceCodeDestinationDirectory, modName, uccPath)

    if (exportcache):    
        print "Generating Cache..."
        subprocess.call([uccPath, "dumpint", modName + ".u"])
        subprocess.call([uccPath, "exportcache", modName + ".u"])

    print "Cleaning up..."
    if (deleteAfterBuild):
        removeDirectory(baseModPath)
    
    print "Finished building " + modName + "."

    return True
