import time as tm
import os
from .functions import functions_ark as ark
import datetime
import subprocess
import sys

ark.log_it(f'Started {os.path.basename(__file__)}')

event = True
if len(sys.argv) > 1:
    week_schedule = sys.argv[1]
    
env = os.environ.copy()
env["PYTHONPATH"] = os.path.dirname(os.path.abspath(__file__))

def general_start():
    subprocess.run(["python", "-m", "arknights-auto-macro.game.main.login"], env=env)
    tm.sleep(1)
    subprocess.run(["python", "-m", "arknights-auto-macro.game.main.get_recruit"], env=env)
    tm.sleep(1)
    subprocess.run(["python", "-m", "arknights-auto-macro.game.main.recruit"], env=env)
    tm.sleep(1)
    subprocess.run(["python", "-m", "arknights-auto-macro.game.base.enter"], env=env)
    tm.sleep(1)
    
def general_end():
    if datetime.time(1, 00) <= datetime.datetime.now().time() <= datetime.time(5, 00):
        subprocess.run(["python", "-m", "arknights-auto-macro.game.base.clue_claim"], env=env)
        tm.sleep(1)
    subprocess.run(["python", "-m", "arknights-auto-macro.game.base.scout"], env=env)
    tm.sleep(1)
    subprocess.run(["python", "-m", "arknights-auto-macro.game.base.exit"], env=env)
    tm.sleep(1)
    weekday = datetime.datetime.now().weekday()
    if datetime.time(1, 00) <= datetime.datetime.now().time() <= datetime.time(14, 00):
        weekday = weekday - 1
        if weekday < 0:
            weekday = 6
    if event == True:
        weekday = 777
    if weekday in [0, 3, 5, 6]:
        subprocess.run(["python", "-m", "arknights-auto-macro.game.farm.RC_120"], env=env)
        tm.sleep(1)
    elif weekday == 1:
        subprocess.run(["python", "-m", "arknights-auto-macro.game.farm.agg_120"], env=env)
        tm.sleep(1)
    elif weekday == 2:
        subprocess.run(["python", "-m", "arknights-auto-macro.game.farm.fib_120"], env=env)
        tm.sleep(1)
    elif weekday == 4:
        subprocess.run(["python", "-m", "arknights-auto-macro.game.farm.gel_120"], env=env)
        tm.sleep(1)
    elif weekday == 777:
        subprocess.run(["python", "-m", "arknights-auto-macro.game.farm.event"], env=env)
        tm.sleep(1)
    if datetime.time(1, 00) <= datetime.datetime.now().time() <= datetime.time(14, 00):
        subprocess.run(["python", "-m", "arknights-auto-macro.game.main.credit"], env=env)
        tm.sleep(1)
        subprocess.run(["python", "-m", "arknights-auto-macro.game.main.mission"], env=env)
        tm.sleep(1)
    ark.log_it(f'Ended {os.path.basename(__file__)}')
    sys.exit()

def work_in():
    general_start()
    subprocess.run(["python", "-m", "arknights-auto-macro.game.base.clear_rest"], env=env)
    tm.sleep(1)
    subprocess.run(["python", "-m", "arknights-auto-macro.game.base.pick"], env=env)
    tm.sleep(1)
    subprocess.run(["python", "-m", "arknights-auto-macro.game.base.drone_exp"], env=env)
    tm.sleep(1)
    subprocess.run(["python", "-m", "arknights-auto-macro.game.base.collect"], env=env)
    tm.sleep(1) 
    general_end()

def work_out():
    general_start()
    subprocess.run(["python", "-m", "arknights-auto-macro.game.base.collect"], env=env)
    tm.sleep(1)    
    subprocess.run(["python", "-m", "arknights-auto-macro.game.base.drone_exp"], env=env)
    tm.sleep(1)
    subprocess.run(["python", "-m", "arknights-auto-macro.game.base.clear"], env=env)
    tm.sleep(1)
    subprocess.run(["python", "-m", "arknights-auto-macro.game.base.rest"], env=env)
    tm.sleep(1)
    general_end()

def work():
    general_start()
    subprocess.run(["python", "-m", "arknights-auto-macro.game.base.collect"], env=env)
    tm.sleep(1)    
    subprocess.run(["python", "-m", "arknights-auto-macro.game.base.drone_exp"], env=env)
    tm.sleep(1)
    general_end()

def rest():
    subprocess.run(["python", "-m", "arknights-auto-macro.game.main.login"], env=env)
    tm.sleep(1)
    subprocess.run(["python", "-m", "arknights-auto-macro.game.base.enter"], env=env)
    tm.sleep(1)
    subprocess.run(["python", "-m", "arknights-auto-macro.game.base.rest"], env=env)
    tm.sleep(1)
    ark.log_it(f'Ended {os.path.basename(__file__)}')
    sys.exit()
    

if week_schedule == '0':
    work_in()

if week_schedule == '1':
    work()
    
if week_schedule == '2':
    work_out()
    
if week_schedule == '3':
    rest()

