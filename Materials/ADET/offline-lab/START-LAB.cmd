@echo off
cd /d "%~dp0starter"
if not exist node_modules\expo\bin\cli (
  echo Packages are missing. Read the offline restore steps in README.md.
  pause
  exit /b 1
)
node node_modules\expo\bin\cli start --offline
pause
