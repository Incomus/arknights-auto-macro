import os
import subprocess
from .functions import functions_ark as ark
import sys

ark.log_it(f'Started {os.path.basename(__file__)}')

if len(sys.argv) > 1:
    week_schedule = sys.argv[1]
else:
    week_schedule = '1'

env = os.environ.copy()
env["PYTHONPATH"] = os.path.dirname(os.path.abspath(__file__))


subprocess.run(["python", "-m", "ark.record_start"], env=env)
subprocess.run(["python", "-m", "ark.1_start", week_schedule], env=env)
subprocess.run(["python", "-m", "ark.record_stop"], env=env)
ark.log_it(f'Ended {os.path.basename(__file__)}')
subprocess.Popen(["python", "-m", "ark.hibernate"], env=env)