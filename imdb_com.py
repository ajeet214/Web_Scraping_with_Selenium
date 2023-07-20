"""
Project : IMDB title review
Author : Ajeet
Date : July 20, 2023
"""

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

url = "https://www.imdb.com/title/tt0368226/reviews"

options = Options()
# options.add_argument('-headless')
driver = webdriver.Firefox(options=options)

# Load the IMDb page
driver.get(url)

while True:
    try:
        button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'load-more-trigger')))

        button.click()
    except (NoSuchElementException, TimeoutException):
        break

"""
The while-loop will keep looking for the Load More button and keep clicking on it until there are no more Load More 
and finally it'll get timed out and break out of the loop.

reference:
https://stackoverflow.com/questions/76726412/movetargetoutofboundsexception-selenium-python-firefox
"""