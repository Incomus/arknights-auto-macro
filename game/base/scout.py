import pyautogui
import time
from ...functions import functions_ark as ark
import os
import keyboard

ark.log_it(f'Started {os.path.basename(__file__)}')

ark.action_start('Arknights', 1242, 812, 339, 164)
pyautogui.click(x=480, y=315)
time.sleep(60)
ark.action_start('Arknights', 1242, 812, 339, 164)
keyboard.press_and_release('esc')
time.sleep(2)

ark.log_it(f'Ended {os.path.basename(__file__)}')