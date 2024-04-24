import sys
import time
import subprocess

cpu_percentage = sys.argv[1]

if not cpu_percentage:
    print("error")
    sys.exit(1)

busy_time = float(cpu_percentage) / 100
idle_time = 1 - busy_time

print("busy ", busy_time)
print("idle ", idle_time)

while True:
    time.sleep(idle_time)

    start_time = time.time()
    end_time = start_time + busy_time

    while True:
        current_time = time.time()
        if current_time >= end_time:
            break
