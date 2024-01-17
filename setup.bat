@echo off
set "$py=0"
call:construct

setlocal
cd /d %~dp0

for /f "delims=" %%a in ('python #.py ^| findstr "3"') do set "$py=3"
goto:%$py%

echo Python 3 is not installed or python's path is not in the %%$path%% env. var

:3
pip install -r requirements.txt
python test.py
pause