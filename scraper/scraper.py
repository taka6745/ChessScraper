from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from chromeOptions import op
driver = webdriver.Chrome(ChromeDriverManager().install(), options=op)
driver.set_window_size(900, 800)


def login():
    driver.get("https://www.chess.com/login")
    driver.find_element(By.ID, "username").send_keys(
        "39036@immanuel.qld.edu.au")
    search = driver.find_element(By.ID, "password")
    search.send_keys("Bindon02")
    search.send_keys(Keys.RETURN)
    driver.implicitly_wait(5)


def playComputer(level: int): #clicks engine and sets the level, starts at 1 and goes to 25, (level) has to be between 0,24
    driver.get("https://www.chess.com/play/computer")
    driver.implicitly_wait(1)
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    driver.implicitly_wait(5)

    for i in range(3):
        webdriver.ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
        driver.implicitly_wait(2)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="board-layout-sidebar"]/div/section/div/div/div[10]/div/div[2]/div/div/img')))
    driver.find_element(By.XPATH, '//*[@id="board-layout-sidebar"]/div/section/div/div/div[10]/div/div[2]/div/div/img').click()
    
    driver.find_element(By.XPATH, "//button[@title='Choose']").click()
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME, "slider-input")))
    driver.find_element(By.CLASS_NAME, 'slider-input').click()
    driver.find_element(By.CLASS_NAME, 'slider-input').send_keys(Keys.ARROW_LEFT)
    for i in range(level):
        driver.find_element(By.CLASS_NAME, 'slider-input').send_keys(Keys.ARROW_RIGHT)

# login() # you don't need to be logged in to play computer but uncomment when doing other things
playComputer(10)

