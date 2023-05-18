import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options=options)

driver.get('https://www.ifsc-climbing.org/index.php/world-competition/calendar?task=ranking-complete&category=3')
time.sleep(2)
# -------------------------------------------------------------------------------------------------------------------
driver.switch_to.frame("calendar")
# -------------------------------------------------------------------------------------------------------------------
table_wrapper = driver.find_element(By.CSS_SELECTOR, 'div[id="table_id_wrapper"]')
results = table_wrapper.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')

data = []
for result in results:
    details = result.find_elements(By.TAG_NAME, 'td')
    temp_dict = {
        "name": f"{details[1].text} {details[2].text}",
        "country": details[3].text,
        "points": details[4].text
    }
    data.append(temp_dict)

print(data)

