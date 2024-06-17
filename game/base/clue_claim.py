import pyautogui
import time
from ...functions import functions_ark as ark
import os

ark.log_it(f'Started {os.path.basename(__file__)}')

ark.action_start('Arknights', 1242, 812, 339, 164)
pyautogui.click(x=1525, y=420)
time.sleep(3)
pyautogui.click(x=622, y=854)
time.sleep(3)
ark.big_out()
time.sleep(1)
pyautogui.click(x=1328, y=851)
time.sleep(10)
pyautogui.click(x=1525, y=420)
time.sleep(3)
pyautogui.click(x=622, y=854)
time.sleep(3)
pyautogui.click(x=1491, y=372)
time.sleep(2)
pyautogui.click(x=1112, y=793)
time.sleep(.6)
pyautogui.click(x=1295, y=335)
time.sleep(3)
pyautogui.click(x=1492, y=570)
time.sleep(3)

def gift_clue(y):
    ark.action_start('Arknights', 1242, 812, 339, 164)
    pyautogui.click(x=557, y=423)
    time.sleep(1)
    pyautogui.click(x=1486, y=y)
    time.sleep(4)
    
gift_clue(336)
gift_clue(465)
gift_clue(613)
gift_clue(750)

pyautogui.click(x=1508, y=929)
time.sleep(1)

gift_clue(336)
gift_clue(465)
gift_clue(613)
gift_clue(750)

pyautogui.click(x=1537, y=233)
time.sleep(1)
pyautogui.click(x=459, y=246)
time.sleep(2)
pyautogui.click(x=459, y=246)

ark.log_it(f'Ended {os.path.basename(__file__)}')