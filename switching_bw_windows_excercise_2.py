"""
Project : 
Author : Dart Korea
Date : July 10, 2023
"""

from selenium.webdriver import Chrome, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import time

driver = Chrome()


url = "https://dart.fss.or.kr/dsab007/main.do"
driver.get(url)

state = driver.find_element(By.ID, 'option')
nsw = Select(state)
nsw.select_by_visible_text('회사명')

search = driver.find_element(By.ID, 'textCrpNm')
search.send_keys('조이푸드')
search.send_keys(Keys.ENTER)


# Store the current window handle
win_handle_before = driver.current_window_handle

# Perform the click operation that opens new window
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[title="감사보고서 공시뷰어 새창"]'))).click()
time.sleep(5)

# Switch to new window opened
driver.switch_to.window(driver.window_handles[1])

# Perform the actions on new window
con = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul[class="jstree-children"]')))
con.find_elements(By.TAG_NAME, 'li')[-1].find_element(By.TAG_NAME, 'a').click()

# do the page parsing
driver.switch_to.frame(driver.find_element(By.ID, 'ifrm'))
overview = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//p[text()="1. 회사의 개요"]')))
print(overview.text)

# Close the new window, if that window no more required
driver.close()

# Switch back to original browser (first window)
driver.switch_to.window(win_handle_before)
