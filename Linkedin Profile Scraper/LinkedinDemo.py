from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import bs4
from time import sleep

# Set up Selenium web driver
driver = webdriver.Chrome()

# Log in to LinkedIn account
driver.get('https://www.linkedin.com/login')
username = driver.find_element(value="username")
password = driver.find_element(value="password")
username.send_keys('bennyrocky100@gmail.com')
sleep(3)
password.send_keys('Rocky1000@')
sleep(2)
password.send_keys(Keys.RETURN)
sleep(4)

# Navigate to Connections page
profileLink="https://www.linkedin.com/in/shumbul/" ## profile Link
driver.get(profileLink)
# Scroll to bottom of page to load all connections
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
data=[]
src = driver.page_source
soup = bs4.BeautifulSoup(src, 'lxml')
head_container = soup.find('div', {'class': 'ph5 pb5'})
# pronoun=soup.find('span',{'class':'text-body-small v-align-middle break-words t-black--light'}).text
# print(pronoun)
for names in soup.find('h1',{'class':'text-heading-xlarge inline t-24 v-align-middle break-words'}):
    profilename=names.text.replace("\n", '')
    print(profilename)
for pronouns in soup.find('span',{'class':'text-body-small v-align-middle break-words t-black--light'}):
    pronoun=pronouns.text.replace('\n','')
    print(pronoun)
for title in soup.find('div',{'class':"text-body-medium break-words"}):
    jobTitle=title.text.replace('\n','')
    print(jobTitle)
for locations in soup.find('span',{'class':'text-body-small inline t-black--light break-words'}):
    location=locations.text.replace('\n','')
    print(location)
for about in soup.find('div',{'class':'pv-shared-text-with-see-more full-width t-14 t-normal t-black display-flex align-items-center'}):
    abouts=about.text.replace('\n','')
    print(abouts)
for talk in soup.find('div',{'class':'text-body-small t-black--light break-words mt2'}):
    talks=talk.text
    print(talks)
for follow in soup.find('ul',{'class':'pv-top-card--list pv-top-card--list-bullet'}):
    follows=follow.text.replace('\n','')
    print(follows)


    
    


driver.quit()
