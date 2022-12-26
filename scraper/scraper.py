from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#This is the path to where I've got my chromedriver file - Luke
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.chess.com/login")

driver.find_element(By.ID, "username").send_keys("39036@immanuel.qld.edu.au")
search = driver.find_element(By.ID, "password")
search.send_keys("Bindon02")
search.send_keys(Keys.RETURN)
driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT, "vs Computer").click()
driver.implicitly_wait(2)
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
driver.implicitly_wait(2)

#The two following loops use the tab symbol to navigate to the correct
#hyperlink to press. This is obviously bad code and should be changed to
#find the correct link directly, but for some reason using By.LINK_TEXT
#wasn't working for me.
for i in range(15):
    webdriver.ActionChains(driver).send_keys(Keys.TAB).perform()
driver.implicitly_wait(2)

webdriver.ActionChains(driver).send_keys(Keys.RETURN).perform()

driver.implicitly_wait(2)

for i in range(18):
    webdriver.ActionChains(driver).send_keys(Keys.TAB).perform()

webdriver.ActionChains(driver).send_keys(Keys.RETURN).perform()
#driver.find_element(By.LINK_TEXT, "Choose").send_keys("\n")
#link.click()

time.sleep(5000)

