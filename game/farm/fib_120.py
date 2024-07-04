import pyautogui
import time
from ...functions import functions_ark as ark
import os

ark.log_it(f'Started {os.path.basename(__file__)}')

ark.action_start('Arknights', 1242, 812, 339, 164)
ark.resource_menu()

ark.action_start('Arknights', 1242, 812, 339, 164)
pyautogui.click(x=1376, y=714)
time.sleep(1)
pyautogui.click(x=1227, y=894)
time.sleep(10)

ark.action_start('Arknights', 1242, 812, 339, 164)
ark.start_farm()
time.sleep(750)

ark.action_start('Arknights', 1242, 812, 339, 164)
ark.big_out()

ark.log_it(f'Ended {os.path.basename(__file__)}')