import os
import time

while True:
    files = os.listdir(".")
    if files:
        for file in files:
            if file.endswith(".txt"):
                with open(file, "r") as file_content:
                    content = file_content.read()
                print(f"Filename: {file}, Content: {content}")
    time.sleep(5)

