from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.sreality.cz/")
driver.maximize_window()

# Below line creates instance of ActionChains class
action = ActionChains(driver)
# Below line locates and stores an element which is outside the shadow-root
element_outside_shadow = driver.find_element(By.XPATH, "//div[@class='szn-cmp-dialog-container']")
# Below 2 lines clicks on the browser at an offset of co-ordinates x=5 and y=5
action.move_to_element_with_offset(element_outside_shadow, 5, 5)
action.click()
