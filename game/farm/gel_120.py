import pyautogui
import time
from ...functions import functions_ark as ark
import os
import sys

ark.log_it(f'Started {os.path.basename(__file__)}')

x_0 = 852
y_0 = 777
if len(sys.argv) > 1:
    event_ignore = sys.argv[1]
    if event_ignore == '1':
        y_0 = y_0 + 60

ark.action_start('Arknights', 1242, 812, 339, 164)
ark.resource_menu()
ark.action_start('Arknights', 1242, 812, 339, 164)
pyautogui.moveTo(724, 895)
pyautogui.mouseDown()
pyautogui.moveTo(724, 720, 1)
time.sleep(.6)
pyautogui.mouseUp()
time.sleep(1)
pyautogui.click(x=989, y=891)
time.sleep(1)
pyautogui.moveTo(724, 895)
pyautogui.mouseDown()
pyautogui.moveTo(674, 456, 1)
time.sleep(.6)
pyautogui.mouseUp()
time.sleep(1)
pyautogui.click(x=x_0, y=y_0)
time.sleep(10)

ark.action_start('Arknights', 1242, 812, 339, 164)
ark.start_farm()
time.sleep(250)

ark.action_start('Arknights', 1242, 812, 339, 164)
ark.big_out()

ark.log_it(f'Ended {os.path.basename(__file__)}')