import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

options = ChromeOptions()

# to start maximized screen
options.add_argument("--start-maximized")
# to remove 'Chrome is being controlled by automated software'
options.add_experimental_option("excludeSwitches", ["enable-automation"])

options.add_experimental_option("useAutomationExtension", False)


driver = webdriver.Chrome(options=options)

url = "https://shopee.vn/search?keyword=iphone&page=0&sortBy=sales"

driver.get(url)

print(type(driver))
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "")))
driver.quit()
