# reddit_scraper [BETA]

this is a beta of an reddit scraper coded in python
[!]mainly tested on linux, using it on other os may need litle fix's
execute python3 cli.py to have a command line interface or you can directly use the function inside of reddit.py
if you use the cli.py, type "help" to see the different function and command 



## How does it work :
this python scraper use the selenium library for python, with this library you can manipulate a web browser only by using python code. Then the code launch firefox in headless mode (without actual browser window) using geckodriver. Then it access the given url and render it in a window size of 1222 by 4000, so that a lot of the post of this subreddit is loaded and that the html can be accessed. Then it access each div where there is a post and download it and use the title of the post as the name of the image in the directory where
you indicated to download it.

## Installation
```bash
pip install selenium
pip install urllib3
pip install beautifulsoup4
pip install Pillow
```
# Geckodriver
You need to install the latest version of geckodriver depending on your os and add it to your executable PATH

[Linux] -> https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-linux64.tar.gz.asc
[Windowd] -> https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-win64.zip
[Mac] -> https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-macos.tar.gz

website where you can sell all version: https://github.com/mozilla/geckodriver/releases

## Usage
```bash
python3 cli.py
```
then

```bash

user@reddit_parser:~$ scraper -sub https://www.reddit.com/r/HolUp/ -n 5 -di newMeme/
```
-sub -> the subreddit you want to download from

-n -> number of post you want to download

-di -> the directory where you want the post to be download (add / at the end [IMPORTANT])

## Other usage
you can directly use the reddit.py as an library and use the function inside
