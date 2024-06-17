import pyautogui
from .functions import functions_ark as ark
import os
import time

ark.log_it(f'Started {os.path.basename(__file__)}')

w = ark.action_start('OBS', 1367, 958, 276, 76)
time.sleep(.5)
w.restore()
time.sleep(.5)
w = ark.action_start('OBS', 1367, 958, 276, 76)
time.sleep(.5)
pyautogui.hotkey('ctrl','r')
time.sleep(5)
w.close()

ark.log_it(f'Ended {os.path.basename(__file__)}')