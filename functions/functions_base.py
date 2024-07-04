import pyautogui
import time
from pandas import DataFrame as DataFrame
from ..functions import functions_ark as ark
import json
import requests
import pyperclip
import keyboard
import os
from datetime import datetime
import winreg
import sys
import win32gui
import win32con
import pywinauto

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def write_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def get_position(data, name):
    for entry in data:
        if entry['name'] == name:
            return entry['position']
    return None

def shuffle(repeat, direction=True):
    while repeat > 0:
        pyautogui.click(x=666, y=450)
        if direction == True:
            time.sleep(.6)
            pyautogui.moveTo(1538, 600)
            pyautogui.mouseDown()
            pyautogui.moveTo(667, 600, 1)
            time.sleep(1)
            pyautogui.mouseUp()
            time.sleep(.6)
            repeat = repeat - 1
        else:
            time.sleep(.6)
            pos = int((1538 + 667) / 2)
            pyautogui.moveTo(pos, 600)
            pyautogui.mouseDown()
            pyautogui.moveTo(1538, 600, 1)
            time.sleep(1)
            pyautogui.mouseUp()
            time.sleep(.6)
            time.sleep(.6)
            pos = int((1538 + 667 + 1) / 2)
            pyautogui.moveTo(pos, 600)
            pyautogui.mouseDown()
            pyautogui.moveTo(1538, 600, 1)
            time.sleep(1)
            pyautogui.mouseUp()
            time.sleep(.6)
            repeat = repeat - 1

def right_shuffle(target, current):
    ark.action_start('Arknights', 1242, 812, 339, 164)
    if target > current:
        repeat = target - current
        shuffle(repeat)
    elif target < current:
        repeat = current - target
        shuffle(repeat, False)
    return target

def open_work():
    ark.action_start('Arknights', 1242, 812, 339, 164)
    time.sleep(.6)
    pyautogui.click(x=472, y=321) # open work
    time.sleep(1)

def open_dorm1():
    pyautogui.click(x=990, y=503)
    time.sleep(1)

def open_dorm2():
    pyautogui.click(x=990, y=621)
    time.sleep(1)

def open_dorm3():
    pyautogui.click(x=992, y=734)
    time.sleep(1)

def open_dorm4():
    pyautogui.click(x=990, y=847)
    time.sleep(1)

def open_center():
    pyautogui.click(x=989, y=395) ## center
    time.sleep(1)
    
def open_recep():
    pyautogui.click(x=990, y=545) ## recep
    time.sleep(1)
    
def open_trade1():
    pyautogui.click(x=992, y=749) ## trade1
    time.sleep(1)    
    
def open_trade2():
    pyautogui.click(x=992, y=900) ## trade2
    time.sleep(1)
    
def open_power1():
    pyautogui.click(x=988, y=351) ## power1
    time.sleep(1)    
    
def open_fac1():
    pyautogui.click(x=993, y=867) ## fac1 gold
    time.sleep(.6)
    
def open_fac2():
    pyautogui.click(x=989, y=316) ## fac2 gold
    time.sleep(1)
    
def open_power2():
    pyautogui.click(x=988, y=465) ## power2
    time.sleep(1)
    
def open_fac3():
    pyautogui.click(x=991, y=950) ## fac3 gold
    time.sleep(1)
    
def open_fac4():
    pyautogui.click(x=990, y=583) ## fac4 exp
    time.sleep(1)
    
def open_power3():
    pyautogui.click(x=992, y=430) ## power3
    time.sleep(1)
    
def switch_skill():
    pyautogui.click(x=1194, y=244)
    time.sleep(.6)

def switch_morale():
    pyautogui.click(x=1269, y=241)
    time.sleep(.6)

def confirm_shift():
    pyautogui.click(x=1470, y=932)
    time.sleep(1)
    pyautogui.click(x=1540, y=931)
    time.sleep(9)

def transform_number(n):
    if n % 2 == 0:
        first_n = int(n / 2)
        second_n = 1
    else:
        first_n = int((n + 1) / 2)
        second_n = 0
    return [first_n, second_n]

def click_op(file_path, op_data, current_page, name, ex=False):
    op_position = get_position(op_data, name)
    if op_position == None:
        op_data.append({"name": name, "position": [0, 1]})
        op_position = get_position(op_data, name)
    source_position = op_position
    repeat = 15
    iteration = 0
    if ex != False:
        ark.action_start('Arknights', 1242, 812, 339, 164)
        count = 12
        while count > 0:
            pyautogui.moveTo(1550, 387)
            pyautogui.mouseDown()
            pyautogui.moveTo(365, 387, 0.3)
            pyautogui.mouseUp()
            time.sleep(.6)
            count = count - 1
        time.sleep(1)
        op_position[1] = 12
        current_page = op_position[0]
    while repeat > 0:
        current_page = right_shuffle(op_position[0], current_page)
        op_pos = transform_number(op_position[1])
        moveTo_x = 750 + 138 * (op_pos[0] - 1)
        if op_pos[1] == 0:
            moveTo_y = 551
        else:
            moveTo_y = 820
        dragTo_x = moveTo_x + 120
        dragTo_y = moveTo_y + 21
        ark.get_ptoys(moveTo_x, moveTo_y, dragTo_x, dragTo_y)
        text = pyperclip.paste()
        try:
            text = ark.normalize(text)
            text = ''.join(text)
        except:
            text = 'Nope lol'
        if name.lower() in text.lower():
            pyautogui.click(x=moveTo_x, y=moveTo_y)
            time.sleep(0.6)
            if ex == False:
                for entry in op_data:
                    if entry['name'] == name:
                        entry['position'] = op_position
                write_json(file_path, op_data)
            return op_data, current_page
        if name.lower() == 'grey' and 'lightn' in text.lower():
            pyautogui.click(x=moveTo_x, y=moveTo_y)
            time.sleep(0.6)
            for entry in op_data:
                if entry['name'] == name:
                    entry['position'] = op_position
            write_json(file_path, op_data)
            return op_data, current_page
        ark.log_it(f'At page {op_position[0]} position {op_position[1]}, [{name}] not in [{text}]')
        iteration += 1
        if ex == False:
            if iteration % 2 == 0:
                op_position[1] -= iteration
            else:
                op_position[1] += iteration
            while op_position[1] > 12:
                op_position[1] -= 12
                op_position[0] += 1
            while op_position[1] < 1:
                op_position[1] += 12
                op_position[0] -= 1
            if op_position[0] < 0:
                op_position[1] += 2 * iteration - 12
                op_position[0] += 1
                while op_position[1] > 12:
                    op_position[1] -= 12
                    op_position[0] += 1
        else:
            op_position[1] -= 1
            while op_position[1] < 1:
                op_position[1] += 12
                op_position[0] -= 1
            
        repeat -= 1
    ark.log_it('Failed to match operator')
    return op_data, current_page

def fill_base(shift_data, op_path, op_data, base_part):
    switch_morale()
    switch_skill()
    operators = get_position(shift_data, base_part)
    current_page = 0
    for operator in operators:
        op_data, current_page = click_op(op_path, op_data, current_page, operator)
    confirm_shift()

def rest_top_4():
    pyautogui.click(x=1091, y=444)
    time.sleep(.6)
    pyautogui.click(x=953, y=439)
    time.sleep(.6)
    pyautogui.click(x=944, y=709)
    time.sleep(.6)
    pyautogui.click(x=811, y=709)
    time.sleep(.6)
    