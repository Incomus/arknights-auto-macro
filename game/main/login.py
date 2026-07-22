import pyautogui
import time
import keyboard
from ...functions import functions_ark as ark
import os

ark.log_it(f'Started {os.path.basename(__file__)}')

pyautogui.click(x=2297, y=1417, button='right') #2330
time.sleep(1)
pyautogui.moveTo(x=2405, y=1330)
time.sleep(1)
pyautogui.moveTo(x=2260, y=1333)
time.sleep(1)
pyautogui.click(x=2088, y=1262)
time.sleep(1)
pyautogui.click(x=1443, y=748)
time.sleep(1)
ark.action_start('Arknights', 1242, 812, 339, 164)
time.sleep(1)
count = 3
while count > 0:
    pyautogui.click(x=949, y=728)
    time.sleep(1)
    pyautogui.click(x=949, y=728)
    time.sleep(1)
    pyautogui.click(x=949, y=728)
    time.sleep(20)
    ark.big_out(click=False)

    count = count - 1
    ark.action_start('Arknights', 1242, 812, 339, 164)

ark.big_out()

ark.log_it(f'Ended {os.path.basename(__file__)}')