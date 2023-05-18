import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


options = ChromeOptions()

# maximized and disable forbar
options.add_argument("--start-maximized")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options=options)


url = "https://twitter.com/login"

driver.get(url)
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "css-1dbjc4n")))
login = driver.find_element(By.CLASS_NAME, "css-1dbjc4n")
time.sleep(2)
username = login.find_element(By.CSS_SELECTOR, 'input[autocomplete="username"]')
username.send_keys("xxxxxxxxxxx")
username.send_keys(Keys.ENTER)
time.sleep(1)
password = login.find_element(By.CSS_SELECTOR, 'input[name="password"]')
password.send_keys("xxxxxxxx")
password.send_keys(Keys.ENTER)

time.sleep(2)
