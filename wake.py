import os
import subprocess
from .functions import functions_ark as ark
import sys
import time
import pyautogui

ark.log_it(f'Started {os.path.basename(__file__)}')

if len(sys.argv) > 1:
    week_schedule = sys.argv[1]
else:
    week_schedule = '1'

if week_schedule == '0':
    var = '0_start_work_in.bat'

if week_schedule == '1':
    var = '0_start_work.bat'
    
if week_schedule == '2':
    var = '0_start_work_out.bat'
    
if week_schedule == '3':
    var = '0_start_rest.bat'

subprocess.Popen(["explorer.exe"])
time.sleep(1)
w = ark.action_start('Home', 1242, 812, 339, 164)
pyautogui.click(x=908, y=246)
pyautogui.write(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bats', var))
time.sleep(.6)
pyautogui.press('enter')
time.sleep(.6)
w.close_window()
#w = ark.action_start('VLC media', 1242, 812, 339, 164)
#time.sleep(.6)
#w.close_window()

ark.log_it(f'Ended {os.path.basename(__file__)}')