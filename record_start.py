import pyautogui
from .functions import functions_ark as ark
import os
import subprocess
import time
import keyboard
from win32api import GetSystemMetrics
ark.log_it(f'Started {os.path.basename(__file__)}')

#width = 0 # GetSystemMetrics(0) - 5
#height = GetSystemMetrics(1) - 5
#pyautogui.click(x=width, y=height)
#time.sleep(.5)
#obs_path = ark.find_obs_path()
#os.chdir(obs_path)
#script_dir = os.path.dirname(os.path.abspath(__file__))
#exp_path = os.path.join(script_dir, r"bats\start_exp.bat")
#subprocess.run([exp_path], check=True)
#time.sleep(2)
#keyboard.press_and_release('tab')
#time.sleep(0.5)
#keyboard.press_and_release('tab')
#time.sleep(0.5)
#keyboard.press_and_release('tab')
#time.sleep(0.5)
#keyboard.press_and_release('tab')
#time.sleep(0.5)
#keyboard.press_and_release('tab')
#time.sleep(1)
#keyboard.write(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\OBS Studio\OBS Studio (64bit).lnk")
#time.sleep(0.5)
os.system("taskkill /f /im obs64.exe")
pyautogui.click(x=1915, y=1195)
time.sleep(1)
pyautogui.click(x=1915, y=1195)
time.sleep(1)
pyautogui.click(x=1915, y=1195)
time.sleep(1)
pyautogui.click(x=1915, y=1195)
time.sleep(1)
keyboard.press_and_release('win')
time.sleep(1)
keyboard.write("OBS Studio")
time.sleep(5)
keyboard.press_and_release('enter')
#time.sleep(0.5)
#try:
#    ark.close_explorer_windows()
#except:
#    print('oof')
#subprocess.Popen(["obs64.exe"])
time.sleep(5)

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
w.minimize_window()
print('record_started')
ark.log_it(f'Ended {os.path.basename(__file__)}')