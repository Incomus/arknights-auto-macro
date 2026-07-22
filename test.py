import pyautogui
import time
from .functions import functions_ark as ark
from .functions import functions_base as base
import pyperclip
import datetime
import subprocess
import os
import winreg
import pygetwindow as gw
import win32gui
import pywinauto
import json
import sys
import difflib
import psutil
import pandas as pd
import traceback
pd.set_option('display.max_rows', None)

# Collecting process information
# ark.drag_from_to(1057, 922, 1057, 506)
# time.sleep(0.5)
# pyautogui.click(x=1275, y=839)
# time.sleep(0.5)
# ark.drag_from_to(1027, 842, 1015, 714)
# time.sleep(0.5)
def restart_gplay(times):
    while times > 0:
        os.system("taskkill /f /im client.exe")
        os.system("taskkill /f /im crosvm.exe")
        os.system("taskkill /f /im Service.exe")
        time.sleep(5)
        try:
            subprocess.Popen(["Bootstrapper.exe"])
            time.sleep(10)
        except:
            x = None
        times -= 1

#pyautogui.click(x=959, y=510, clicks=1000, interval=0.01)
#restart_gplay(3)
try:
    ark.action_start('Arknights', 1319, 812, 262, 155)
except:
    print('cant open ark')


#ark.get_ptoys(698, 578, 1173, 701)
#ark.kill_w_name('Powertoys')
#pyautogui.click(x=953, y=471)
#ark.action_start('4G LTE', 1367, 958, 276, 76)
#ark.action_start('OBS', 1367, 958, 276, 76)
#ark.action_start('Arknights', 1319, 812, 262, 155)

#pyautogui.moveTo(x=650, y=395)
#pyautogui.click(x=1139, y=841)
#time.sleep(10)




    
# Iterate over all running processes


current_position = pyautogui.position()
print(f"The current position of the cursor is: {current_position}")

print('done')
