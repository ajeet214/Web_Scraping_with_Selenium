from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.set_window_size(500, 500)
driver.get('https://clickclickclick.click/')

actions = ActionChains(driver)

x_coord, y_coord = 250, 182 #coordinates of the button
t = actions.move_by_offset(x_coord, y_coord).click().perform()
time.sleep(5)