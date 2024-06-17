import pyautogui
import time
from ...functions import functions_ark as ark
import os

ark.log_it(f'Started {os.path.basename(__file__)}')

ark.resource_menu()

pyautogui.click(x=989, y=891)
time.sleep(1)
pyautogui.moveTo(724, 895)
pyautogui.mouseDown()
pyautogui.moveTo(674, 456, 1)
time.sleep(.6)
pyautogui.mouseUp()
time.sleep(1)
pyautogui.click(x=852, y=777)
time.sleep(10)

ark.start_farm()
time.sleep(750)

ark.big_out()

ark.log_it(f'Ended {os.path.basename(__file__)}')