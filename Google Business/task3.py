import pandas as pd
import numpy as np
import requests,openpyxl
from bs4 import BeautifulSoup

url="https://www.infohindihub.in/2021/03/free-bulk-email-id-list-1000-active.html"
try:
    source=requests.get(url)
    source.raise_for_status()
    soup = BeautifulSoup(source.content, 'html.parser')
    print(soup)
    email=soup.find('div',class_="post-body entry-content float-container").find_all('p')
    print(email)
    for i in email:
        ma=i.find('span').get_text(strip=True)
        print(ma)
except Exception as e:
    print(e)
