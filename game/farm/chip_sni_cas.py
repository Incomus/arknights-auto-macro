import pyautogui
import time
from ...functions import functions_ark as ark
import os

ark.log_it(f'Started {os.path.basename(__file__)}')

ark.action_start('Arknights', 1242, 812, 339, 164)
ark.resource_menu()

ark.action_start('Arknights', 1242, 812, 339, 164)
pyautogui.click(x=464, y=594) 
time.sleep(1)
pyautogui.click(x=802, y=542)
time.sleep(1)
ark.drag_from_to(983, 805, 983, 417)
time.sleep(1)
pyautogui.click(x=1226, y=818)
time.sleep(10)
pyautogui.click(x=1156, y=478) 

ark.action_start('Arknights', 1242, 812, 339, 164)
ark.start_farm()
time.sleep(250)

ark.action_start('Arknights', 1242, 812, 339, 164)
ark.big_out()

ark.log_it(f'Ended {os.path.basename(__file__)}')