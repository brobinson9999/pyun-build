@echo off
del E:\software\UT2004\UserLogs\ConfigTestMutatorResults.log
E:\software\UT2004\System\UT2004.exe Blackbox?bAutoNumBots=False?NumBots=0?mutator=UnrealUtilityLib.ConfigTestMutator -makenames -windowed
type E:\software\UT2004\UserLogs\ConfigTestMutatorResults.log