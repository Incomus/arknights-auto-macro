import time
from .functions import functions_ark as ark
import os

ark.log_it(f'Started {os.path.basename(__file__)}')

w = ark.action_start('Arknights', 1242, 812, 339, 164)
time.sleep(.5)
w.restore()
time.sleep(.5)
w = ark.action_start('Arknights', 1242, 812, 339, 164)
time.sleep(.5)
w.close()
time.sleep(1)
os.system("taskkill /f /im crosvm.exe")
time.sleep(1)
os.system("taskkill /f /im crosvm.exe")

ark.log_it(f'Ended {os.path.basename(__file__)}')