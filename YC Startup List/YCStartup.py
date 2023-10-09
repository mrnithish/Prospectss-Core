import bs4
from selenium import webdriver 
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import pandas as pd 
from time import sleep
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from emailfinder.extractor import *
import csv,openpyxl
import pandas as pd

#Excel creation
excel=openpyxl.Workbook()
sheet=excel.active
sheet.title='Email List'
sheet.append(['Comapny Name','Company Location','Company Description','Company Links'])


searchQuery=input("Enter the search: ")
driver = webdriver.Chrome()
ycStartup='https://www.ycombinator.com'
url="https://www.ycombinator.com/companies?query="+searchQuery
driver.get(url)
sleep(2)


last_height = driver.execute_script("return document.body.scrollHeight")
# while True:
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     sleep(1)
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height < last_height:
#         break
#     last_height = new_height

sleep(50)
src = driver.page_source
companyName=[]
companyLocation=[]
companyDescription=[]
companyTags=[]
companyLink=[]
soup = bs4.BeautifulSoup(src, 'lxml')
link=soup.find_all('a', class_="WxyYeI15LZ5U_DOM0z8F no-hovercard")
for name in soup.findAll('span',{'class':'CBY8yVfV0he1Zbv9Zwjx'}):
    companyName.append(name.text)
for name in soup.findAll('span',{'class':'eKDwirBf1zBn7I5MGAOb'}):
    companyLocation.append(name.text)
for name in soup.findAll('span',{'class':'OCTUb4j7DGmBqnUsAzVD'}):
    companyDescription.append(name.text)
for name in soup.findAll('span',{'class':'pill cK7bzFxvFB9Nwf9WWTA0'}):
    companyTags.append(name.text)
for i in soup.find_all('a', {"class":"WxyYeI15LZ5U_DOM0z8F"}):
    productLinks = ycStartup + i['href']
    companyLink.append(productLinks)

print(len(companyLink))
print(len(companyName))
print(len(companyDescription))
print(len(companyLocation))
Size_of_List=len(companyName)
try:
    for i in range(0,Size_of_List):
        sheet.append([companyName[i],companyLocation[i],companyDescription[i],companyLink[i]]) #Appending the data to the excelsheet
    excel.save('YCOMBINATOR.xlsx')
    print("Successfull")
except Exception as e:
    print("error")


#close
sleep(4)
driver.quit()