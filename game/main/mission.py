import pyautogui
import time
from ...functions import functions_ark as ark
import os

ark.log_it(f'Started {os.path.basename(__file__)}')

ark.action_start('Arknights', 1242, 812, 339, 164)
time.sleep(.6)
pyautogui.click(x=1107, y=824)
time.sleep(3)
pyautogui.click(x=1415, y=331)
time.sleep(3)
ark.big_out()
time.sleep(3)
pyautogui.click(x=1107, y=824)
time.sleep(2)
pyautogui.click(x=1178, y=235)
time.sleep(3)
pyautogui.click(x=1415, y=331)
time.sleep(3)
ark.big_out()

ark.log_it(f'Ended {os.path.basename(__file__)}')