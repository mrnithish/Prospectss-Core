from selenium import webdriver
from time import sleep


url = r"https://www.facebook.com/groups/5857109064338371/members"
driv = r'C:\Users\HP\Downloads\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(driv)
driver.get(url)

sleep(2)
email = driver.find_element('xpath','//*[@id="email"]').send_keys('sivagurum004@gmail.com')
sleep(4)
pwd = driver.find_element('xpath','//*[@id="pass"]').send_keys('Sivaguru123@')
sleep(5)
login = driver.find_element('xpath','//*[@id="loginbutton"]').click()
sleep(2)



# nam = driver.find_element('xpath','//+[contains(concat( " ", @class, " " ), concat( " ", "x1jx94hy", " " ))]//[contains(concat( " ", @class, " " ), concat( " ", "x1jx94hy", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "xt0b8zv", " " ))]').text
# print(nam)
last_height = driver.execute_script("return document.body.scrollHeight")

t = 0
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height < last_height:
        break
    elif t == 1:
        break
    last_height = new_height
    t +=1
sleep(20)

for i in range(1,50):
    try:
        # name = driver.find_element('xpath','//*+[contains(concat( " ", @class, " " ), concat( " ", "x1jx94hy", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "x1jx94hy", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "x1rdy4ex", " " ))]//div[(((count(preceding-sibling::*) + 1) = 1) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "x1lliihq", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "x1yc453h", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "xzsf02u", " " ))]').text
        # print(name)
        
        nam = driver.find_element('xpath',f'//*+[contains(concat( " ", @class, " " ), concat( " ", "x1jx94hy", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "x1jx94hy", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "x1rdy4ex", " " ))]//div[(((count(preceding-sibling::*) + 1) = {i}) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "x1ja2u2z", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "x1ja2u2z", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "xzsf02u", " " )) and contains(concat( " ", @class, " " ), concat( " ", "x1s688f", " " ))]').text
        print(nam)
        # jn = driver.find_element('xpath',f'//*[@id="mount_0_0_x+"]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div/div[3]/div/div/div[4]/div/div/div/div/div/div/div/div/div/div/div[2]/div[6]/div/div[2]/div/div[{i}]/div/div/div[2]/div[1]/div/div/div[2]/span/span').text
        # print(jn)
        # try:
        #     dis = driver.find_element('xpath',f'//*[@id="mount_0_0_x+"]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div/div[3]/div/div/div[4]/div/div/div/div/div/div/div/div/div/div/div[2]/div[6]/div/div[2]/div/div[{i}]/div/div/div[2]/div[1]/div/div/div[3]/span/text()')
        #     print(dis)
        # except:
        #     print('no dis')
        # url = driver.find_element('xpath',f'//*[@id="mount_0_0_x+"]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div/div[3]/div/div/div[4]/div/div/div/div/div/div/div/div/div/div/div[2]/div[6]/div/div[2]/div/div[{i}]/div/div/div[2]/div[1]/div/div/div[1]/span/span/span/a')
        # print(url)
    except Exception as e:
        print(e)
        