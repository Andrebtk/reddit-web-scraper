import os
from termcolor import colored
import time
import sys
from tqdm import tqdm

term = "\033[92minsta@pc_master_meme\033[95m:\033[94m~\033[95m$ \033[0m"
data = ""


while True:

    data = ""
    command = str(input(term))
    
    
    if command == "clean": data = "clean()"
    if command == "main": data = "main()"

    if command == "loading":
        for i in tqdm(range(20)):
            time.sleep(1)


    if data != "":
        os.system("ssh pi@192.168.1.37 'cd memeBot ; DISPLAY=:0 python3 -c \"from function import *; " + data + "\"'")

