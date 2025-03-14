import psutil
import time


seconds = 5

while True:
    # This will print the CPU usage in percentage
    cpu_usage = psutil.cpu_percent()

    # This will print the memory usage in percentage
    memory_usage = psutil.virtual_memory().percent

    print(f"CPU Usage: {cpu_usage}% Memory Usage: {memory_usage}")
    # print(f"CPU Usage: {cpu_usage}%")

    # time interval for the loop
    time.sleep(seconds)
