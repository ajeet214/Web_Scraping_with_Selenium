"""
Project : Instagram
Author : Ajeet
Date : June 20, 2023
"""
import time
import json
from typing import Optional

from selenium import webdriver
from selenium.webdriver import ChromeOptions, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver

from credentials import creds


class Instagram:

    def __init__(self):
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])

        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)

    def login(self, username, password):
        self.driver.get("https://www.instagram.com/")
        # username
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="username"]'))).send_keys(username)
        # password
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="password"]'))).send_keys(password+Keys.ENTER)
        # click on "Not Now" to close "Save Your Login Info?"
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//div[text()="Not Now"]'))).click()

    def save_cookies(self, username: str, password: str, path: str) -> None:
        self.login(username, password)
        json_object = json.dumps(self.driver.get_cookies())

        # Writing to instagram_cookies.json
        with open(path, "w") as outfile:
            outfile.write(json_object)

    def load_cookies(self, path: str) -> WebDriver:
        self.driver.get("https://www.instagram.com/")

        # Opening JSON file
        f = open(path)
        cookies = json.load(f)
        # load cookies to the driver
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        time.sleep(1)
        # refresh the browser
        self.driver.refresh()
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//button[text()="Not Now"]'))).click()
        time.sleep(1)

        return self.driver


if __name__ == '__main__':
    obj = Instagram()
    # obj.login(creds['instagram_username'], creds['instagram_password'])
    # obj.save_cookies(creds['instagram_username'], creds['instagram_password'], 'D:\\automation\InstagramAPI\instgram_cookies.json')
    # obj.load_cookies('D:\\automation\InstagramAPI\instgram_cookies.json')
