import psutil
import time

# memory_usage

while True:
    # This will print the CPU usage in percentage
    cpu_usage = psutil.cpu_percent()

    print(f"CPU Usage: {cpu_usage}%")

    # time interval for the loop
    time.sleep(1)
