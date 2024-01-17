@echo off
set "$py=0"
call:construct

setlocal
cd /d %~dp0

python --version 3>NUL
if errorlevel 1 goto errorNoPython

pip install -r requirements.txt
python test.py
pause
goto:eof

:errorNoPython
echo Error^: Python not installed
pause
