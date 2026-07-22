import pyautogui
import time
from .functions import functions_ark as ark
import os
import subprocess
import sys
import keyboard

ark.log_it(f'Started {os.path.basename(__file__)}')

subprocess.Popen([r"C:\Program Files\Google\Play Games\Bootstrapper.exe"])
time.sleep(120)
pyautogui.click(x=1900, y=20)
time.sleep(0.5)
keyboard.press_and_release('win')
time.sleep(1)
keyboard.write("Arknights")
time.sleep(5)
keyboard.press_and_release('enter')
#time.sleep(0.5)
#try:
#    ark.close_explorer_windows()
#except:
#    print('oof')
#os.startfile('googleplaygames://launch/?id=com.YoStarEN.Arknights')
time.sleep(30)
os.system("taskkill /f /im client.exe")
time.sleep(1)
os.system("taskkill /f /im client.exe")
time.sleep(200)

ark.log_it(f'Ended {os.path.basename(__file__)}')