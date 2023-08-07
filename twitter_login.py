"""
Project : Twitter Login
Author : Ajeet
Date : August 7, 2023
"""

import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def login_twitter(username: str, password: str) -> None:
    """
    Log in to Twitter using the provided username and password.

    This function automates the login process on Twitter using Selenium WebDriver.
    It opens the Twitter login page, enters the provided username and password, and submits the form.

    Parameters:
    username (str): The Twitter username to log in with.
    password (str): The Twitter password for the specified username.

    Returns:
    None
    """
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(options=options)

    # Open the Twitter login page
    url = "https://twitter.com/i/flow/login"
    driver.get(url)

    # Find and input the username
    username_input = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="username"]')))
    username_input.send_keys(username)
    username_input.send_keys(Keys.ENTER)

    # Find and input the password
    password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)

    # Wait for a short period (e.g., 10 seconds) to ensure the login process completes
    time.sleep(10)


if __name__ == "__main__":
    your_username = "your_twitter_username_here"
    your_password = "your_twitter_password_here"

    # Call the login_twitter function with your Twitter credentials
    login_twitter(your_username, your_password)
