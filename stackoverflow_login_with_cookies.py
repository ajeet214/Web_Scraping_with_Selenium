import time
import json
from selenium import webdriver
from selenium.webdriver import ChromeOptions


def login():
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--incognito")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extension")
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    # create chrome driver object with options
    driver = webdriver.Chrome(options=options)

    # open then website
    driver.get("https://stackoverflow.com")

    # Opening JSON file
    f = open('stackoverflow_cookies.json')
    cookies = json.load(f)
    # load cookies to the driver
    for cookie in cookies:
        driver.add_cookie(cookie)

    time.sleep(2)
    # refresh the browser
    driver.refresh()

    return driver


if __name__ == '__main__':
    login()






