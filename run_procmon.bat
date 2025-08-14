@echo off
setlocal enabledelayedexpansion

REM Base directory = this script's folder
set "BASEDIR=%~dp0"

REM Ensure logs folder exists
if not exist "%BASEDIR%logs" mkdir "%BASEDIR%logs"

REM Inputs
set "DURATION=%~1"
if "%DURATION%"=="" set "DURATION=5"

REM Paths
set "PROCMON=%BASEDIR%tools\Procmon64.exe"
set "PML=%BASEDIR%logs\procmon_log.pml"

if not exist "%PROCMON%" (
  echo [!] Procmon not found at %PROCMON%
  exit /b 1
)

echo [*] Launching Procmon for %DURATION% seconds...
"%PROCMON%" /Quiet /Minimized /AcceptEula /BackingFile "%PML%"
timeout /t %DURATION% /nobreak >nul

echo [*] Stopping Procmon...
taskkill /IM Procmon64.exe /F >nul 2>&1

echo [*] Procmon stopped. Log: %PML%
endlocal
