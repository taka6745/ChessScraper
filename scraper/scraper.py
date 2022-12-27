from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from chromeOptions import op
driver = webdriver.Chrome(ChromeDriverManager().install(),options=op)
def login():
    driver.get("https://www.chess.com/login")
    driver.find_element(By.ID, "username").send_keys("39036@immanuel.qld.edu.au")
    search = driver.find_element(By.ID, "password")
    search.send_keys("Bindon02")
    search.send_keys(Keys.RETURN)
    driver.implicitly_wait(5)
def playComputer():
    driver.get("https://www.chess.com/play/computer")
    driver.implicitly_wait(1)
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    driver.implicitly_wait(5)
    
    driver.find_element(By.XPATH, '//*[@id="board-layout-sidebar"]/div/section/div/div/div[3]/div/div[2]/div[6]/div/img').click()
    driver.find_element(By.XPATH, "//button[@title='Choose']").click()

login()
playComputer()
time.sleep(5000)
