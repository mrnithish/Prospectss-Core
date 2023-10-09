from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import pandas as pd

input=input("What are you looking for...? (Do not type near me!): ")
url="https://www.google.com/maps/search/"+input+"+near+me/@11.0628748,77.0024176,15z"
browser=webdriver.Chrome()
browser.get(url)
soup=BeautifulSoup(browser.page_source,"html.parser")
container=soup.find_all("div",class_="Nv2PK THOPZb CpccDe")

Store_details={"Title":[],"Address":[],"Contact":[],"Rating":[],"Review":[],"Link":[]}

Num=[]
phone=[]
for store in container:
    title=store.find("a",class_="hfpxzc").get("aria-label")
    link=store.find("a",class_="hfpxzc").get("href")
    r=requests.get(link)
    soup=BeautifulSoup(r.content,"html.parser")
    address=soup.find("meta",attrs={"itemprop":"name"}).get("content")
    Store_details["Title"].append(title)
    Store_details["Address"].append(address)
    Store_details["Link"].append(link)
    try:
        rating=store.find("span",class_="MW4etd").text
        review=store.find("span",class_="UY7F9").text.replace("(","").replace(")","")
        Store_details["Rating"].append(rating)
        Store_details["Review"].append(review)
    except:
        Store_details["Rating"].append(" ")
        Store_details["Review"].append(" ")
    con_details=store.find_all("div",class_="W4Efsd")

    for i in con_details[3]:
        num=i.find_all("span")
        for j in num:
            Num.append(j.text)
    phone.append(Num[-1].replace(" ",""))
for num in phone:
    try:
        contact=int(num)
        Store_details["Contact"].append(contact)
    except:
        Store_details["Contact"].append(" ")

print(Store_details)

Dataframe=pd.DataFrame.from_dict(Store_details)
print(Dataframe)