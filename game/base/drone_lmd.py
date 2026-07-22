import pyautogui
import time
from ...functions import functions_ark as ark
import os

ark.log_it(f'Started {os.path.basename(__file__)}')

ark.action_start('Arknights', 1242, 812, 339, 164)
pyautogui.click(x=796, y=525)
time.sleep(1)
pyautogui.click(x=796, y=525)
time.sleep(1)
ark.drag_from_to(401, 603, 1538, 600)
ark.drag_from_to(401, 603, 1538, 600)

pyautogui.click(x=706, y=602)
time.sleep(1)
pyautogui.click(x=706, y=602)
time.sleep(1)
pyautogui.click(x=663, y=858)
time.sleep(1)
repeat = 7
while repeat > 0:
    pyautogui.click(x=711, y=717)
    time.sleep(1)
    pyautogui.click(x=711, y=717)
    time.sleep(1)
    pyautogui.click(x=1268, y=561)
    time.sleep(1)
    pyautogui.click(x=1266, y=794)
    time.sleep(1)
    repeat -= 1

pyautogui.click(x=423, y=236)
time.sleep(4)
pyautogui.click(x=423, y=236)
time.sleep(1)

ark.log_it(f'Ended {os.path.basename(__file__)}')