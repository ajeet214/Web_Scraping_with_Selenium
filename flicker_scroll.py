"""
Project : flicker
Author : Ajeet
Date : Sep. 22, 2023
"""

import time
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
url = "https://www.flickr.com/groups/allfreepictures/pool/page3041"

driver.get(url=url)

# scroll to the bottom of the page to load all available images
flag = True
last_height = driver.execute_script("return document.body.scrollHeight")
while flag:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        flag = False
    else:
        last_height = new_height

time.sleep(2)

soup = BeautifulSoup(driver.page_source, 'html.parser')
image_urls = [link['href'] for link in soup.findAll("a", {"class": "overlay"})]
print(len(image_urls))
print(image_urls)

"""
reference:
https://stackoverflow.com/questions/77155340/selenium-scroll-flickr-page-to-get-all-the-images
"""