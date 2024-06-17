import time as tm
import os
from .functions import functions_ark as ark
import datetime
import subprocess
import schedule
import sys

ark.log_it(f'Started {os.path.basename(__file__)}')

if len(sys.argv) > 1:
    week_schedule = sys.argv[1]
    
env = os.environ.copy()
env["PYTHONPATH"] = os.path.dirname(os.path.abspath(__file__))

def general_start():
    subprocess.run(["python", "-m", "ark.start"], env=env)
    tm.sleep(1)
    subprocess.run(["python", "-m", "ark.game.main.login"], env=env)
    tm.sleep(1)
    subprocess.run(["python", "-m", "ark.game.main.get_recruit"], env=env)
    tm.sleep(1)
    subprocess.run(["python", "-m", "ark.game.main.recruit"], env=env)
    tm.sleep(1)
    subprocess.run(["python", "-m", "ark.game.base.enter"], env=env)
    tm.sleep(1)
    
def general_end():    
    subprocess.run(["python", "-m", "ark.game.base.drone_exp"], env=env)
    tm.sleep(1)
    if datetime.time(1, 00) <= datetime.datetime.now().time() <= datetime.time(5, 00):
        subprocess.run(["python", "-m", "ark.game.base.clue_claim"], env=env)
        tm.sleep(1)
    subprocess.run(["python", "-m", "ark.game.base.scout"], env=env)
    tm.sleep(1)
    subprocess.run(["python", "-m", "ark.game.base.exit"], env=env)
    tm.sleep(1)
    weekday = datetime.datetime.now().weekday()
    if datetime.time(1, 00) <= datetime.datetime.now().time() <= datetime.time(14, 00):
        weekday = weekday - 1
        if weekday < 0:
            weekday = 6
    if weekday in [0, 3, 5, 6]:
        subprocess.run(["python", "-m", "ark.game.farm.RC_120"], env=env)
        tm.sleep(1)
    elif weekday == 1:
        subprocess.run(["python", "-m", "ark.game.farm.agg_120"], env=env)
        tm.sleep(1)
    elif weekday == 2:
        subprocess.run(["python", "-m", "ark.game.farm.fib_120"], env=env)
        tm.sleep(1)
    elif weekday == 4:
        subprocess.run(["python", "-m", "ark.game.farm.gel_120"], env=env)
        tm.sleep(1)
    if datetime.time(1, 00) <= datetime.datetime.now().time() <= datetime.time(14, 00):
        subprocess.run(["python", "-m", "ark.game.main.credit"], env=env)
        tm.sleep(1)
        subprocess.run(["python", "-m", "ark.game.main.mission"], env=env)
        tm.sleep(1)
    subprocess.run(["python", "-m", "ark.stop"], env=env)
    tm.sleep(1)
    ark.log_it(f'Ended {os.path.basename(__file__)}')
    sys.exit()

def work_in():
    general_start()
    subprocess.run(["python", "-m", "ark.game.base.clear_rest"], env=env)
    tm.sleep(1)
    subprocess.run(["python", "-m", "ark.game.base.work_2traders"], env=env)
    tm.sleep(1)
    general_end()

def work_out():
    general_start()
    subprocess.run(["python", "-m", "ark.game.base.collect"], env=env)
    tm.sleep(1)
    subprocess.run(["python", "-m", "ark.game.base.clear"], env=env)
    tm.sleep(1)
    subprocess.run(["python", "-m", "ark.game.base.rest"], env=env)
    tm.sleep(1)
    general_end()

def work():
    general_start()
    subprocess.run(["python", "-m", "ark.game.base.collect"], env=env)
    tm.sleep(1)
    general_end()

def rest():
    subprocess.run(["python", "-m", "ark.record_start"], env=env)
    tm.sleep(1)
    subprocess.run(["python", "-m", "ark.start"], env=env)
    tm.sleep(1)
    subprocess.run(["python", "-m", "ark.game.main.login"], env=env)
    tm.sleep(1)
    subprocess.run(["python", "-m", "ark.game.base.enter"], env=env)
    tm.sleep(1)
    subprocess.run(["python", "-m", "ark.game.base.rest"], env=env)
    tm.sleep(1)
    subprocess.run(["python", "-m", "ark.stop"], env=env)
    tm.sleep(1)
    subprocess.run(["python", "-m", "ark.record_stop"], env=env)
    tm.sleep(1)
    ark.log_it(f'Ended {os.path.basename(__file__)}')
    sys.exit()
    

schedule.every().day.at('20:10').do(rest)
schedule.every().day.at('08:10').do(rest)

if week_schedule == '0':
    schedule.every().day.at('14:00').do(work_in)
    schedule.every().day.at('02:00').do(work_in)

if week_schedule == '1':
    schedule.every().day.at('14:00').do(work)
    schedule.every().day.at('02:00').do(work)
    
if week_schedule == '2':
    schedule.every().day.at('14:00').do(work_out)
    schedule.every().day.at('02:00').do(work_out)
    
if week_schedule == '3':
    schedule.every().day.at('14:00').do(rest)
    schedule.every().day.at('02:00').do(rest)

while True:
    schedule.run_pending()
    tm.sleep(1)