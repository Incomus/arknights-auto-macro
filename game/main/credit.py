import pyautogui
import time
from ...functions import functions_ark as ark
import os

ark.log_it(f'Started {os.path.basename(__file__)}')

ark.action_start('Arknights', 1242, 812, 339, 164)
time.sleep(.6)
pyautogui.click(x=1143, y=709)
time.sleep(10)
pyautogui.click(x=1485, y=306)
time.sleep(5)
ark.action_start('Arknights', 1242, 812, 339, 164)
pyautogui.click(x=1326, y=240)
time.sleep(10)
pyautogui.click(x=966, y=883)
time.sleep(5)
pyautogui.click(x=966, y=883)
time.sleep(5)
pyautogui.click(x=966, y=883)
time.sleep(5)

def buy(x, y):
    ark.action_start('Arknights', 1242, 812, 339, 164)
    time.sleep(.5)
    pyautogui.click(x=x, y=y)
    time.sleep(1)
    pyautogui.click(x=1243, y=797)
    time.sleep(5)
    pyautogui.click(x=966, y=883)
    time.sleep(2)

buy(479, 512)
buy(714, 512)
buy(956, 512)
buy(1199, 512)
buy(1440, 512)
buy(479, 743)

ark.big_out()

ark.log_it(f'Ended {os.path.basename(__file__)}')