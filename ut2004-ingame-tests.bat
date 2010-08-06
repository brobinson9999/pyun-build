@echo off
del C:\UT2004\UserLogs\ConfigTestMutatorResults.log
C:\UT2004\System\UT2004.exe Blackbox?bAutoNumBots=False?NumBots=0?mutator=UnrealUtilityLib.ConfigTestMutator -makenames -windowed
type C:\UT2004\UserLogs\ConfigTestMutatorResults.log