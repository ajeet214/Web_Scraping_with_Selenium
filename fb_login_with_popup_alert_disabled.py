import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options = ChromeOptions()

# maximized and disable forbar
options.add_argument("--start-maximized")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option(
    "prefs",
    {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2
        # with 2 should disable/block notifications and 1 to allow
    },
)

driver = webdriver.Chrome(options=options)

url = "https://www.facebook.com/"
driver.get(url)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "globalContainer")))
container = driver.find_element(By.ID, "globalContainer")

# # fill the email account, password
email = container.find_element(By.ID, 'email')
password = container.find_element(By.ID, 'pass')
email.send_keys("xxxxxxxxx")
password.send_keys("xxxxxxxxxxxx")
password.send_keys(Keys.ENTER)
time.sleep(10)
