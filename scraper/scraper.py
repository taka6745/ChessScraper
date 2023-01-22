from distutils.log import error
from turtle import reset
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


def getMove():  # returns most recent move
    moves = driver.find_elements(By.CLASS_NAME, "move")
    white = moves[len(moves)-1].find_element(By.XPATH,"//*[contains(@class, 'white')]").text
    black = moves[len(moves)-1].find_element(By.XPATH,"//*[contains(@class, 'black')]").text

    return white, black


# clicks engine and sets the level, starts at 1 and goes to 25, (level) has to be between 0,24
def playComputer(level: int):
    for i in range(3):  # retries 3 times if failed
        try:
            print("Connecting...")
            driver.get("https://www.chess.com/play/computer")
            time.sleep(1)
            webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
            print("Connected")
            break
        except(error):
            print("failed to connect to chess.com")
            print(error.__code__)

    # Scrolling to "Engine"
    for i in range(6):
        webdriver.ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(1)

    for i in range(3):
        try:
            print("Finding Engine...")
            #WebDriverWait(driver, 20, 1).until(EC.presence_of_element_located((By.XPATH, '//*[@id="board-layout-sidebar"]/div/section/div/div/div[10]/div/div[2]/div/div/img')))
            WebDriverWait(driver, 20, 1).until(
                EC.presence_of_element_located((By.XPATH, "//img[@alt='komodo1']")))
            time.sleep(1)
            #driver.find_element(By.XPATH, '//*[@id="board-layout-sidebar"]/div/section/div/div/div[10]/div/div[2]/div/div/img').click()
            driver.find_element(By.XPATH, "//img[@alt='komodo1']").click()

            print("Found")
            break
        except:
            print("Could not find Engine")

    # Click Choose button
    WebDriverWait(driver, 20, 1).until(
        EC.presence_of_element_located((By.XPATH, "//button[@title='Choose']")))
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[@title='Choose']").click()

    # Find Slider
    for i in range(3):
        try:
            print("Finding Slider...")
            WebDriverWait(driver, 20, 1).until(EC.presence_of_element_located(
                (By.XPATH, "//input[@class='slider-input']")))
            time.sleep(1)

            driver.find_element(
                By.XPATH, "//input[@class='slider-input']").click()

        except:
            print("Could not find Slider")
    computer_levels = [0, 250, 400, 500, 700, 850, 1000, 1100, 1200, 1300, 1400, 1500,
                       1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2900, 3200]
    for i in range(3):
        try:
            print("Setting Engine to level", level)
            for i in range(48):
                current_level = int(driver.find_element(
                    By.XPATH, "//span[@class='user-tagline-rating user-tagline-white']").text.strip("()"))
                if current_level > computer_levels[level]:
                    driver.find_element(
                        By.CLASS_NAME, 'slider-input').send_keys(Keys.ARROW_LEFT)
                elif current_level < computer_levels[level]:
                    driver.find_element(
                        By.CLASS_NAME, 'slider-input').send_keys(Keys.ARROW_RIGHT)
                elif current_level == computer_levels[level]:
                    print("Set to level,", level)
                    break

        except:
            print("Failed to move slider")

    # Click "Challenege then Play"
    WebDriverWait(driver, 20, 1).until(EC.presence_of_element_located(
        (By.XPATH, "//div[@data-cy='Challenge']")))
    driver.find_element(By.XPATH, "//div[@data-cy='Challenge']").click()

    WebDriverWait(driver, 20, 1).until(
        EC.presence_of_element_located((By.XPATH, "//button[@title='Play']")))
    driver.find_element(By.XPATH, "//button[@title='Play']").click()
    inputArea()


# login() # you don't need to be logged in to play computer but uncomment when doing other things
playComputer(10)
sendMove("a3")
white, black = getMove()
print(white,black)
