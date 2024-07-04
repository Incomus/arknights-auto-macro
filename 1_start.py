import time as tm
import os
from .functions import functions_ark as ark
import datetime
import subprocess
import sys


event = True # if event is running it's generally prefered to farm that event instead
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
    
ark.log_it(f'Started {os.path.basename(__file__)}, {text}')
    
env = os.environ.copy()
env["PYTHONPATH"] = os.path.dirname(os.path.abspath(__file__))

def general_start():
    subprocess.run(["python", "-m", "arknights-auto-macro.record_start"], env=env)
    tm.sleep(1)
    subprocess.run(["python", "-m", "arknights-auto-macro.start"], env=env)
    tm.sleep(1)
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
    # this is a little unreliable. my time zone is switching arknights day at 2 pm and neither do I have any actions between 12 am - 1 am
    # god (chatgpt) help you if your time zone is switching at 12 am or you want to run between 12 to 1 am
    if datetime.time(1, 00) <= datetime.datetime.now().time() <= datetime.time(14, 00):
        weekday = weekday - 1
        if weekday < 0:
            weekday = 6
    if event == True: # if event is running it's generally prefered to farm that event instead
        weekday = 777
    if weekday in [0, 3, 5, 6]: # setup your own schedule here
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
    # new arknights day starts for me at 2 pm, at 2 am I run last farm of the day
    # as such it is better to run all farms and then collect mission for their better completion
    if datetime.time(1, 00) <= datetime.datetime.now().time() <= datetime.time(14, 00): 
        subprocess.run(["python", "-m", "arknights-auto-macro.game.main.credit"], env=env)
        tm.sleep(1)
        subprocess.run(["python", "-m", "arknights-auto-macro.game.main.mission"], env=env)
        tm.sleep(1)
    subprocess.run(["python", "-m", "arknights-auto-macro.stop"], env=env)
    tm.sleep(1)
    subprocess.run(["python", "-m", "arknights-auto-macro.record_stop"], env=env)
    tm.sleep(1)
    ark.log_it(f'Ended {os.path.basename(__file__)}, {text}')
    tm.sleep(1)
    subprocess.Popen(["python", "-m", "arknights-auto-macro.hibernate"], env=env)

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

def rest(): # this should run 6 hours after work out
    subprocess.run(["python", "-m", "arknights-auto-macro.record_start"], env=env)
    tm.sleep(1)
    subprocess.run(["python", "-m", "arknights-auto-macro.start"], env=env)
    tm.sleep(1)
    subprocess.run(["python", "-m", "arknights-auto-macro.game.main.login"], env=env)
    tm.sleep(1)
    subprocess.run(["python", "-m", "arknights-auto-macro.game.base.enter"], env=env)
    tm.sleep(1)
    subprocess.run(["python", "-m", "arknights-auto-macro.game.base.rest"], env=env)
    tm.sleep(1)
    subprocess.run(["python", "-m", "arknights-auto-macro.stop"], env=env)
    tm.sleep(1)
    subprocess.run(["python", "-m", "arknights-auto-macro.record_stop"], env=env)
    tm.sleep(1)
    ark.log_it(f'Ended {os.path.basename(__file__)}, {text}')
    tm.sleep(1)
    subprocess.Popen(["python", "-m", "arknights-auto-macro.hibernate"], env=env)
    

if week_schedule == '0':
    work_in()

if week_schedule == '1':
    work()
    
if week_schedule == '2':
    work_out()
    
if week_schedule == '3':
    rest()

