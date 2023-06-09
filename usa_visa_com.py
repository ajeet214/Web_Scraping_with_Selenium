"""
Project : 
Author : Ajeet
Date : June 9, 2023
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Chrome()
driver.get('https://usa.visa.com/support/consumer/travel-support/exchange-rate-calculator.html')
wait = WebDriverWait(driver, 30)

# click to Accept
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Accept']"))).click()

shadow_root = driver.find_element(By.XPATH, "//dm-calculator").shadow_root
# enter_amount
shadow_root.find_element(By.ID, "input_amount_paid").send_keys("1")

# from_dropdown
shadow_root.find_element(By.ID, "autosuggestinput_from").click()
shadow_root.find_element(By.ID, "listbox-item-157").click()

# to_dropdown
shadow_root.find_element(By.ID, "autosuggestinput_to").click()
shadow_root.find_element(By.ID, "listbox-item-0").click()

# fee_edit
shadow_root.find_element(By.CLASS_NAME, 'vs-link-cta.vs-calculator-edit-link').click()

bank_rate = to_dropdown = shadow_root.find_element(By.ID, "input_bank_rate")
bank_rate.send_keys(Keys.CONTROL, 'a')
bank_rate.send_keys(Keys.BACKSPACE)
bank_rate.send_keys('0')

# clicks on Calculate Conversion button
shadow_root.find_elements(By.CSS_SELECTOR, 'div.vs-container')[-1].find_elements(By.TAG_NAME, 'button')[0].click()
sleep(2)


