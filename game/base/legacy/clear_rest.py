import pyautogui
import time
from ...functions import functions_ark as ark
import os
import keyboard

ark.log_it(f'Started {os.path.basename(__file__)}')

ark.action_start('Arknights', 1242, 812, 339, 164)
time.sleep(.6)
pyautogui.click(x=472, y=321) # open rest
time.sleep(1)
pyautogui.click(x=1449, y=246)
time.sleep(1)

def clear(y):
    ark.action_start('Arknights', 1242, 812, 339, 164)
    pyautogui.click(x=1498, y=y)
    time.sleep(10)

ark.drag_down()

clear(503)

ark.drag_down()

clear(609)

ark.drag_down()

clear(736)

ark.drag_down()

clear(844)

keyboard.press_and_release('esc')
time.sleep(2)

ark.log_it(f'Ended {os.path.basename(__file__)}')