import pyautogui
import time
from ...functions import functions_ark as ark
import os

ark.log_it(f'Started {os.path.basename(__file__)}')

ark.resource_menu()

pyautogui.click(x=1276, y=715)
time.sleep(1)
pyautogui.click(x=1130, y=890)
time.sleep(10)

ark.start_farm()
time.sleep(750)

ark.big_out()

ark.log_it(f'Ended {os.path.basename(__file__)}')