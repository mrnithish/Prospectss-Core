from selenium import webdriver 
import pandas as pd 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
url="https://www.youtube.com/@madangowri" ## channel link
yabout="/about"
driver.get(url+yabout)

joinDate = driver.find_elements(By.XPATH,'//*[@id="right-column"]/yt-formatted-string[2]/span[2]')
noViews=driver.find_elements(By.XPATH,'//*[@id="right-column"]/yt-formatted-string[3]')
noSubscribers=driver.find_elements(By.XPATH,'//*[@id="subscriber-count"]')
ytIdHandle=driver.find_elements(By.XPATH,'//*[@id="channel-handle"]')
ytName=driver.find_elements(By.XPATH,'//*[@id="text"]')
description=driver.find_elements(By.XPATH,'//*[@id="description"]')
noOfVideosYt=driver.find_elements(By.XPATH,'//*[@id="videos-count"]/span[1]')
ytChannelLocation=driver.find_elements(By.XPATH,'//*[@id="details-container"]/table/tbody/tr[2]/td[2]/yt-formatted-string')
for i in range(1,8):
    linkxpath="//*[@id='link-list-container']/a["+str(i)+"]"
    elems=driver.find_elements(By.XPATH,linkxpath)
    links = [elem.get_attribute('href') for elem in elems]
    print(links)

for value in joinDate:
        print(value.text)
for value in noViews:
        print(value.text)
for value in noOfVideosYt:
        print(value.text)
for value in description:
        print(value.text)
for value in noSubscribers:
        print(value.text)
for value in ytIdHandle:
        print(value.text)
for value in ytName:
        print(value.text)
for value in ytChannelLocation:
        print(value.text)

# if noSubscribers>1000 and noViews>4000:
#         print("Monetization")
# else:
#         print("No Monetization")











#video link
# user_data = driver.find_elements(By.XPATH,'//*[@id="video-title"]')
# links = []
# for i in user_data:
#             links.append(i.get_attribute('href'))

# print(len(links))