import pyautogui
import time
from .functions import functions_ark as ark
import os
import subprocess
import sys
import keyboard

ark.log_it(f'Started {os.path.basename(__file__)}')

time.sleep(1)
pyautogui.click(x=1915, y=1195)
time.sleep(1)
pyautogui.click(x=1915, y=1195)
time.sleep(1)

def restart_p(times):
    while times > 0:
        ark.kill_w_name('Powertoys')
        keyboard.press_and_release('win')
        time.sleep(1)
        keyboard.write("powertoys")
        time.sleep(5)
        keyboard.press_and_release('enter')
        time.sleep(5)
        times -= 1

restart_p(3)

gplay_path = ark.find_google_play_games_path()
os.chdir(gplay_path)

def restart_gplay(times):
    while times > 0:
        os.system("taskkill /f /im client.exe")
        os.system("taskkill /f /im crosvm.exe")
        os.system("taskkill /f /im Service.exe")
        time.sleep(5)
        try:
            subprocess.Popen([r"C:\Program Files\Google\Play Games\Bootstrapper.exe"])
            time.sleep(10)
        except:
            x = None
        times -= 1

restart_gplay(3)
time.sleep(10)
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
#time.sleep(0.5)
#time.sleep(1)
#keyboard.write(r"C:\Users\User\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Google Play Games\Arknights.lnk")
#time.sleep(0.5)


ark.log_it(f'Ended {os.path.basename(__file__)}')