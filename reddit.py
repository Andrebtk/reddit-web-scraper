from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver import Firefox
import selenium as se
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
import urllib.request
from bs4 import BeautifulSoup
import os
from PIL import Image
import sys


def init_driver():

    fp = se.webdriver.FirefoxProfile()

    options = se.webdriver.FirefoxOptions()
    options.headless = True
    options.log.level = "trace"
    driver = se.webdriver.Firefox(firefox_profile=fp, options=options)
    return driver

def main(sub, driver):

    meme_url=sub

    meme_url3 = "https://www.reddit.com/r/pcmasterrace/"
    meme_url2 = "https://www.reddit.com/r/pcmasterrace/top/?t=week"
    maxMeme2 = 30


    
    driver.set_window_size(1220, 4000)
    driver.get(meme_url)
    time.sleep(10)

def pngToJpg(directory):
    files = os.listdir(directory)    
    for file in files:
        if ".png" in file:
            im = Image.open(directory + file)
            newImage = im.convert('RGB')
            newImage.save(file+".jpg")
            os.system('rm '+directory+ file)
            print("[!]deleted -> " + file)

def url_save(url, i, directory):
    try: 
        if len(i) > 250: i = i[0:200]
        if " " in i: i = i.replace(" ","_")
        if "'" in i: i = i.replace("'","_")
        if "." in i: i = i.replace(".","")
        

        if ".png" in url: finish = ".png"
        elif ".jpg" in url: finish = ".jpg"
        else :
            print("ffmpeg -i "+ url +" -bsf:a aac_adtstoasc -c copy "+i+".mp4") 
            os.system('ffmpeg -i "'+ url +'" -bsf:a aac_adtstoasc -c copy '+directory+""+i+'.mp4')
            time.sleep(5)
            return 0

        
        urllib.request.urlretrieve(url, directory+ "/" + str(i)+ finish)
    except:
        print("[!] error during url_save function")
        pass



def scrape(maxMeme, driver, directory):



    datas = driver.find_elements_by_class_name("_1oQyIsiPHYt6nx7VOmd1sz")
    memeUrls = driver.find_elements_by_class_name("_2_tDEnGMLxpM6uOa2kaDB3")
    upvote = driver.find_elements_by_css_selector("._1rZYMD_4xY3gRcSS3p8ODO._3a2ZHWaih05DgAOtvu6cIo")
    titles = driver.find_elements_by_class_name("_eYtD2XCVieq6emjKBH3m")
    memeData = driver.find_elements_by_class_name("_1oQyIsiPHYt6nx7VOmd1sz")
    maxMeme=int(maxMeme)


    del memeData[0]
    memeData = memeData[0:maxMeme]



    for data in memeData:
        html = data.get_attribute("innerHTML")
        
        
        soup = BeautifulSoup(html, 'lxml')
        title = soup.find('h3',class_="_eYtD2XCVieq6emjKBH3m")
        creator = soup.find('a',class_="_2tbHP6ZydRpjI44J3syuqC")
        
        memeUrlFather = soup.find("div", class_="_3JgI-GOrkmyIeDeyzXdyUD")
        
        if title is None: break
        
        memeVideo = memeUrlFather.find('source')
        memeImage = soup.find('img', class_="_2_tDEnGMLxpM6uOa2kaDB3")

        title = title.get_text()

        
        if memeVideo is not None : 

            print("[!]Downloading meme -> this meme is a video -> not implemented")

        if memeImage is not None :
            print("[!]Downloading meme -> this meme is a photo")

            
            url_save(memeImage['src'], title, directory + "/")    
        

    
