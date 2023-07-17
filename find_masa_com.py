"""
Project : 
Author : Ajeet
Date : July 17, 2023
"""

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

# Create a Chrome driver instance
driver = Chrome()

url = 'https://findmasa.com/view/map#b1cc410b'
driver.get(url)

# Wait for the li element with id 'b1cc410b' to be present on the page
li_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li#b1cc410b')))

data_lat = li_element.get_attribute('data-lat')
data_lng = li_element.get_attribute('data-lng')
artist_name = li_element.find_element(By.TAG_NAME, 'a').text
address = li_element.find_elements(By.TAG_NAME, 'p')[1].text
city = li_element.find_elements(By.TAG_NAME, 'p')[2].text

# Print the extracted data
print(data_lat)
print(data_lng)
print(artist_name)
print(address)
print(city)

"""
The information you're looking for gets loaded slowly and involves Javascript. As the requests library doesn't support 
the javascript, it doesn't return the content/information and thus your if-statement gets False. So, it goes to the 
else-statement and you get NO DATA.

output:
34.102025
-118.32694167
Tristan Eaton
6301 Hollywood Boulevard
Los Angeles, California

reference:
https://stackoverflow.com/questions/76700158/how-to-use-python-to-get-information-from-the-map-navigation-container-of-a-webs
"""