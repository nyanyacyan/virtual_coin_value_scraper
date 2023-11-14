@echo off
schtasks /create /f /tn "RunMainTask" /tr "%~dp0\03_main_test.bat" /sc daily /st 12:00 /RL HIGHEST
echo schedule complete
pause
