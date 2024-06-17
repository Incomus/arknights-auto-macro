import pyautogui
import time
from ...functions import functions_ark as ark
import os

ark.log_it(f'Started {os.path.basename(__file__)}')

git_url = 'https://github.com/Incomus/arknights-recruit-tags-thingie'
tags = ark.load_json(git_url, 'tags.json')
operators_data = ark.load_json(git_url, 'operators.json')

operators_data.sort()
operators_data = [[x[0], x[1], [num + 1 for num in x[2]]] for x in operators_data]
operators_data = [[x[0], x[1], x[2] + [0] + [1]] for x in operators_data]

ark.action_start('Arknights', 1242, 812, 339, 164)
pyautogui.click(x=1305, y=734)
time.sleep(1)

ark.click_tags(370, 530, 946, 640, 658, 517, operators_data, tags)

ark.click_tags(978, 526, 1540, 637, 1266, 516, operators_data, tags)

ark.click_tags(373, 793, 937, 902, 667, 781, operators_data, tags)

ark.click_tags(983, 793, 1541, 901, 1261, 765, operators_data, tags)

ark.action_start('Arknights', 1242, 812, 339, 164)
pyautogui.click(x=426, y=239)
time.sleep(.6)
ark.big_out()

ark.log_it(f'Ended {os.path.basename(__file__)}')