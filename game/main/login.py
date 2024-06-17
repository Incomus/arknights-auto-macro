import pyautogui
import time
from ...functions import functions_ark as ark
import os

ark.log_it(f'Started {os.path.basename(__file__)}')

ark.action_start('Arknights', 1242, 812, 339, 164)
time.sleep(1)
count = 20
while count > 0:
    pyautogui.click(x=949, y=728)
    time.sleep(2)
    count = count - 1
    ark.action_start('Arknights', 1242, 812, 339, 164)

ark.big_out()

ark.log_it(f'Ended {os.path.basename(__file__)}')