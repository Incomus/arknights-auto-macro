import pyautogui
import time
from .functions import functions_ark as ark
import os
import subprocess
import sys

ark.log_it(f'Started {os.path.basename(__file__)}')

gplay_path = ark.find_google_play_games_path()
os.chdir(gplay_path)
try:
    subprocess.Popen(["Bootstrapper.exe"])
    time.sleep(30)
except:
    x = None
os.startfile('googleplaygames://launch/?id=com.YoStarEN.Arknights')
time.sleep(30)
os.system("taskkill /f /im client.exe")
time.sleep(1)
os.system("taskkill /f /im client.exe")
time.sleep(200)

ark.log_it(f'Ended {os.path.basename(__file__)}')