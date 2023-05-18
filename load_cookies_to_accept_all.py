import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.common.by import By

options = ChromeOptions()

# to start maximized screen
options.add_argument("--start-maximized")
# to remove 'Chrome is being controlled by automated software'
options.add_experimental_option("excludeSwitches", ["enable-automation"])

options.add_experimental_option("useAutomationExtension", False)

driver = Chrome(options=options)

driver.get("https://langsungkerja.id/registration/")

driver.add_cookie({"name": "cookieyes-consent", "value": "consent:yes,action:yes"})
driver.refresh()

driver.find_element(By.CSS_SELECTOR, 'button.tutor-btn.tutor-btn-primary').click()
time.sleep(1)

