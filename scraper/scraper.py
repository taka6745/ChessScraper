from selenium import webdriver
import time

#This is the path to where I've got my chromedriver file - Luke
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://chess.com")
print(driver.title)
time.sleep(5000)

