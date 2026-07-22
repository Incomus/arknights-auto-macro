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
pyautogui.click(x=993, y=886)

ark.drag_from_to(708, 869, 708, 342)
time.sleep(1)
pyautogui.click(x=854, y=655)

time.sleep(10)

ark.action_start('Arknights', 1242, 812, 339, 164)
ark.start_farm()
time.sleep(150)

ark.action_start('Arknights', 1242, 812, 339, 164)
ark.big_out()

ark.log_it(f'Ended {os.path.basename(__file__)}')