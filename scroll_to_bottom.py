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

"""
steps followed:

1. First, we wait for the scroll-bar web element to get visibly located/loaded on the page and assign it to a variable 
scroll_bar
2. Next, we get the current height of this scroll_bar and assign it to a variable last_height.
3. start looping and in each iteration, scroll down to the bottom of the scroll bar, take a pause, get the height of 
the scroll bar, and assign it to a variable new_height and check if the new_height == last_height, break out of the 
loop(flag=Flase) otherwise, update the variable last_height with new_height and repeat this step until the if condition
 is True.
 
reference:
https://stackoverflow.com/questions/76503251/how-to-scroll-down-to-the-bottom-of-an-inner-scroll-bar-using-selenium-with-pyth
"""
