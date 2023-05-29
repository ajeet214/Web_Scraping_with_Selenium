import time
import selenium.common.exceptions
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from bs4 import BeautifulSoup

driver = Chrome()

driver.get('https://www.knx.org/knx-en/for-professionals/community/partners/?country=120')
driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary.cb-enable').click()

try:
    while True:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a#knx-load-button.load_more'))).click()
        time.sleep(1)
except selenium.common.exceptions.TimeoutException:
    pass

soup = BeautifulSoup(driver.page_source, 'lxml')
driver.quit()
table = soup.select_one('table#partner-list')
rows = table.select('tr')
print(f"total rows: {len(rows)}")

for row in rows[1:]:
    print(list(filter(None, row.text.split('\n'))))
    # you can further parse this data as you want


