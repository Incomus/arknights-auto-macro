import pyautogui
import time
from ...functions import functions_ark as ark
from ...functions import functions_base as base
import os
import keyboard

def rest_dorm(op_path, op_data, op):
    pyautogui.click(x=836, y=931)
    time.sleep(.6)
    base.switch_morale()
    base.switch_skill()
    current_page = 0
    op_data, current_page = base.click_op(op_path, op_data, current_page, op)
    base.switch_skill()
    base.switch_morale()
    base.switch_morale()
    base.right_shuffle(0, current_page)
    base.rest_top_4()
    base.confirm_shift()

ark.log_it(f'Started {os.path.basename(__file__)}')

op_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'jsons', 'operators.json')
op_data = base.read_json(op_path)

base.open_work()

ark.drag_down()

base.open_dorm1()
rest_dorm(op_path, op_data, 'Lumen')

ark.drag_down()

base.open_dorm2()
rest_dorm(op_path, op_data, 'Myrt')

ark.drag_down()

base.open_dorm3()
rest_dorm(op_path, op_data, 'Amiya')

ark.drag_down()

base.open_dorm4()
rest_dorm(op_path, op_data, 'Zima')

keyboard.press_and_release('esc')
time.sleep(2)

ark.log_it(f'Ended {os.path.basename(__file__)}')