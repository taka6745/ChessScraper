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


def inputArea():
    WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.CLASS_NAME, "ccHelper-input")))
    driver.find_element(By.CLASS_NAME, "ccHelper-input").click()


def sendMove(move: str):
    driver.find_element(By.CLASS_NAME, "ccHelper-input").send_keys(move)
    driver.find_element(By.CLASS_NAME, "ccHelper-input").send_keys(Keys.ENTER)


def getMove(): # returns most recent move
    moves = driver.find_elements(By.CLASS_NAME, "move")    
    white = moves[len(moves)-1].find_element(By.CLASS_NAME, "white").text
    black = moves[len(moves)-1].find_element(By.CLASS_NAME, "black").text
        
    return white, black
    

# clicks engine and sets the level, starts at 1 and goes to 25, (level) has to be between 0,24
def playComputer(level: int):
    driver.get("https://www.chess.com/play/computer")
    time.sleep(1)
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    time.sleep(3)

    for i in range(4):
        webdriver.ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(1)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="board-layout-sidebar"]/div/section/div/div/div[10]/div/div[2]/div/div/img')))
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="board-layout-sidebar"]/div/section/div/div/div[10]/div/div[2]/div/div/img').click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@title='Choose']")))

    driver.find_element(By.XPATH, "//button[@title='Choose']").click()

    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME, "slider-input")))
    driver.implicitly_wait(5)
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, 'slider-input').click()
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME, "slider-input")))
    

    for i in range(24):
        driver.find_element(By.CLASS_NAME, 'slider-input').send_keys(Keys.ARROW_LEFT)
    for i in range(level):
        driver.find_element(By.CLASS_NAME, 'slider-input').send_keys(Keys.ARROW_RIGHT)

    driver.find_element(By.XPATH, "//div[@data-cy='Challenge']").click()
    driver.find_element(By.XPATH, "//button[@title='Play']").click()
    inputArea()


# login() # you don't need to be logged in to play computer but uncomment when doing other things
playComputer(10)
sendMove("a3")
white, black = getMove()
print(black)