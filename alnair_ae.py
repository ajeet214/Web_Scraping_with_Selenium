"""
Project : Alnair
Author : Ajeet
Date : July 29, 2023
"""

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


URL_alnair = 'https://alnair.ae/app/view/1412/3386/apartment/apartments'
o = Options()
o.add_experimental_option('detach', True)
o.add_argument('--start-maximized')

driver = Chrome(service=ChromeService(ChromeDriverManager().install()), options=o)

def get_data():
    driver.get(URL_alnair)
    driver.set_page_load_timeout(2)

    scroll_bar = driver.find_element(By.CSS_SELECTOR, 'div[class^="_scrollContainer_"]')
    driver.execute_script("arguments[0].scrollBy(0, arguments[0].scrollHeight);", scroll_bar)

get_data()


"""
- You first need to find/locate the scrollbar which is embedded in the HTML page.
- The web-element <div class="_scrollContainer_1ah3s_14"> represents the scrollbar which can be located using the 
mentioned strategy.
- Once we find the web element for the scrollbar, simply can scroll down to its height.

reference:
https://stackoverflow.com/questions/76791670/scrolling-using-selenium4-10-0
"""