set "countdown3=60"
:CountdownLoop3
echo Waiting %countdown3% seconds to hibernate...
timeout /t 1 /nobreak >nul
set /a "countdown3-=1"
if %countdown3% gtr 0 goto CountdownLoop3

shutdown -h