import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
options = ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=options)
driver.get("https://deliorder-web.shoprite.com/stores/279/departments/553/products/258234")
time.sleep(5)
driver.execute_script("window.scrollBy(0, 300);")


# --------------------------------------------------------------------------------------------------------------------
driver.find_element(By.XPATH, '//span[contains(text(), "Standard Thickness")]').click()
# --------------------------------------------------------------------------------------------------------------------


time.sleep(2)
slicing_preference = ["Shaved", "Sliced Thin", "Standard Thickness", "Sliced Thick"]
# choose Sliced Thin (slicing_preference[1] is "Sliced Thin")
driver.find_element(By.XPATH, f'//span[contains(text(), "{slicing_preference[1]}")]').click()
time.sleep(2)

