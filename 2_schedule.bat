@echo off
schtasks /create /tn "RunMainTask" /tr "%~dp03_main_test.bat" /sc daily /st 06:00
echo schedule complete
pause