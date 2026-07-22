import pyautogui
import time
from ...functions import functions_ark as ark
import os
import sys

ark.log_it(f'Started {os.path.basename(__file__)}')



ark.action_start('Arknights', 1242, 812, 339, 164)
ark.resource_menu()

ark.action_start('Arknights', 1242, 812, 339, 164)
# ark.drag_from_to(1057, 922, 1057, 506)
# time.sleep(0.5)
pyautogui.click(x=898, y=544)
time.sleep(0.5)
ark.drag_from_to(1196, 810, 1183, 629)
time.sleep(0.5)
pyautogui.click(x=1318, y=751)
time.sleep(10)

ark.action_start('Arknights', 1242, 812, 339, 164)
ark.start_farm()
time.sleep(250)

ark.action_start('Arknights', 1242, 812, 339, 164)
ark.big_out()

ark.log_it(f'Ended {os.path.basename(__file__)}')