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
pyautogui.click(x=476, y=582)
time.sleep(1)
pyautogui.click(x=1234, y=683)
time.sleep(10)
pyautogui.click(x=965, y=582)
time.sleep(2)
pyautogui.click(x=1119, y=389)
time.sleep(2)

times = 4
while times > 0:
    pyautogui.click(x=1430, y=911)
    time.sleep(2)
    pyautogui.click(x=1430, y=911)
    time.sleep(10)
    pyautogui.click(x=1430, y=911)
    time.sleep(5)


ark.action_start('Arknights', 1242, 812, 339, 164)
ark.big_out()

ark.log_it(f'Ended {os.path.basename(__file__)}')