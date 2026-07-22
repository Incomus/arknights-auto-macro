import pyautogui
import time
from ...functions import functions_ark as ark
import os

ark.log_it(f'Started {os.path.basename(__file__)}')

ark.action_start('Arknights', 1242, 812, 339, 164)
pyautogui.click(x=845, y=638)
time.sleep(1)
pyautogui.click(x=845, y=638)
time.sleep(1)

pyautogui.moveTo(x=401, y=603)
pyautogui.mouseDown()
pyautogui.moveTo(1538, 600, 1)
time.sleep(1)
pyautogui.mouseUp()
time.sleep(1)
pyautogui.moveTo(x=401, y=603)
pyautogui.mouseDown()
pyautogui.moveTo(1538, 600, 1)
time.sleep(1)
pyautogui.mouseUp()
time.sleep(1)

pyautogui.click(x=650, y=395)
time.sleep(1)
pyautogui.click(x=650, y=395)
time.sleep(1)
pyautogui.click(x=650, y=395)
time.sleep(1)
pyautogui.click(x=753, y=833)
time.sleep(4)
pyautogui.click(x=1517, y=753)
time.sleep(1)
pyautogui.click(x=1267, y=562)
time.sleep(1)
pyautogui.click(x=1370, y=791)
time.sleep(10)
pyautogui.click(x=1420, y=857)
time.sleep(10)
pyautogui.click(x=423, y=236)
time.sleep(4)
pyautogui.click(x=423, y=236)


ark.log_it(f'Ended {os.path.basename(__file__)}')