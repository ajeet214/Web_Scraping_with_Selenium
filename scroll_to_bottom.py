"""
Project : 
Author : Ajeet
Date : June 19, 2023
"""

import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

driver = Chrome()
wait = WebDriverWait(driver, 10)
driver.get('https://kart.1881.no/?query=1010')

scroll_bar = wait.until(EC.visibility_of_element_located((By.ID, 'search_result')))

flag = True
last_height = driver.execute_script("return arguments[0].scrollHeight", scroll_bar)
SCROLL_PAUSE_TIME = 0.5

while flag:
    # ---------------------------------------------------------------------------------------------------------------
    driver.execute_script("arguments[0].scrollBy(0, arguments[0].scrollHeight);", scroll_bar)
    time.sleep(SCROLL_PAUSE_TIME)
    # ---------------------------------------------------------------------------------------------------------------
    new_height = driver.execute_script("return arguments[0].scrollHeight", scroll_bar)

    if new_height == last_height:
        flag = False
    else:
        last_height = new_height

