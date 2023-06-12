"""
Project : 
Author : Ajeet
Date : June 12, 2023
"""

import time
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://bdap-opendata.rgs.mef.gov.it/opendata/spd_mop_prg_mon_reg18_01_9999?t=Scarica"

chrome_options = ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
driver = Chrome(options=chrome_options)
driver.get(url)
wait = WebDriverWait(driver, 20)
# ----------------------------------------------------------------------------------------------------------------------
# wait for the target iframe to get loaded in order to switch to it
iframe = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'iframe.tabIframe.dinamically-tab-iframe-content')))
# switch to the target iframe
driver.switch_to.frame(iframe)
# ----------------------------------------------------------------------------------------------------------------------

wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@title="Excel file format."]'))).click()

try:
    driver.switch_to.alert.accept()
except NoAlertPresentException:
    pass

time.sleep(5)

"""
Steps to follow:
1. First wait for the desired iframe tag to be get loaded/located on the page.
2. after making sure that it's loaded, switch to this iframe as mentioned in the code above (using switch_to.frame())
3. Once you're inside the iframe, you can easily locate the desired element using XPATH but make sure it is clickable before clicking as the website takes some time to load this particular section on the page.
4. Sometimes, when you click the desired button/element, an alert box appears as shown below, you can simply accept it:

reference:
https://stackoverflow.com/questions/76454460/webcrawling-with-selenium-couldnt-extract-the-xpath-of-a-button
"""