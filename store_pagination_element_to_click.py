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

url = "https://www.google.com/search?q=toi"


driver.get(url)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

pages = driver.find_element(by=By.CLASS_NAME, value="AaVjTc").find_element(by=By.TAG_NAME, value='tr').find_elements(by=By.TAG_NAME, value='td')

lst = [page.find_element(by=By.TAG_NAME, value='a') for page in pages[2:]]

print(lst)
print(len(lst))
lst[2].click()
time.sleep(5)

driver.quit()