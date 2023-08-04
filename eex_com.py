"""
Project : EEX.COM
Author : Ajeet
Date : August 4, 2023
"""

import time
import pandas as pd
from selenium.webdriver import Chrome, ChromeOptions, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def data_by_date(day: int, month: int, year: int) -> pd.DataFrame:
    """
    Scrape data for a specific date from the EEX German Power Futures.

    Args:
        day (int): The day of the month (1 to 31).
        month (int): The month (1 to 12).
        year (int): The year.

    Returns:
        pandas.DataFrame: A DataFrame containing the scraped data for the specified date.
                          The DataFrame includes details about futures contracts.
    """

    options = ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = Chrome(options=options)
    wait = WebDriverWait(driver, 20)

    driver.get(url='https://www.eex.com/en/market-data/power/futures')
    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='I accept all cookies.']"))).click()
    time.sleep(3)
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button.btn.dropdown-toggle.form.input-select div.filter-option-inner"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,
                                           "//div[@class='dropdown-menu show']//li/a[@class='dropdown-item']/span[contains(., 'EEX German Power Futures')]"))).click()

    # Find and set the date input field to the desired date
    calender_container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#symbolheader_pfpde')))
    date_input = calender_container.find_element(By.CSS_SELECTOR, 'input.mv-input-box')
    date_input.clear()
    date_input.send_keys(f'{year}-{month}-{day}')
    date_input.send_keys(Keys.ENTER)

    table_data = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div#baseloadwidget_pfpde > table.mv-quote")))
    # Find the table containing the data and extract column names
    columns = [i.text for i in table_data.find_elements(By.CSS_SELECTOR, 'tr.mv-quote-header-row>th')]

    all_data = []

    # Loop through each row of the table and extract data for each cell
    for row in WebDriverWait(table_data, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'tbody>tr'))):
        data = [i.text for i in row.find_elements(By.CSS_SELECTOR, 'td[style^="text-align:"]')]
        all_data.append(data)

    # Create a Pandas DataFrame with the scraped data and return it
    df = pd.DataFrame(data=all_data, columns=columns[:-1])
    return df


print(data_by_date(day=2, month=8, year=2023))

"""
output:

   Future Last Price Last Volume Settlement Price Volume Exchange Volume Trade Registration Open Interest
0  Cal-24     134.00       8,784           134.52       2,714,256                 2,643,984        72,459
1  Cal-25     124.75       8,760           124.67         604,440                   289,080        17,377
2  Cal-26     106.00       8,760           105.59          87,600                   350,400         4,072
3  Cal-27      90.25       8,760            90.23          17,520                   113,880           787
4  Cal-28          -           -            84.18               -                         -           111
5  Cal-29          -           -            82.65               -                         -            13
6  Cal-30          -           -            83.11               -                         -             7
7  Cal-31          -           -            82.93               -                         -             2
8  Cal-32          -           -            82.78               -                         -             2
9  Cal-33          -           -            81.93               -                         -             0

reference:
https://stackoverflow.com/questions/76826884/getting-data-for-different-dates-when-scraping-data-with-selenium
"""
