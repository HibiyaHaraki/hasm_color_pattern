@echo off
setlocal

cd /d "%~dp0"

python scripts\generate-index-html.py
if errorlevel 1 (
  echo Failed to generate index.html
  exit /b 1
)

start "" "%~dp0index.html"

endlocal
