import time

while True:
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    filename = "time_file.txt"
    with open(filename, "w") as file:
        file.write(current_time)
    time.sleep(10)
