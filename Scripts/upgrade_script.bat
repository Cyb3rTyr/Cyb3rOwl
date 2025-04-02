@echo off
setlocal enabledelayedexpansion

:: Enable immediate output display
chcp 65001 >nul
cls

echo Updating system using winget...
echo.
winget update | findstr /V "^$"

echo.
echo Upgrading all apps, including unexpected ones...
echo.
winget upgrade --all --include-unknown --silent --accept-source-agreements | findstr /V "^$"

echo.
echo All tasks completed!
echo.

:: Prevent premature exit
pause
exit /b