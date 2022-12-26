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
driver.find_element(By.LINK_TEXT, "Choose").send_keys("\n")
#link.click()

time.sleep(5000)

