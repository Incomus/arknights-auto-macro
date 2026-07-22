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
import sys
import win32gui
import win32con
import pywinauto
import difflib
import psutil
import pandas as pd
import subprocess
import traceback

class WindowMgr:
    def __init__(self):
        self._handle = None

    def _window_enum_callback(self, hwnd, wildcard):
        """Pass to win32gui.EnumWindows() to check all open windows"""
        if wildcard in win32gui.GetWindowText(hwnd):
            if win32gui.IsWindowVisible(hwnd) and not win32gui.GetParent(hwnd):
                self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)
        if not self._handle:
            raise Exception(f"No window found matching: {wildcard}")

    def minimize_window(self):
        if self._handle is not None and self._handle != 0:
            win32gui.ShowWindow(self._handle, win32con.SW_MINIMIZE)
        else:
            raise Exception("Invalid window handle")

    def close_window(self):
        if self._handle is not None and self._handle != 0:
            win32gui.PostMessage(self._handle, win32con.WM_CLOSE, 0, 0)
        else:
            raise Exception("Invalid window handle")


def action_start(title, resize_x, resize_y, move_x, move_y):
    if title == "Arknights":
        resize_x = 1319 #1242
        resize_y = 812
        move_x = 269 #339
        move_y = 160 #164
    try:
        w = WindowMgr()
        w.find_window_wildcard(title)
        
        win32gui.ShowWindow(w._handle, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(w._handle)
        
        win32gui.MoveWindow(w._handle, move_x, move_y, resize_x, resize_y, True)
        time.sleep(0.5)
        return w
    except Exception as e:
        print(f"Error action_start: {title}, {e}")
        log_it(f"Error action_start: {title}, {e}")
        sys.exit()
        

def normalize(text):
    text = text.replace('\n', ',').replace('\r', ',').replace(',,', ',')
    text = text.split(',')
    text = ["Mlynar" if "mkynar" in x.lower() else x for x in text]
    text = ["Zima" if "tima" in x.lower() else x for x in text]
    text = ["Greyy" if "grew" in x.lower() else x for x in text]
    try:
        for element in text:
            if element in ['', ' ']:
                text.remove(element)
    except:
        x = None
    return text

def normalize_tags(text, possible_inputs):
    normalized_text = []
    
    for phrase in text:
        # Split the phrase into individual words
        words = phrase.split()
        print(words)
        for word in words:
            # Clean the word
            word_cleaned = word.replace(' ', '').replace('•', '').replace('.', '').lower()
            print(word_cleaned)
            # Find the closest match from possible_inputs
            match = difflib.get_close_matches(word_cleaned, [x.lower() for x in possible_inputs], n=1, cutoff=0.6)
            print(match)
            if match:
                # Find the original case-sensitive match in possible_inputs
                original_match = next((x for x in possible_inputs if x.lower() == match[0]), word)
                normalized_text.append(original_match)
            else:
                # Handle case where no close match is found (optional)
                normalized_text.append(None)  # You can also choose to append the original word or skip it
    normalized_text = [word for word in normalized_text if word is not None]
    return normalized_text
    
    

    
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
                                input_tags[tag3_index] == 28 and \
                                manual == True:
                            log_it("Recruitment manual senior op!")
                            raise ValueError('manual senior op')
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
            return tags_parse[tags_parse['Tag'].str.lower() == tag.lower()].index[0]
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


def get_ptoys(moveTo_x, moveTo_y, dragTo_x, dragTo_y):
    action_start('Arknights', 1242, 812, 339, 164)
    pyautogui.hotkey('win','shift','t')
    time.sleep(2)
    pyautogui.moveTo(moveTo_x, moveTo_y)
    time.sleep(.6)
    pyautogui.mouseDown()
    time.sleep(.6)
    pyautogui.mouseDown()
    time.sleep(.6)
    pyautogui.moveTo(dragTo_x, dragTo_y, 1)
    time.sleep(.6)
    pyautogui.mouseUp()
    time.sleep(.6)
    pyautogui.mouseUp()
    time.sleep(1)
    pyautogui.click(x=1435, y=36)
    time.sleep(.5)
    action_start('Arknights', 1242, 812, 339, 164)
    time.sleep(.5)
    pyautogui.click(x=1152, y=944)
    time.sleep(.1)

def click_tags(moveTo_x, moveTo_y, dragTo_x, dragTo_y, click_x, click_y, operators_data, tags):
    action_start('Arknights', 1242, 812, 339, 164)
    get_ptoys(moveTo_x, moveTo_y, dragTo_x, dragTo_y)
    action_start('Arknights', 1242, 812, 339, 164)
    text = pyperclip.paste()
    if not any(x in text.lower() for x in ['h', 'a', 'l', 'x', 'p', 'd']):
        pyautogui.click(x=click_x, y=click_y)
        time.sleep(1)
        repeat = 0
        while True:
            if repeat > 5:
                break
            get_ptoys(698, 578, 1173, 701)
            
            input_tags = pyperclip.paste()
            input_tags = normalize(input_tags)
            input_tags = normalize_tags(input_tags, tags[2:])
            log_it(f'Tags: {input_tags}')
            input_tags = get_tags(operators_data, tags, input_tags)
            result = False
            if input_tags == 'X':
                break
            if '0' in input_tags:
                pyautogui.click(x=775, y=608)
                time.sleep(.6)
                result = True
            if '1' in input_tags:
                pyautogui.click(x=781, y=676)
                time.sleep(.6)
                result = True
            if '2' in input_tags:
                pyautogui.click(x=928, y=601)
                time.sleep(.6)
                result = True
            if '3' in input_tags:
                pyautogui.click(x=935, y=678)
                time.sleep(.6)
                result = True
            if '4' in input_tags:
                pyautogui.click(x=1095, y=605)
                time.sleep(.6)
                result = True
            if not result:
                text_prev = pyperclip.paste()
                get_ptoys(1224, 669, 1337, 695)
                text = pyperclip.paste()
                if any(x in text.lower() for x in ['p', 'e', 'f', 's']) and text != text_prev:
                    pyautogui.click(x=1274, y=628)
                    time.sleep(.6)
                    pyautogui.click(x=1113, y=714)
                    time.sleep(1)
                else:
                    break
            else:
                break
            repeat += 1
        if input_tags != 'X':
            pyautogui.click(x=782, y=521)
            time.sleep(.6)
            pyautogui.click(x=1277, y=794)
        else:
            log_it("Recruitment interrupted")
            pyautogui.click(x=426, y=239)
        time.sleep(9)
    time.sleep(1)
    
def big_out(count=10, click=True):
    action_start('Arknights', 1242, 812, 339, 164)
    while count > 0:
        time.sleep(2)
        keyboard.press_and_release('esc')
        count = count - 1
    action_start('Arknights', 1242, 812, 339, 164)
    if click:
        count = 5
        while count > 0:
            time.sleep(.6)
            pyautogui.click(x=769, y=713)
            count = count - 1
    
def log_it(name):
    try:
        print(name)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Determine the parent directory of the script directory
        parent_dir = os.path.dirname(script_dir)
        
        # Define the log directory in the parent directory
        log_dir = os.path.join(parent_dir, 'logs')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        log_file = os.path.join(log_dir, 'ark_log.log')
        
        # Create the log entry manually
        log_entry = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {name}\n"
        
        # Append the new log entry to the log file
        with open(log_file, 'a', encoding='utf-8') as file:
            file.write(log_entry)
    
    except Exception as e:
        print(f"An error occurred: {e}")

def resource_menu():
    action_start('Arknights', 1242, 812, 339, 164)
    time.sleep(.6)
    pyautogui.click(x=1311, y=843)
    time.sleep(10)
    pyautogui.click(x=1555, y=523)
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
    action_start('Arknights', 1242, 812, 339, 164)
    pyautogui.click(x=400, y=919)
    pyautogui.moveTo(1550, 953) # move rest
    pyautogui.mouseDown()
    pyautogui.moveTo(1550, 218, 1)
    time.sleep(1)
    pyautogui.mouseUp()
    time.sleep(.6)

def drag_from_to(x1, y1, x2, y2):
    action_start('Arknights', 1242, 812, 339, 164)
    #pyautogui.click(x=400, y=919)
    pyautogui.moveTo(x1, y1) # move rest
    pyautogui.mouseDown()
    pyautogui.moveTo(x2, y2, 1)
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
    
def find_google_play_games_path():
    # Check if an environment variable is set
    google_play_games_path = os.getenv("GOOGLE_PLAY_GAMES_PATH")
    if google_play_games_path:
        return google_play_games_path

    # Search the Windows Registry
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall") as key:
            for i in range(0, winreg.QueryInfoKey(key)[0]):
                subkey_name = winreg.EnumKey(key, i)
                with winreg.OpenKey(key, subkey_name) as subkey:
                    try:
                        name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                        if "Google Play Games" in name:
                            install_location = winreg.QueryValueEx(subkey, "InstallLocation")[0]
                            if validate_google_play_games_path(install_location):
                                return install_location
                    except FileNotFoundError:
                        continue
    except Exception as e:
        print(f"Error accessing registry: {e}")

    # Search common installation directories
    common_install_dirs = [r"C:\Program Files", r"C:\Program Files (x86)"]
    for start_dir in common_install_dirs:
        for root, dirs, files in os.walk(start_dir):
            if "Bootstrapper.exe" in files:
                if validate_google_play_games_path(root):
                    return root

    return None

def validate_google_play_games_path(path):
    # Check for specific files and directories unique to Google Play Games
    expected_items = [
        "Bootstrapper.exe",
        "uninstaller.exe",
        os.path.join("current", "client", "client.exe")
    ]
    for item in expected_items:
        if not os.path.exists(os.path.join(path, item)):
            return False
    return True

def enum_windows_callback(hwnd, explorer_windows):
    window_text = win32gui.GetWindowText(hwnd)
    class_name = win32gui.GetClassName(hwnd)
    if class_name == "CabinetWClass":  # This is the class name for Windows Explorer windows
        explorer_windows.append(hwnd)

def close_explorer_windows():
    explorer_windows = []
    win32gui.EnumWindows(enum_windows_callback, explorer_windows)

    if explorer_windows:
        for hwnd in explorer_windows:
            win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)

def kill_w_name(name):
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # Check if 'powertoys' (lowercase) is in the process name (converted to lowercase)
            if name.lower() in proc.info['name'].lower():
                print(f"Killing {proc.info['name']} with PID {proc.info['pid']}")
                os.system(f"taskkill /F /PID {proc.info['pid']}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Handle errors if a process no longer exists or cannot be accessed
            pass
    time.sleep(10)

def print_process():
    process_list = []
    for proc in psutil.process_iter(['pid', 'name']):
        process_list.append(proc.info)

    # Converting the list of processes into a DataFrame
    df = pd.DataFrame(process_list)

    # Sorting the DataFrame by the 'name' column
    df_sorted = df.sort_values(by='name')

    # Displaying the sorted DataFrame
    print(df_sorted)

def run_with_error_handling(command, env):
    try:
        subprocess.run(command, env=env)
    except Exception:
        ark.log_it(traceback.format_exc())

