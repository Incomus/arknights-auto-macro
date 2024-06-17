import pyautogui
import time
from ...functions import functions_ark as ark
import os
import keyboard

ark.log_it(f'Started {os.path.basename(__file__)}')

ark.action_start('Arknights', 1242, 812, 339, 164)
pyautogui.click(x=1539, y=289)
time.sleep(1)
count = 6
while count > 0:
    ark.action_start('Arknights', 1242, 812, 339, 164)
    pyautogui.click(x=531, y=932)
    time.sleep(3)
    count = count - 1

pyautogui.click(x=1523, y=336)
time.sleep(1)
count = 6
while count > 0:
    ark.action_start('Arknights', 1242, 812, 339, 164)
    pyautogui.click(x=531, y=932)
    time.sleep(3)
    count = count - 1

count = 4
while count > 0:
    pyautogui.click(x=1114, y=434)
    time.sleep(.6)
    count = count - 1
    
keyboard.press_and_release('esc')
time.sleep(2)

ark.log_it(f'Ended {os.path.basename(__file__)}')