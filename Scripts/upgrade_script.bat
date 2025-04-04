@echo off
setlocal enabledelayedexpansion
cls

:: Enable immediate output display
chcp 65001 >nul

echo Updating system using winget for apps...
echo.
winget update | findstr /V "^$"

echo.
echo Triggering Windows system update...
echo.

:: Triggering system updates with wuauclt
echo Running Windows Update...
wuauclt /detectnow
wuauclt /updatenow

echo.
echo Upgrading all apps, including unexpected ones...
echo.
winget upgrade --all --include-unknown --silent --accept-source-agreements --no-progress | findstr /V "^$"

echo.
echo All tasks completed!
echo.

:: Exit the script without user interaction
exit /b
