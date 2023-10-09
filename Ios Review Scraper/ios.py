from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep



driver = webdriver.Chrome()
driver.get("https://www.apple.com/app-store/")
sleep(3)
search = driver.find_element(By.CSS_SELECTOR, '#globalnav-menubutton-link-search').click()
sleep(2)
search_box = driver.find_element(By.XPATH, '//*[@id="globalnav-submenu-search"]/div/div/form/div[1]/input[1]')
search_box.send_keys("stack ball") ##search Query
sleep(2)
search_box.send_keys(Keys.RETURN)
sleep(2)
driver.find_element(By.XPATH, '//*[@id="exploreCurated"]/div[1]/div[2]/h2/a').click()
sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="ember13"]')
# Scroll to the element
actions = ActionChains(driver)
actions.move_to_element(element).perform()
sleep(3)
element.click()
seeall=driver.find_element(By.XPATH, '/html/body/div[3]/main/div[2]/section[5]/div[1]/a').get_attribute('href') 
driver.get(seeall)
sleep(2)
#scale this
more=driver.find_element(By.XPATH,'/html/body/div[3]/main/div[2]/section/div[2]/div[1]/div[2]/blockquote/button').click()
sleep(4)
reviews=driver.find_elements(By.XPATH,'/html/body/div[2]/div/div/div/div')
date=driver.find_elements(By.XPATH,'/html/body/div[2]/div/div/div/div/div/time')
person=driver.find_elements(By.XPATH,'/html/body/div[2]/div/div/div/div/div/span[1]')
for value in person:
        print(value.text)
for value in date:
        print(value.text)
for value in reviews:
        print(value.text)
sleep(2)
close = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/button').click()
sleep(3)


driver.quit()