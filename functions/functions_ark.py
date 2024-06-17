import pyautogui
import time
from pandas import DataFrame as DataFrame
import json
import requests
import pyperclip
import keyboard
import os
from datetime import datetime
import winreg

def action_start(title, resize_x, resize_y, move_x, move_y):
    w = pyautogui.getWindowsWithTitle(title)[0]
    w.activate()
    w.restore()
    w.resizeTo(resize_x, resize_y)
    w.moveTo(move_x, move_y)
    time.sleep(.5)
    return w

def normalize(text):
    text = text.replace('\n', ',').replace('\r', ',').replace(',,', ',')
    text = text.split(',')
    text = ["AoE" if x.lower() == "aoe" else x for x in text]
    return text

def load_json(repo_url, json_path):
    url = f"{repo_url}/raw/main/{json_path}"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data

def comb_tags(tags, operators_data, input_tags, debug=False, manual=True):
    combinatory_data = []
    tags_range = range(len(input_tags))
    tags1_range = [0, *tags_range[2:-2]]
    for tag1_index in tags1_range:
        tags2_range = tags_range[tag1_index + 1:-1]
        for tag2_index in tags2_range:
            tags3_range = tags_range[tag2_index + 1:]
            for tag3_index in tags3_range:
                if debug == True:
                    if input_tags[tag1_index] == 0 and input_tags[tag2_index] == 1:
                        print_tags = input_tags[tag3_index] - 1
                    elif input_tags[tag1_index] in [0, 1]:
                        print_tags = [input_tags[tag2_index] - 1, input_tags[tag3_index] - 1]
                    else:
                        print_tags = [input_tags[tag1_index] - 1, input_tags[tag2_index] - 1,
                                      input_tags[tag3_index] - 1]
                    print('picked', print_tags)
                operators_var = []
                rarity_var = []
                match = False
                for operator_index in range(len(operators_data)):
                    if input_tags[tag1_index] in operators_data[operator_index][2] and \
                            input_tags[tag2_index] in operators_data[operator_index][2] and \
                            input_tags[tag3_index] in operators_data[operator_index][2]:
                        match = True
                        if operators_data[operator_index][0] == 0:
                            if debug == True:
                                print(f'skipped {print_tags}: matched low rar {operators_data[operator_index][1]}')
                            break
                        if tag1_index == 0 and \
                                tag2_index == 1 and \
                                input_tags[tag3_index] == 29:
                            if debug == True:
                                print(f'skipped {print_tags}: skip single top op')
                            if manual == True:
                                log_it("Recruitment manual top op!")
                                raise ValueError('manual top op')
                            break
                        if tag1_index == 0 and \
                                tag2_index == 1 and \
                                input_tags[tag3_index] == 7:
                            if manual == True:
                                log_it("Recruitment manual: robot")
                                raise ValueError('manual robot')
                        if operators_data[operator_index][0] == -1:
                            if debug == True:
                                print('skipped robot')
                            continue
                        if operators_data[operator_index][0] == 3 and \
                                input_tags[tag1_index] != 29 and \
                                input_tags[tag2_index] != 29 and \
                                input_tags[tag3_index] != 29:
                            if debug == True:
                                print(f'skipped {operators_data[operator_index][1]}: 6* without top op')
                            continue
                        if rarity_var and min(rarity_var) < operators_data[operator_index][0]:
                            if debug == True:
                                print(f'skipped {operators_data[operator_index][1]}: higher rarity than min')
                            continue
                        bads = 0
                        for point in combinatory_data:
                            point = [[x for x in point[0] if x not in [0, 1]], point[1], point[2]]
                            if set(point[0]).issubset({input_tags[tag1_index], input_tags[tag2_index],
                                                       input_tags[tag3_index]}):
                                for op in point[2]:
                                    op_tags = [row for row in operators_data if row[1] == op][0][2]
                                    if {input_tags[tag1_index], input_tags[tag2_index],
                                        input_tags[tag3_index]}.issubset(op_tags):
                                        bads = 1
                        if bads == 1:
                            if debug == True:
                                print(f'skipped {operators_data[operator_index][1]}: is subset')
                            continue
                        operators_var.append(operators_data[operator_index][1])
                        rarity_var.append(operators_data[operator_index][0])
                        if debug == True:
                            print(f'added {print_tags}: {operators_data[operator_index][1]} is good to go')
                if rarity_var:
                    combinatory_var = [[input_tags[tag1_index], input_tags[tag2_index], input_tags[tag3_index]],
                                       min(rarity_var), operators_var]
                    combinatory_data.append(combinatory_var)
                else:
                    if debug == True and match is False:
                        print('no matches')
    combinatory_data = [[[ops for ops in x[0] if ops not in [0, 1]], x[1], x[2]] for x in combinatory_data]
    for point in combinatory_data:
        for i, tag in enumerate(point[0]):
            point[0][i] = tags[tag]
    combinatory_df = DataFrame(combinatory_data, columns=['Tags', 'Rarity', 'Operators'])
    combinatory_df['len'] = combinatory_df['Tags'].str.len()
    combinatory_df = combinatory_df.sort_values(by='len').drop(columns='len')
    combinatory_df = combinatory_df.sort_values(by='Rarity', ascending=False).reset_index(drop=True)
    combinatory_df = combinatory_df['Tags']
    if combinatory_df.empty:
        return combinatory_df
    combinatory_df = combinatory_df[0]
    return combinatory_df

def get_tags(operators_data, tags, user_tags):
    robot_rar = -1
    for operator_index in range(len(operators_data)):
        if 8 in operators_data[operator_index][2]:
            operators_data[operator_index][0] = robot_rar
    tags_df = DataFrame(tags, columns=['Tag'])
    tags_parse = tags_df[1:].reset_index(drop=True)[1:]
    discrepancies = []
    def get_tag_index(tag):
        try:
            return tags_parse[tags_parse['Tag'] == tag].index[0]
        except IndexError:
            discrepancies.append(tag)
            return None
    try:
        user_tags = [get_tag_index(tag) for tag in user_tags]
        if discrepancies:
            log_it(f"Recruitment discrepancies observed: {discrepancies}")
            return 'X'
        user_tags_source = DataFrame(user_tags, columns=['Tag'])
        user_tags_source = user_tags_source.reset_index(drop=True)
#        print(user_tags_source)
        
        user_tags = [num + 1 for num in user_tags]
        user_tags.append(0)
        user_tags.append(1)
        user_tags.sort()
        df = comb_tags(tags, operators_data, user_tags)
    #    print(df)
        df = tags_parse[tags_parse['Tag'].isin(df)].index
    #    print(df)
        final_tags = list(user_tags_source[user_tags_source['Tag'].isin(df)].index)
    #    print(final_tags)
        if not final_tags:
            final_tags = ''
        final_tags = ''.join(str(num) for num in final_tags)
        return final_tags
    except:
        return 'X'

def click_tags(moveTo_x, moveTo_y, dragTo_x, dragTo_y, click_x, click_y, operators_data, tags):
    action_start('Arknights', 1242, 812, 339, 164)
    pyautogui.hotkey('win','shift','t')
    time.sleep(1)

    pyautogui.moveTo(moveTo_x, moveTo_y)
    pyautogui.mouseDown()
    pyautogui.moveTo(dragTo_x, dragTo_y, 1)
    time.sleep(.6)
    pyautogui.mouseUp()
    time.sleep(5)

    action_start('Arknights', 1242, 812, 339, 164)
    text = pyperclip.paste()
    if not any(x in text for x in ['H', 'a', 'n', 'l', 'x', 'p', 'd']):
        pyautogui.click(x=click_x, y=click_y)
        time.sleep(1)
        
        action_start('Arknights', 1242, 812, 339, 164)
        pyautogui.hotkey('win','shift','t')
        time.sleep(1)
        
        pyautogui.moveTo(698, 578)
        pyautogui.mouseDown()
        pyautogui.moveTo(1173, 701, 1)
        time.sleep(.6)
        pyautogui.mouseUp()
        time.sleep(1)
        
        action_start('Arknights', 1242, 812, 339, 164)
        input_tags = pyperclip.paste()
        input_tags = normalize(input_tags)
        input_tags = get_tags(operators_data, tags, input_tags)
        if '0' in input_tags:
            pyautogui.click(x=775, y=608)
            time.sleep(.6)
        if '1' in input_tags:
            pyautogui.click(x=781, y=676)
            time.sleep(.6)
        if '2' in input_tags:
            pyautogui.click(x=928, y=601)
            time.sleep(.6)
        if '3' in input_tags:
            pyautogui.click(x=935, y=678)
            time.sleep(.6)
        if '4' in input_tags:
            pyautogui.click(x=1095, y=605)
            time.sleep(.6)
        if input_tags != 'X':
            pyautogui.click(x=782, y=521)
            time.sleep(.6)
            pyautogui.click(x=1277, y=794)
        else:
            log_it("Recruitment interrupted")
            pyautogui.click(x=426, y=239)
        time.sleep(9)
    time.sleep(1)
    
def big_out():
    action_start('Arknights', 1242, 812, 339, 164)
    count = 10
    while count > 0:
        time.sleep(.6)
        keyboard.press_and_release('esc')
        count = count - 1
    action_start('Arknights', 1242, 812, 339, 164)
    count = 5
    while count > 0:
        time.sleep(.6)
        pyautogui.click(x=769, y=713)
        count = count - 1
    
def log_it(name):
    print(name)
    log_dir = r'C:\Users\User\Desktop\ark\logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    log_file = os.path.join(log_dir, 'ark_log.log')
    
    # Create the log entry manually
    log_entry = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {name}\n"
    
    # Read the current content of the log file
    if os.path.exists(log_file):
        with open(log_file, 'r') as file:
            old_content = file.read()
    else:
        old_content = ""
    
    # Write the new log entry followed by the old content
    with open(log_file, 'w') as file:
        file.write(log_entry + old_content)

def resource_menu():
    action_start('Arknights', 1242, 812, 339, 164)
    time.sleep(.6)
    pyautogui.click(x=1311, y=843)
    time.sleep(10)
    count = 2
    while count > 0:
        action_start('Arknights', 1242, 812, 339, 164)
        pyautogui.moveTo(1530, 873)
        pyautogui.mouseDown()
        pyautogui.moveTo(1062, 897, 1)
        time.sleep(.6)
        pyautogui.mouseUp()
        time.sleep(1)
        count = count - 1
    pyautogui.click(x=1400, y=527)
    time.sleep(1)
    pyautogui.click(x=604, y=879)
    time.sleep(1)
    pyautogui.click(x=933, y=702)
    time.sleep(1)
    pyautogui.click(x=464, y=417)
    time.sleep(1)
    
def start_farm():
    action_start('Arknights', 1242, 812, 339, 164)
    pyautogui.click(x=1440, y=919)
    time.sleep(3)
    pyautogui.click(x=1400, y=722)

def drag_down():
    pyautogui.moveTo(1550, 953) # move rest
    pyautogui.mouseDown()
    pyautogui.moveTo(1550, 218, 1)
    time.sleep(1)
    pyautogui.mouseUp()
    time.sleep(.6)
    
def find_obs_path():
    obs_path = os.getenv("OBS_PATH")
    if obs_path:
        return obs_path

    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall") as key:
            for i in range(0, winreg.QueryInfoKey(key)[0]):
                subkey_name = winreg.EnumKey(key, i)
                with winreg.OpenKey(key, subkey_name) as subkey:
                    try:
                        name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                        if "OBS Studio" in name:
                            install_location = winreg.QueryValueEx(subkey, "InstallLocation")[0]
                            return install_location
                    except FileNotFoundError:
                        continue
    except Exception as e:
        print(f"Error accessing registry: {e}")

    common_install_dirs = [r"C:\Program Files", r"C:\Program Files (x86)"]
    for start_dir in common_install_dirs:
        for root, dirs, files in os.walk(start_dir):
            if "obs64.exe" in files:
                return root

    return None