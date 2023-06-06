"""
Project : mercedes-benz Scrapper
Author : Ajeet
Date : 06/06/2023
"""

import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions, Keys
from selenium.webdriver.common.by import By

options = ChromeOptions()

options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=options)

url = "https://www.mercedes-benz.co.in/passengercars/buy/new-car/search-results.html/?emhsort=price-asc&emhvehicleAssortment=vehicles&emhstockType=IN_STOCK"
driver.get(url)
time.sleep(5)
# click on the "Agree to all" button to proceed
shadow_element_1 = driver.find_element(By.CSS_SELECTOR, "cmm-cookie-banner.hydrated").shadow_root
shadow_element_1.find_element(By.CSS_SELECTOR, 'div.button-group').find_element(By.XPATH, 'button[text()="Agree to all"]').click()

# enter the pin code to proceed further
shadow_element_2 = driver.find_element(By.CSS_SELECTOR, 'dh-io-emh-region-picker[class="webcomponent webcomponent-nested"]').shadow_root
region_picker = shadow_element_2.find_element(By.CSS_SELECTOR, 'input#postCodeInput')
region_picker.send_keys(110001)
region_picker.send_keys(Keys.ENTER)

# parse the search results
shadow_element_3 = driver.find_element(By.CSS_SELECTOR, 'emh-search-result[data-component-name="emh-search-result"]').shadow_root
search_container = shadow_element_3.find_element(By.CSS_SELECTOR, 'div.dcp-cars-srp__results.dcp-cars-srp-results.srp-grid-layout__results')
results = search_container.find_elements(By.CSS_SELECTOR, 'div.dcp-cars-srp-results__tile')

for result in results:
    print(result.find_element(By.CSS_SELECTOR, 'h2.wb-vehicle-tile__title').text)

time.sleep(5)

"""
output:

GLB200
GLB200
GLB200
C220d MY23
C220d MY23
C220d MY23
C220d MY23
C220d MY23
C220d MY23
C220d MY23
C220d MY23
C220d MY23
"""

"""
Things to notice:

1. First of all, we need to find and click on the Agree to all button which lies under a shadow-root.
2. Next, we need to find and input the pin code (which again lies under a shadow-root) to proceed further.
3. Finally, we get to the search page where we can see 12 different search results. We find the element (this element also lies under a shadow-root) which contains the search results data.

The variable results holds all the 12 results on the page and we can iterate over it to extract/parse all the pieces of information.

reference:
https://stackoverflow.com/questions/76408371/why-does-xpath-half-work-in-this-web-page
"""