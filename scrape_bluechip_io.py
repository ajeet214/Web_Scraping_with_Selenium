from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = Chrome()

url = "https://bluechip.io/sport?bt-path=%2Fschedule%3FscheduleSport%3Dsoccer-1"
driver.get(url)

inner_page = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#bt-inner-page"))).shadow_root
eventCard = WebDriverWait(inner_page, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[data-editor-id="eventCard"]')))
print(len(eventCard))
# 20
"""
Few things to note:

1. First, we should wait for the presence of the content bt-inner-page to get located so that we can further look for the shadow_root in it.
2. Once we are inside the shadow_root, we need to again wait for the web element of the event cards to get loaded on the page.

As you can see above, we get all of the 20 event cards which can be further parsed accordingly as per the need.

I hope this solves your problem, cheers!
"""
