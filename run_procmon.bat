@echo off
setlocal enabledelayedexpansion

REM Base directory
set "BASEDIR=%~dp0"

REM Ensure logs folder exists
if not exist "%BASEDIR%logs" mkdir "%BASEDIR%logs"

REM Inputs
set "DURATION=%~1"
if not defined DURATION set "DURATION=30"

REM Paths
set "PROCMON=%BASEDIR%tools\Procmon64.exe"
set "PML=%BASEDIR%logs\procmon_log.pml"

if not exist "%PROCMON%" (
  echo [!] Procmon not found at "%PROCMON%"
  exit /b 1
)

echo [*] Launching Procmon for %DURATION% seconds...
start "" "%PROCMON%" /Quiet /Minimized /AcceptEula /NoFilter /BackingFile "%PML%"

REM Wait for specified duration
timeout /t %DURATION% /nobreak >nul

echo [*] Stopping Procmon...
"%PROCMON%" /Terminate

echo [*] Procmon stopped. Log: "%PML%"
endlocal
 
