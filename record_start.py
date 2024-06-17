import pyautogui
from .functions import functions_ark as ark
import os
import subprocess
import time

ark.log_it(f'Started {os.path.basename(__file__)}')

obs_path = ark.find_obs_path()
os.chdir(obs_path)
subprocess.Popen(["obs64.exe"])

try:
    ark.action_start('Safe Mode', 643, 236, 626, 426)
    time.sleep(.5)
    pyautogui.click(x=1169, y=614)
    time.sleep(5)
except:
    time.sleep(5)
    
w = ark.action_start('OBS', 1367, 958, 276, 76)
time.sleep(.5)
pyautogui.hotkey('ctrl','r')
time.sleep(.5)
w.minimize()
print('record_started')
ark.log_it(f'Ended {os.path.basename(__file__)}')