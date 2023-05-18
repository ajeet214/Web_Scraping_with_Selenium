import time
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

options = ChromeOptions()

options.add_argument("--start-maximized")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = Chrome(options=options)
# Here I've taken the URL of this same stackoverflow page
driver.get("https://stackoverflow.com/questions/75945977/how-to-get-mouse-hover-message-in-selenium-webdriver-which-is-not-given-in-html")
time.sleep(1)
# and lets for example, take the java tag in your post
element_to_hover_over = driver.find_element(By.XPATH, '//*[@id="question"]/div/div[2]/div[2]/div/div/ul/li[1]')
hover = ActionChains(driver).move_to_element(element_to_hover_over)
hover.perform()
time.sleep(2)
hover_tag_all_detail = element_to_hover_over.find_element(By.CSS_SELECTOR, 'div.esc-remove').text
print(f"all details:\n{hover_tag_all_detail}")
hover_tag_descrition = element_to_hover_over.find_element(By.CSS_SELECTOR, 'div.fc-light').text
print(f"tag description only:\n{hover_tag_descrition}")

