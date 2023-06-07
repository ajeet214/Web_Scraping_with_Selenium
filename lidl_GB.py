"""
Project : Lidl GB
Author : Ajeet
Date : 07/06/2023
"""
import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options = ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)
url = "https://www.lidl.co.uk/about-us/store-finder-opening-hours#"
driver.get(url)

# wait for element to get located to click the "ACCEPT" cookies button
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.cookie-alert-extended-button"))).click()
# wait for element to get located to click the "STORE SEARCH" button
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.nuc-m-button.nuc-a-button"))).click()
# wait for element to get located to Enter post code or city
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter post code or city"]'))).send_keys('London')

time.sleep(10)
