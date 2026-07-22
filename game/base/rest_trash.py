import pyautogui
import time
from ...functions import functions_ark as ark
from ...functions import functions_base as base
import os
import keyboard
import json
import pyperclip

ark.log_it(f'Started {os.path.basename(__file__)}')

shift_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'jsons', 'operators_shifts.json')
shift_data = base.read_json(shift_path)

op_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'jsons', 'operators.json')
op_data = base.read_json(op_path)

ark.action_start('Arknights', 1242, 812, 339, 164)
pyautogui.click(x=461, y=315)
time.sleep(5)
pyautogui.click(x=1435, y=249)
time.sleep(5)
pyautogui.click(x=1465, y=917)
time.sleep(20)
pyautogui.click(x=1000, y=837)
time.sleep(5)
pyautogui.click(x=829, y=929)
time.sleep(5)
base.fill_base(shift_data, op_path, op_data, 'Dorm 1')
time.sleep(5)
pyautogui.click(x=432, y=234)
time.sleep(5)
ark.log_it(f'Ended {os.path.basename(__file__)}')
