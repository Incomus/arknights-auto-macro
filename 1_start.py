import time as tm
import os
from .functions import functions_ark as ark
import datetime
import subprocess
import sys
import traceback


event = True
red_cred = False
event_ignore = '0'

if len(sys.argv) > 1:
    week_schedule = sys.argv[1]
else:
    week_schedule = '1'

if week_schedule == '0':
    text = 'work_main'

if week_schedule == '1':
    text = 'work'
    
if week_schedule == '2':
    text = 'work_trash'
    
if week_schedule == '3':
    text = 'rest_main'
    
if week_schedule == '4':
    text = 'rest_trash'
    
ark.log_it(f'Started {os.path.basename(__file__)}, {text}')
    
env = os.environ.copy()
env["PYTHONPATH"] = os.path.dirname(os.path.abspath(__file__))
def general_start():
    #ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.record_start"], env=env)
    #tm.sleep(1)
    #ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.internet_start"], env=env)
    #tm.sleep(1)
    ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.start"], env=env)
    tm.sleep(1)
    ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.run_ark"], env=env)
    tm.sleep(1)
    ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.main.login"], env=env)
    tm.sleep(1)
    weekday = datetime.datetime.now().weekday()
    if datetime.time(1, 00) <= datetime.datetime.now().time() <= datetime.time(14, 00):
        weekday = weekday - 1
        if weekday < 0:
            weekday = 6
    if datetime.datetime.now().time() <= datetime.time(14, 00) or (weekday in [0, 1, 2, 3] and datetime.datetime.now().time() >= datetime.time(14, 00)):
        ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.main.get_recruit"], env=env)
        tm.sleep(1)
        ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.main.recruit"], env=env)
        tm.sleep(1)
    ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.base.enter"], env=env)
    tm.sleep(1)
    
def general_end():
    if datetime.time(1, 00) <= datetime.datetime.now().time() <= datetime.time(14, 00):
        ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.base.clue_claim"], env=env)
        tm.sleep(1)
    ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.base.scout"], env=env)
    tm.sleep(1)
    ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.base.exit"], env=env)
    tm.sleep(1)
    weekday = datetime.datetime.now().weekday()
    if datetime.time(1, 00) <= datetime.datetime.now().time() <= datetime.time(14, 00):
        weekday = weekday - 1
        if weekday < 0:
            weekday = 6
    if event == True:
        weekday = 777
    elif red_cred == True:
        weekday = 888
    if weekday in [0, 3, 5, 6]:
        ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.farm.RC_120"], env=env)
        tm.sleep(1)
    elif weekday == 4:
        # ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.farm.chip_med_def"], env=env)
        ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.farm.rock_105"], env=env)
        tm.sleep(1)
    elif weekday == 1:
        # if datetime.datetime.now().time() <= datetime.time(14, 00):
            # ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.farm.annihil"], env=env)
            # tm.sleep(1)
        # else:
        # ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.farm.chip_sni_cas"], env=env)
        ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.farm.rock_105"], env=env)
        tm.sleep(1)
    elif weekday == 2:
        # ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.farm.chip_van_sup"], env=env)
        ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.farm.rock_105"], env=env)
        tm.sleep(1)
    elif weekday == 777:
        ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.farm.event"], env=env)
        tm.sleep(1)
    elif weekday == 888:
        ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.farm.RC_120"], env=env)
        tm.sleep(1)
    if datetime.time(1, 00) <= datetime.datetime.now().time() <= datetime.time(14, 00):
        ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.main.credit"], env=env)
        tm.sleep(1)
        ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.main.mission"], env=env)
        tm.sleep(1)
    ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.stop"], env=env)
    tm.sleep(1)
    #ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.record_stop"], env=env)
    ark.run_with_error_handling(["taskkill", "/F", "/IM", "obs64.exe"], env=env)
    tm.sleep(1)
    ark.log_it(f'Ended {os.path.basename(__file__)}, {text}')
    tm.sleep(1)
    subprocess.Popen(["python", "-m", "arknights-auto-macro.hibernate"], env=env)

def work_main():
    general_start()
    ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.base.change_shift"], env=env)
    tm.sleep(1)
    ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.base.collect"], env=env)
    tm.sleep(1) 
    #ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.base.drone_exp"], env=env)
    ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.base.drone_lmd"], env=env)
    tm.sleep(1)
    ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.base.rest_trash"], env=env)
    tm.sleep(1)
    general_end()

def work_trash():
    tm.sleep(1800)
    general_start()
    ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.base.change_shift"], env=env)
    tm.sleep(1)
    ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.base.rest_main"], env=env)
    tm.sleep(1)
    ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.base.collect"], env=env)
    tm.sleep(1) 
    ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.base.drone_lmd"], env=env)
    tm.sleep(1)
    general_end()

def work():
    general_start()
    ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.base.collect"], env=env)
    tm.sleep(1)
    #ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.base.drone_exp"], env=env)
    ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.base.drone_lmd"], env=env)
    tm.sleep(1)    
    general_end()

def rest_main():
    general_start()
    ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.base.rest_main"], env=env)
    tm.sleep(1)
    ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.base.collect"], env=env)
    tm.sleep(1)
    ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.base.drone_lmd"], env=env)
    tm.sleep(1) 
    general_end()

def rest_trash():
    general_start()
    ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.base.rest_trash"], env=env)
    tm.sleep(1)
    ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.base.collect"], env=env)
    tm.sleep(1)
    #ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.base.drone_exp"], env=env)
    ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.game.base.drone_lmd"], env=env)
    tm.sleep(1) 
    general_end()
    

try:
    if week_schedule == '0':
        work_main()

    if week_schedule == '1':
        work()
        
    if week_schedule == '2':
        work_trash()
        
    if week_schedule == '3':
        rest_main()
        
    if week_schedule == '4':
        rest_trash()
except Exception:
    ark.log_it(traceback.format_exc())
    ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.stop"], env=env)
    tm.sleep(1)
    #ark.run_with_error_handling(["python", "-m", "arknights-auto-macro.record_stop"], env=env)
    ark.run_with_error_handling(["taskkill", "/F", "/IM", "obs64.exe"], env=env)
    tm.sleep(1)
    ark.log_it(f'Ended {os.path.basename(__file__)}, {text}')
    tm.sleep(1)
    subprocess.Popen(["python", "-m", "arknights-auto-macro.hibernate"], env=env)