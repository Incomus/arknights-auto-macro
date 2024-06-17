import pyautogui
import time
from .functions import functions_ark as ark
import os
import subprocess
import sys

ark.log_it(f'Started {os.path.basename(__file__)}')

ark_path = ark.find_google_play_games_path()
if ark_path:
    os.chdir(ark_path)
    subprocess.Popen(["Bootstrapper.exe"])
else:
    print("Google Play Games installation path not found.")
    input()
    sys.exit()
    
time.sleep(15)

ark.action_start('Google Play', 1750, 900, 85, 120)
time.sleep(1)
pyautogui.click(x=973, y=735)
time.sleep(15)
pyautogui.click(x=973, y=735)
time.sleep(15)
pyautogui.click(x=973, y=735)
time.sleep(15)
pyautogui.click(x=973, y=735)
time.sleep(15)
pyautogui.click(x=973, y=735)
time.sleep(15)
pyautogui.click(x=1718, y=304)
time.sleep(5)
pyautogui.click(x=440, y=826)
time.sleep(20)
ark.action_start('Google Play', 1750, 900, 85, 120)
time.sleep(1)
pyautogui.click(x=440, y=826)
time.sleep(20)
ark.action_start('Google Play', 1750, 900, 85, 120)
time.sleep(1)
pyautogui.click(x=440, y=826)
time.sleep(20)
ark.action_start('Google Play', 1750, 900, 85, 120)
time.sleep(1)
pyautogui.click(x=440, y=826)
time.sleep(20)
ark.action_start('Google Play', 1750, 900, 85, 120)
time.sleep(1)
pyautogui.click(x=440, y=826)
time.sleep(20)
ark.action_start('Google Play', 1750, 900, 85, 120)
time.sleep(1)
pyautogui.click(x=440, y=826)
time.sleep(20)
w = ark.action_start('Google Play', 1750, 900, 85, 120)
time.sleep(1)
pyautogui.click(x=440, y=826)
time.sleep(5)
w.close()
time.sleep(1)
os.system("taskkill /f /im client.exe")
time.sleep(1)
os.system("taskkill /f /im client.exe")

ark.log_it(f'Ended {os.path.basename(__file__)}')
