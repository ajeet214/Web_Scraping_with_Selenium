"""
Project : Google Chrome Version
Author : Ajeet
Date : July 12, 2023
"""

import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
driver = webdriver.Chrome(options=options)

driver.get('chrome://settings/help')

time.sleep(2)
update_check = driver.execute_script("return document.querySelector('settings-ui').shadowRoot.querySelector('settings-main').shadowRoot.querySelector('settings-about-page').shadowRoot.querySelectorAll('settings-section')[0].querySelector('div.secondary').getInnerHTML();")
print(update_check)

"""
Since the page is highly embedded with many shadow-root elements that make it impossible to locate the elements 
that are embedded inside the shadow-root using the usual locator strategies such as XAPTH, CSS Selector, ID, etc.

references:
https://stackoverflow.com/questions/76667428/cant-access-the-latest-version-xpath-of-google-chrome-through-selenium-and-chro
"""