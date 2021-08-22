# reddit_parser [BETA]

this is a beta of an reddit parser


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

```bash

user@reddit_parser:~$ parser -sub https://www.reddit.com/r/HolUp/ -n 5 -di newMeme/
```
-sub -> the subreddit you want to download from

-n -> number of post you want to download

-di -> the directory where you want the post to be download (add / at the end [IMPORTANT])

