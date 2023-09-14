"""
Project : 
Author : Ajeet
Date : September 14, 2023
"""
import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])

# Specify the Chrome profile directory to use (Profile 2)
options.add_argument('--profile-directory=Profile 2')

# Specify the user data directory where Chrome profile data is stored
options.add_argument("--user-data-dir=C:\\Users\\PC\\AppData\\Local\\Google\\Chrome\\User Data\\")

driver = webdriver.Chrome(options=options)
driver.get("https://www.instagram.com/")

time.sleep(5)


"""
Things to note:

1. Ensure Chrome is Closed:
Make sure that all instances of Chrome are closed before running your Selenium script. Sometimes, if Chrome is running in the background or doesn't shut down correctly, it can cause issues when trying to start a new instance.

2. Check ChromeDriver Version:
Ensure that your ChromeDriver version matches the version of Google Chrome installed on your system. If they don't match, it can lead to compatibility issues.

reference:
https://stackoverflow.com/questions/77099511/im-developing-an-application-in-python-using-selenium-and-to-make-it-work-i
"""

