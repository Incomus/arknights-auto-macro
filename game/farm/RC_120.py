import pyautogui
import time
from ...functions import functions_ark as ark
import os

### Mon/Thu/Sat/Sun / 0, 3, 5, 6

ark.log_it(f'Started {os.path.basename(__file__)}')

ark.action_start('Arknights', 1242, 812, 339, 164)
time.sleep(.6)
pyautogui.click(x=1482, y=853)
time.sleep(3)
pyautogui.click(x=761, y=395)
time.sleep(1)
pyautogui.click(x=1237, y=691)
time.sleep(3)
pyautogui.click(x=1247, y=410)
time.sleep(2)

ark.start_farm()
sleep_time = 750-4*60-10
time.sleep(sleep_time)

ark.big_out()

ark.log_it(f'Ended {os.path.basename(__file__)}')