import os
import sys
import time

env_str = os.environ.get('CPU_LOAD')

if env_str:
    try:
        cpu_percentage = int(env_str)
        print("CPU load:", cpu_percentage)
    except ValueError:
        print("Error: CPU load not valid")
else:
    print("cpu load NOT configured")
    sys.exit()

busy_time = float(cpu_percentage) / 100
idle_time = 1 - busy_time

while True:
    time.sleep(idle_time)

    start_time = time.time()
    end_time = start_time + busy_time

    while True:
        current_time = time.time()
        if current_time >= end_time:
            break
