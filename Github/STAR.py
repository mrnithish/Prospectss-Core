import  requests
from bs4 import BeautifulSoup

url = 'https://github.com/search?q=scraping&type=repositories'
response = requests.get(url)
msg = response.text
soup=BeautifulSoup(msg,'html.parser')
for name in soup.findAll('a',{'class':'Link--muted'}):
    print(name.text)









# import bs4,requests,lxml
# from bs4 import BeautifulSoup
# from time import sleep



# url="https://github.com/search?q=scraping&type=repositories"

# src = requests.get(url)
# soup = bs4.BeautifulSoup(src, "html.parser")
# for name in soup.findAll('a',{'class':'Link--muted'}):
#     print(name.text)