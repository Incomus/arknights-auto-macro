import pyautogui
import time
from ...functions import functions_ark as ark
import os

ark.log_it(f'Started {os.path.basename(__file__)}')

def get_recruit(x, y):
    ark.action_start('Arknights', 1242, 812, 339, 164)
    time.sleep(.6)
    pyautogui.click(x=1305, y=734)
    time.sleep(2)
    pyautogui.click(x=x, y=y)
    time.sleep(2)
    count = 15
    while count > 0:
        pyautogui.click(x=1522, y=238)
        time.sleep(1)
        count = count - 1
    ark.big_out()

get_recruit(427, 605)
get_recruit(1441, 605)
get_recruit(427, 872)
get_recruit(1441, 872)

ark.log_it(f'Ended {os.path.basename(__file__)}')