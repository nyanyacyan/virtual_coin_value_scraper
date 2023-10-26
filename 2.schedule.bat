@echo off
schtasks /create /tn "RunMainTask" /tr "%~dp0run_main.bat" /sc daily /st 06:00
echo schedule complete
pause