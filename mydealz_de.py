"""
Project : 
Author : Ajeet
Date : June 12, 2023
"""

import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC


driver = Chrome()
driver.get("https://www.mydealz.de/register")
wait = WebDriverWait(driver, 10)

# accept all cookies
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[data-t="acceptAllBtn"]'))).click()

checkboxes = driver.find_elements(By.CSS_SELECTOR, 'span.tGrid-cell.tGrid-cell--shrink')
# select the 2nd checkbox
checkboxes[1].click()
# Similarly, you can also select the 1st checkbox using checkboxes[0].click()

time.sleep(2)

"""
reference:
https://stackoverflow.com/questions/76453368/how-to-click-a-checkbox-by-driver-find-elementid-in-python
"""
