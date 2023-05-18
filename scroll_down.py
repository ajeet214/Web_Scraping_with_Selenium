from selenium import webdriver
from selenium.webdriver import ChromeOptions, Keys
from selenium.webdriver.common.by import By
import json
import time
options = ChromeOptions()
# maximized and disable forbar
options.add_argument("--start-maximized")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=options)
old_ulr= "https://stackoverflow.com/"
driver.get(old_ulr)
# open cookie file
with open("cookies.json", "r") as f:
    cookies = json.load(f)
    #load cookies to driver
for cookie in cookies:
    driver.add_cookie(cookie)
time.sleep(3)
driver.refresh()
# open new tab
new_url = "https://stackoverflow.com/users/11179336/ajeet-verma"
driver.execute_script("window.open('');")
# Switch to the new tab and open new URL
driver.switch_to.window(driver.window_handles[1])
driver.get(new_url)
time.sleep(5)
driver.find_element(By.XPATH, "//a[normalize-space()='Answers']").click()
time.sleep(3)

# -----------------------------------------------------------------------------------------------------------------
# scroll down to bottom
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# driver.execute_script("arguments[0].scrollTop = 200", element)
# -----------------------------------------------------------------------------------------------------------------

time.sleep(3)
# find element and click it
driver.find_element(By.XPATH, "//a[contains(text(),'What are the advantages of NumPy over regular Pyth')]").click()
time.sleep(5)
