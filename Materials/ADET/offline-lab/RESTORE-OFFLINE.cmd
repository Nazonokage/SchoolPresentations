@echo off
cd /d "%~dp0starter"
echo This restores starter dependencies from the prepared cache.
call npm ci --offline --cache "..\npm-cache" --no-audit --no-fund
pause
