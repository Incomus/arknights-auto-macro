import pyautogui
import time
from ...functions import functions_ark as ark
import os

ark.log_it(f'Started {os.path.basename(__file__)}')

ark.action_start('Arknights', 1242, 812, 339, 164)
time.sleep(.6)
pyautogui.click(x=1311, y=843)
time.sleep(20)

ark.log_it(f'Ended {os.path.basename(__file__)}')