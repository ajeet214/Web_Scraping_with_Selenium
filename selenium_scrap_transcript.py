from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("https://www.luyennghetienganh.com/learn-by-listening-level-1/1060-learn-english-by-listening-level-1-unit-001.html")

container = driver.find_elements(By.CSS_SELECTOR, 'div.rabbit-lyrics__line')
eng_sub = [i.get_attribute('innerHTML') for i in container]
print(eng_sub)




