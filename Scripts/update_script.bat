@echo off

cls

echo Checking for and installing updates...
winget update
echo Updates have been triggered. Please wait for them to install.

:: Exit the script without user interaction
exit /b
