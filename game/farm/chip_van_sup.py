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
pyautogui.click(x=808, y=722)
time.sleep(1)
ark.drag_from_to(1097, 857, 1092, 610)
time.sleep(1)
pyautogui.click(x=1221, y=866)
time.sleep(10)
pyautogui.click(x=1146, y=484)  

ark.action_start('Arknights', 1242, 812, 339, 164)
ark.start_farm()
time.sleep(250)

ark.action_start('Arknights', 1242, 812, 339, 164)
ark.big_out()

ark.log_it(f'Ended {os.path.basename(__file__)}')