from selenium import webdriver
from selenium.webdriver import ChromeOptions, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import json
import time

options = ChromeOptions()

# maximized and disable forbar
options.add_argument("--start-maximized")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options=options)

url = "https://booking.bbdc.sg/#/login?redirect=%2Ftransactions%2Findex"


driver.get(url)

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="login-content d-flex justify-center flex-column"]')))
username= driver.find_element(by=By.ID, value='input-8')
username.send_keys("ajeet@123")
password = driver.find_element(by=By.ID, value='input-15')
password.send_keys("ajee")

# locate the button to click by using its partial class name
driver.find_element(By.CSS_SELECTOR, 'button[class^="v-btn v-btn"]').click()
time.sleep(5)


driver.quit()