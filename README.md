# reddit_scraper [BETA]

this is a beta of an reddit parser coded in python



## Installation
```bash
pip install selenium
pip install urllib3
pip install beautifulsoup4
pip install Pillow
```

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
