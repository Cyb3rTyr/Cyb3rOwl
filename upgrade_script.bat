@echo off
:: Update all apps and Windows silently
echo Updating system using winget...
winget update

:: Upgrade all apps, including unexpected upgrades, without prompts
echo Upgrading all apps, including unexpected ones...
winget upgrade --all --include-unknown --silent --accept-source-agreements

echo 
echo All tasks completed!
pause
