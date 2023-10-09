import requests,openpyxl
from bs4 import BeautifulSoup

url="https://www.google.com/maps/search/nearby+coffee+shop/@11.0807964,76.9907652,14z/data=!3m1!4b1"

try:
    source=requests.get(url)
    source.raise_for_status()
    soup=BeautifulSoup(source.text,'html.parser')
    print(soup)
except Exception as e:
    print(e)