import psutil
import time

seconds = 5

while True:
    # This will print the CPU usage in percentage
    cpu_usage = psutil.cpu_percent()

    # This will print the memory usage in percentage
    memory_usage = psutil.virtual_memory().percent

    # This will print the CPU and Memory usage in a formatted string
    output = f"CPU Usage: {cpu_usage}% Memory Usage: {memory_usage}"
    print(output)

    # Extending the script to write the data to a file
    with open("monitoring-log.txt", "a") as file:
        file.write(f"{output}\n")

    # time interval for the loop
    time.sleep(seconds)
