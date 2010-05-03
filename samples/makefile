# Makefile for building my projects

# set this to the path of the python you want to use - watch out for platform issues if you use Cygwin
python := /cygdrive/c/Python26/python.exe

.SILENT: #don't echo commands

# flatten source trees by copying all files under flatten-sample's src subdirectory to a flattened-src directory
dummy := $(shell $(python) ../copy-flatten-newer.py projects/flatten-sample/src flattened-src/flatten-sample)

all : build-records/hello-world.buildrecord build-records/flatten-sample.buildrecord build-records/codegen-sample.buildrecord build-records/ut3-compile.buildrecord

build-records/hello-world.buildrecord : $(wildcard projects/hello-world/src/*)
	(cd projects/hello-world;$(python) build.py)
	echo Built > build-records/hello-world.buildrecord

build-records/codegen-sample-generate.buildrecord : $(wildcard projects/codegen-sample/codegen/*)
	(cd projects/codegen-sample;$(python) ../../../executeDynamicSourceFiles.py codegen)
	echo Built > build-records/codegen-sample-generate.buildrecord

build-records/codegen-sample.buildrecord : build-records/codegen-sample-generate.buildrecord $(wildcard projects/codegen-sample/src/*)
	(cd projects/codegen-sample;$(python) build.py)
	echo Built > build-records/codegen-sample.buildrecord

build-records/flatten-sample.buildrecord : $(wildcard flattened-src/flatten-sample/*)
	(cd flattened-src/flatten-sample;$(python) ../../projects/flatten-sample/build.py)
	echo Built > build-records/flatten-sample.buildrecord

build-records/ut3-compile.buildrecord : build-records/hello-world.buildrecord
	ut3compile.bat
	echo Built > build-records/ut3-compile.buildrecord

clean : 
	rm build-records/*.buildrecord
	(cd flattened-src;rm */*)
