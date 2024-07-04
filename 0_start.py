import os
import subprocess
from .functions import functions_ark as ark
import sys
import time as tm

ark.log_it(f'Started {os.path.basename(__file__)}')

if len(sys.argv) > 1:
    week_schedule = sys.argv[1]
else:
    week_schedule = '1'

if week_schedule == '0':
    text = 'work_in'

if week_schedule == '1':
    text = 'work'
    
if week_schedule == '2':
    text = 'work_out'
    
if week_schedule == '3':
    text = 'rest'

ark.log_it(f'Started {text}')
env = os.environ.copy()
env["PYTHONPATH"] = os.path.dirname(os.path.abspath(__file__))


subprocess.run(["python", "-m", "arknights-auto-macro.record_start"], env=env)
tm.sleep(1)
subprocess.run(["python", "-m", "arknights-auto-macro.start"], env=env)
tm.sleep(1)
subprocess.run(["python", "-m", "arknights-auto-macro.1_start", week_schedule], env=env)
tm.sleep(1)
subprocess.run(["python", "-m", "arknights-auto-macro.stop"], env=env)
tm.sleep(1)
subprocess.run(["python", "-m", "arknights-auto-macro.record_stop"], env=env)
tm.sleep(1)
ark.log_it(f'Ended {os.path.basename(__file__)}')
tm.sleep(1)
subprocess.Popen(["python", "-m", "arknights-auto-macro.hibernate"], env=env)
