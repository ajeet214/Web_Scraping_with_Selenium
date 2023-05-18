from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.google.com/travel/flights')

wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[aria-placeholder='Where from?'] input"))).click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[aria-label='Enter your origin'] input"))).send_keys("Sydney" + Keys.ARROW_DOWN + Keys.ENTER)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[aria-placeholder='Where to?'] input"))).click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[aria-label='Enter your destination'] input"))).send_keys("Auckland" + Keys.ARROW_DOWN + Keys.ENTER)
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Search']"))).click()

driver.quit()
