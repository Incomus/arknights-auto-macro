import pyautogui
import time
from ...functions import functions_ark as ark
from ...functions import functions_base as base
import os
import keyboard
import json
import pyperclip

ark.log_it(f'Started {os.path.basename(__file__)}')
ark.action_start('Arknights', 1242, 812, 339, 164)
pyautogui.click(x=461, y=315)
time.sleep(5)
pyautogui.click(x=1504, y=385)
time.sleep(5)
pyautogui.click(x=1504, y=573)
time.sleep(5)
pyautogui.click(x=1504, y=758)
time.sleep(5)
ark.drag_from_to(1153, 914, 1153, 326)
time.sleep(5)
pyautogui.click(x=1504, y=361)
time.sleep(5)
pyautogui.click(x=1504, y=509)
time.sleep(5)
pyautogui.click(x=1504, y=702)
time.sleep(5)
pyautogui.click(x=1504, y=850)
time.sleep(5)
ark.drag_from_to(1153, 914, 1153, 326)
time.sleep(5)
pyautogui.click(x=1504, y=448)
time.sleep(5)
pyautogui.click(x=1504, y=643)
time.sleep(5)
pyautogui.click(x=1504, y=790)
time.sleep(5)
ark.drag_from_to(1153, 914, 1153, 326)
time.sleep(5)
pyautogui.click(x=1504, y=386)
time.sleep(5)
pyautogui.click(x=1504, y=572)
time.sleep(5)
pyautogui.click(x=432, y=234)
ark.log_it(f'Ended {os.path.basename(__file__)}')
