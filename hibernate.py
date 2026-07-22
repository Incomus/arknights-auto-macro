import os
from .functions import functions_ark as ark
import time

ark.log_it(f'Started {os.path.basename(__file__)}')
os.system("taskkill /f /im client.exe")
os.system("taskkill /f /im crosvm.exe")
os.system("taskkill /f /im Service.exe")
ark.kill_w_name('Powertoys')
countdown = 60

while countdown > 0:
    print(f"Waiting {countdown} seconds to hibernate...")
    time.sleep(1)
    countdown -= 1

# Execute hibernate command
os.system("shutdown /h")
