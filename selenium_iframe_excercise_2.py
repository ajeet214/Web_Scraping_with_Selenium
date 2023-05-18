import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

driver = Chrome()

driver.get("https://www.northamericanstainless.com/NAS_App/Surcharge1?language=E&type=F")

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'iframe.surcharge-iframe')))
# -------------------------------------------------------------------------------------------------------------------
driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, 'iframe.surcharge-iframe'))
# -------------------------------------------------------------------------------------------------------------------
# click on submit button
driver.find_element(By.ID, 'submitStylev2').click()
time.sleep(5)
