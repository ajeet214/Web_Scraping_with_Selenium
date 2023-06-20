from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = Chrome()

url = "https://bluechip.io/sport?bt-path=%2Fschedule%3FscheduleSport%3Dsoccer-1"
driver.get(url)

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#bt-inner-page")))
# --------------------------------------------------------------------------------------------------------------------
# inner_page = driver.execute_script('''return document.getElementById('bt-inner-page').shadowRoot''')
# or
inner_page = driver.find_element(By.CSS_SELECTOR, "div#bt-inner-page").shadow_root
# --------------------------------------------------------------------------------------------------------------------
eventCard = WebDriverWait(inner_page, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[data-editor-id="eventCard"]')))
print(len(eventCard))
