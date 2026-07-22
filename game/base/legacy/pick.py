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

base.open_work()
ark.drag_down()
base.open_dorm1()
current_page = 0
base.switch_skill()
op_data, current_page = base.click_op(op_path, op_data, current_page, 'Siege')
base.confirm_shift()
keyboard.press_and_release('esc')
time.sleep(1)

base.open_work()
base.open_center()
base.fill_base(shift_data, op_path, op_data, 'Center')

base.open_recep()
base.fill_base(shift_data, op_path, op_data, 'Reception')

base.open_trade1()
current_page = 0
op_data, current_page = base.click_op(op_path, op_data, current_page, 'Morgan')
base.switch_skill()
op_data, current_page = base.click_op(op_path, op_data, current_page, 'Proviso')
base.switch_morale()
base.switch_morale()
op_data, current_page = base.click_op(op_path, op_data, current_page, 'Siege', True)
base.switch_skill()
base.confirm_shift()

base.open_trade2()
base.fill_base(shift_data, op_path, op_data, 'Trade 2')

ark.drag_down()

base.open_power1()
base.fill_base(shift_data, op_path, op_data, 'Power 1')

base.open_dorm1()
base.fill_base(shift_data, op_path, op_data, 'Dorm 1')

base.open_fac1()
base.fill_base(shift_data, op_path, op_data, 'Fac 1')

ark.drag_down()

base.open_fac2()
base.fill_base(shift_data, op_path, op_data, 'Fac 2')

base.open_power2()
base.fill_base(shift_data, op_path, op_data, 'Power 2')

base.open_dorm2()
base.fill_base(shift_data, op_path, op_data, 'Dorm 2')

base.office()
base.fill_base(shift_data, op_path, op_data, 'Office')

base.open_fac3()
base.fill_base(shift_data, op_path, op_data, 'Fac 3')

ark.drag_down()

base.open_power3()
base.fill_base(shift_data, op_path, op_data, 'Power 3')

base.open_fac4()
base.fill_base(shift_data, op_path, op_data, 'Trade 3')

base.open_dorm3()
base.fill_base(shift_data, op_path, op_data, 'Dorm 3')

ark.drag_down()

base.open_dorm4()
base.fill_base(shift_data, op_path, op_data, 'Dorm 4')

keyboard.press_and_release('esc')
time.sleep(2)

ark.log_it(f'Ended {os.path.basename(__file__)}')
