import pyautogui
from .functions import functions_ark as ark
import os
import time

ark.log_it(f'Started {os.path.basename(__file__)}')
try:
    w = ark.action_start('OBS', 1367, 958, 276, 76)
    time.sleep(.5)
    pyautogui.hotkey('ctrl','r')
    time.sleep(5)
    w.close_window
except:
    ark.log_it(f'Failed to kill OBS, simply killing obs64 instead')
os.system("taskkill /f /im obs64.exe")()

ark.log_it(f'Ended {os.path.basename(__file__)}')