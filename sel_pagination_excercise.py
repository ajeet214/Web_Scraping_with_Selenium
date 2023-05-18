from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time


def scrape_page_data():
    WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'results-wrapped')))
    container = driver.find_element(By.CLASS_NAME, 'results-wrapped')

    # scroll down to load all content on the page
    for i in range(4):
        driver.execute_script("window.scrollBy(0, 2000);")
        time.sleep(2)

    skus = container.find_elements(By.CLASS_NAME, 'product-identifier--bd1f5')
    prices = container.find_elements(By.CLASS_NAME, 'price-format__main-price')

    return skus, prices


def pagination(url, pages=1):
    prod_num = []
    prod_price = []

    page_num = 0
    # iterate over the pages
    for i in range(1, pages+1):

        print(f"this is page {i}")
        driver.get(f"{url}?Nao={page_num}")
        skus, prices = scrape_page_data()

        for sku in skus:
            prod_num.append(sku.text)
        for price in prices:
            prod_price.append(price.text)

        # increment it by 24 since each page has 24 data
        page_num += 24
        time.sleep(1)

    return prod_num, prod_price


website = 'https://www.homedepot.com/b/Milwaukee/Special-Values/N-5yc1vZ7Zzv'
driver = webdriver.Chrome()
prod_num, prod_price = pagination(website, pages=3)

df = pd.DataFrame({'code': prod_num, 'price': prod_price})
df.to_csv('HD_test.csv', index=False)
print(df)

