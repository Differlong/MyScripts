"""
import glob
import os
import time
picPathes = (path for path in glob.glob(r"F:/美图录/*/*.jpg"))
for pic in picPathes:
    os.popen(pic)
    time.sleep(3)

#体验不好的第一点是背景音乐太正了，应该去找AV里面的背景音乐；第二点是看到不想看的人可以跳过，这样就很好。这样怎么做呢？




"""

import time
import glob
import random

import os
from selenium import webdriver
chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

picPath = glob.glob(r"F:/美图录精华版/*")
while True:
    picFold = random.choice(picPath)
    isFirst = True
    for pic in glob.glob(picFold+"/*.jpg"):
        driver.get(pic)
        if isFirst:
            if(input("Do you want to continue"+pic)==""):
                break
            else:
                isFirst = False
        time.sleep(3)
        
driver.close()
driver.quit()
#这样看会产生


"""


import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("selenium")
elem.send_keys(Keys.RETURN)
assert "Google" in driver.title
driver.close()
driver.quit()

"""


"""

import glob
import os
from selenium import webdriver
chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

picPath = glob.glob(r"F:/美图录/*")
for picFold in picPath:
    isFirst = True
    for pic in glob.glob(picFold+"/*.jpg"):
        driver.get(pic)
        if isFirst:
            if(input("Do you want to like it? input '' mean ignore it!" +picFold)==""):
                break
            else:
                basename = os.path.basename(picFold)
                source = "F:\美图录\\"+basename
                destination = "F:\美图录精华版\\"+basename
                os.popen("echo D | xcopy %s %s"%(source,destination))
                break
        #time.sleep(3)
        
driver.close()
driver.quit()

"""
























