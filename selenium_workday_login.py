import time
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

options = ChromeOptions()
options.add_argument('--start-maximized')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36")


driver = Chrome(options=options)
wait = WebDriverWait(driver, 10)

url = "https://walmart.wd5.myworkdayjobs.com/en-US/WalmartExternal/login"
driver.get(url)

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-automation-id="email"]')))
email = driver.find_element(By.CSS_SELECTOR, 'input[data-automation-id="email"]')
email.send_keys('your_username')

password = driver.find_element(By.CSS_SELECTOR, 'input[data-automation-id="password"]')
password.send_keys('your_password')

submit = driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Sign In"]')

hover = ActionChains(driver).move_to_element(submit)
hover.click().perform()

time.sleep(10)

"""
Few things to note:

1. we need to wait for the Sign In box to appear on the page.
2. we must pass the user-agent to the Chrome options.
3. Use ActionChains to successfully perform the click to get to the logged-in profile. A simple click() will not work here.
"""