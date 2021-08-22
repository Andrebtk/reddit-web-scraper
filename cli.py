import reddit
import os
from termcolor import colored
import time
import sys
from tqdm import tqdm

term = "\033[92muser@reddit_parser\033[95m:\033[94m~\033[95m$ \033[0m"




while True:

    command = str(input(term))
    
    print(command)
    if command == "help":
        
        function="""[!]list of all function/command: 
        init_driver(): -> 
                        no argument
                        initalise driver
                        return driver

        main(sub, driver): -> 
                        sub is a string of a subreddit
                        driver is the driver returned by init_driver()

        pngToJpg(directory): ->
                        directory is the directory you want to convert png
                        to jpg

        parser(maxMeme, driver): ->
                        maxMeme is the number post you want to download
                        driver is the driver returned by init_driver()
                        and after being passed to main()

        for other function see reddit.py source code !


        [!]parser command usage: ->
                        -sub "[your subreddit]"
                        -n [number of meme you want to download]
                        -di [directory where you want the post to be download]
        """
        print(function)

    if "parser" in command :

        
        parsed = command.split()
        sub=""
        n=0
        di=""


        for x in range(len(parsed)):
            if parsed[x] == "-sub": sub=parsed[x+1]
            if parsed[x] == "-n": n=parsed[x+1]
            if parsed[x] == "-di": di=parsed[x+1] 

        driver = reddit.init_driver()
        reddit.main(sub,driver)
        reddit.parser(n,driver, di+"/")