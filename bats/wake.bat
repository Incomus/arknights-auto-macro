@echo off
if "%1"=="" (
    set arg=1
) else (
    set arg=%1
)


cd /d "%~dp0..\.."
python -m ark.wake %arg%