from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver import Firefox, ActionChains
import selenium as se
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time



url = "https://www.tiktok.com/login/phone-or-email/email"

"""
proxies = ['51.158.119.88:8761', '51.158.119.88:8811']


PROXY = proxies[0]

webdriver.DesiredCapabilities.FIREFOX['proxy']={
    "httpProxy":PROXY,
    "ftpProxy":PROXY,
    "sslProxy":PROXY,
    
    "proxyType":"MANUAL",
} 
"""


fp = se.webdriver.FirefoxProfile()
options = se.webdriver.FirefoxOptions()
#options.headless = True
options.log.level = "trace"
driver = se.webdriver.Firefox(firefox_profile=fp, options=options)
driver.set_window_size(1220, 2000)
driver.get(url)
time.sleep(10)


#print(driver.page_source)

data = driver.find_elements_by_tag_name('input')


data[0].send_keys("Anbertok25@gmail.com")
data[1].send_keys("665544Ab_")

submit = driver.find_element_by_css_selector(".login-button-31D24.highlight-1TvcX").click()




"""
for a in data:
    if i == 0:
        a.send_keys("big")
    else:
        a.send_keys("dick")    
    i+=1
"""

"""
login = driver.find_element_by_class_name("login-button").click()
time.sleep(5)

newURl = driver.window_handles[0]
driver.switch_to.window(newURl)

driver.find_element_by_class_name("channel-name-2qzLW").click()
"""