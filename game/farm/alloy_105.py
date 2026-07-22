import pyautogui
import time
from ...functions import functions_ark as ark
import os
import sys

ark.log_it(f'Started {os.path.basename(__file__)}')

x_0 = 1322
y_0 = 509
if len(sys.argv) > 1:
    event_ignore = sys.argv[1]
    if event_ignore == '1':
        y_0 = y_0 + 60

ark.action_start('Arknights', 1242, 812, 339, 164)
ark.resource_menu()

ark.action_start('Arknights', 1242, 812, 339, 164)
pyautogui.click(x=1470, y=368)
time.sleep(1)
repeat = 2
while repeat > 0:
    x = 936
    y = 723
    pyautogui.moveTo(x, y)
    pyautogui.mouseDown()
    y = 723 - 350
    pyautogui.moveTo(x, y, 1)
    time.sleep(.6)
    pyautogui.mouseUp()
    time.sleep(1)
    repeat = repeat - 1
pyautogui.click(x=x_0, y=y_0)
time.sleep(10)

ark.action_start('Arknights', 1242, 812, 339, 164)
ark.start_farm()
time.sleep(250)

ark.action_start('Arknights', 1242, 812, 339, 164)
ark.big_out()

ark.log_it(f'Ended {os.path.basename(__file__)}')