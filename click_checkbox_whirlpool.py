import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

driver = Chrome()
driver.get('https://register.whirlpool.com/en-us/registration')

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'privacy_policy')))
# ------------------------------------------------------------------------------------------------------------
driver.execute_script("document.getElementById('privacy_policy').click();")
# ------------------------------------------------------------------------------------------------------------
time.sleep(2)
var1 = driver.find_element(By.ID, "privacy_policy").is_selected()
print(var1)


"""
output:
True

You can also cross-check by simply running the javascript query document.getElementById('privacy_policy').click() on the Console of the page and you'll see that it indeed performs the click on the desired checkbox.

reference:
https://stackoverflow.com/questions/76404208/not-able-to-click-on-checkbox-using-selenium-in-python-error-selenium-common-ex
"""