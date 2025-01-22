"""
Author: Ajeet
Created: 1/11/2025
Description: This script automates the process of navigating to the NSE India announcements page,
             selecting the SME tab, switching to the "1W" (1 Week) filter, and downloading the
             announcements in a CSV file format.
Project: Automation
"""
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Selenium WebDriver (using undetected_chromedriver to bypass bot detection)
driver = uc.Chrome()

# Define an explicit wait for elements
wait = WebDriverWait(driver, 10)

try:
    # Step 1: Open the NSE India announcements page
    print("Opening NSE announcements page...")
    driver.get("https://www.nseindia.com/companies-listing/corporate-filings-announcements")

    # Step 2: Select the SME tab
    sme_tab = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#containTabNav > li:nth-child(2) > a")))
    sme_tab.click()
    time.sleep(2) # Pause to allow the page content to load

    # Step 3: Select the "1W" (1 Week) tab
    one_week_tab = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[id="Announcements_sme"]>div:nth-child(2)>div>div.block-detail-dates-box>div>div>ul>li:nth-child(2)')))
    one_week_tab.click()
    time.sleep(2) # Pause to allow the filtered content to load

    # Step 4: Wait for the table containing announcements to load
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#CFanncsmeTable>tbody>tr>td>a')))

    # Step 5: Download the CSV file
    print("Downloading CSV file...")
    download = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#CFanncsme-download')))
    download.click()

    # Pause to allow the download process to complete
    time.sleep(3)
    print(f"File downloaded!")

except Exception as e:
    # Handle any unexpected errors and print a user-friendly message
    print(f"An unexpected error occurred: {e}")

"""
output:
Opening NSE announcements page...
Downloading CSV file...
File downloaded!

stackoverflow link: https://stackoverflow.com/a/79349087/11179336
"""