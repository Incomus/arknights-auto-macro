import pyautogui
from .functions import functions_ark as ark
import os
import subprocess
import time
import keyboard
from win32api import GetSystemMetrics
ark.log_it(f'Started {os.path.basename(__file__)}')

time.sleep(1)

ark.log_it(f'Ended {os.path.basename(__file__)}')