"""
Project : DKB Bank Login
Author : Ajeet
Date : July 24, 2023
"""

# Import required modules
import time
from selenium.webdriver import Chrome,Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def main():
    # Initialize Chrome WebDriver
    driver = Chrome()

    # Open the DKB login page
    driver.get("https://banking.dkb.de/login")

    # Set up WebDriverWait with a timeout of 10 seconds
    wait = WebDriverWait(driver, 10)

    # Switch to the iframe and refuse all cookies
    # The website may display a cookie consent popup within an iframe.
    iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe#privacy-iframe')))
    driver.switch_to.frame(iframe)
    driver.find_element(By.CSS_SELECTOR, 'button.btn.refuse-all').click()

    # After refusing cookies, go back to the main page (DKB login page)
    driver.get("https://banking.dkb.de/login")

    # Initialize ActionChains to perform actions like mouse movements and keystrokes
    actions = ActionChains(driver)

    # Logging in with provided credentials
    # Find the username input field, click on it, and enter the username '123456789'
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-testid="sui-input-username"]'))).click()
    username = driver.find_element(By.CSS_SELECTOR, 'input#username')
    actions.move_to_element(username).send_keys('123456789').perform()

    # Find the password input field, click on it, and enter the password 'abcdefg'
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-testid="sui-input-password"]'))).click()
    password = driver.find_element(By.CSS_SELECTOR, 'input#password')
    actions.move_to_element(password).send_keys('abcdefg').perform()

    # Press the Enter key to submit the login form
    password.send_keys(Keys.ENTER)

    # Wait for 2 seconds (to allow the page to load or perform further actions)
    time.sleep(2)

# Call the main function to start the script
main()

"""
reference:
https://stackoverflow.com/questions/76749285/i-cannot-send-keys-because-element-not-interactable-in-selenium-web-automation
"""
