"""
Project : Lidl GB
Author : Ajeet
Date : 07/06/2023
"""
import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options = ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)
url = "https://www.lidl.co.uk/about-us/store-finder-opening-hours#"
driver.get(url)

# wait for element to get located to click the "ACCEPT" cookies button
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.cookie-alert-extended-button"))).click()
# wait for element to get located to click the "STORE SEARCH" button
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.nuc-m-button.nuc-a-button"))).click()
# wait for element to get located to Enter post code or city
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter post code or city"]'))).send_keys('London')

time.sleep(10)


"""
Few things to note:

1. First, as we hit the URL, a cookie pops up that we can accept to continue. So we wait for this pop-up and click on the ACCEPT button.
2. Next, we wait for the STORE SEARCH button to get located and then click.
3. It loads a side search box where we can enter the city or the postcode to search. So we wait for this to get loaded/located in order to enter the query. we can use send_keys() method to enter/input either the city name or the postcode.

for example, as we enter the city name/postcode (London), a dropdown list appears with available stores in that region, you can choose accordingly and proceed further.
reference:
https://stackoverflow.com/questions/76392044/how-can-i-locate-and-enter-text-in-the-search-box-on-lidls-website-using-seleni
"""