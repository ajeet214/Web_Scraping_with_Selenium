
import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


options = ChromeOptions()

# maximized and disable forbar
options.add_argument("--start-maximized")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options=options)

url = "https://www.kbb.com/"
driver.get(url)

# ---------------------------------------------------------------------------------------------
element_to_hover_over = driver.find_element(By.XPATH, '//*[@id="app"]/header/div/nav/div[2]')
hover = ActionChains(driver).move_to_element(element_to_hover_over)
hover.perform()
# ---------------------------------------------------------------------------------------------

driver.find_element(By.XPATH, '//*[@id="app"]/header/div/nav/div[2]/ul/li[1]').click()
time.sleep(2)
