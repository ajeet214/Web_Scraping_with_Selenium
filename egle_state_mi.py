"""
Project : EGLE State, Remediation Information Data Exchange
Author : Ajeet
Date : 09/06/2023
"""
import os
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def download_file(path):

    options = ChromeOptions()
    options.add_argument('--start-maximized')
    prefs = {'download.default_directory': path}
    options.add_experimental_option('prefs', prefs)

    driver = Chrome(options=options)
    driver.get('https://www.egle.state.mi.us/RIDE/inventory-of-facilities/facilities')
    wait = WebDriverWait(driver, 100)

    wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'mat-table')))
    driver.execute_script('''document.querySelector("button[aria-label='Export Facilities Table results to CSV']").click();''')

    while True:
        is_exist = os.path.exists(f"{path}\\Facilities.csv")
        if is_exist:
            print(f"The file is downloaded!")
            break


if __name__ == '__main__':
    PATH = 'D:\\test'
    download_file(PATH)

    """
    output:
    The file is downloaded!
    """

"""
steps to follow:

1. As the site takes some time to load the desired element (here, the Export button). And clicking on this button downloads 
the data of the table. Therefore we wait to make sure that the table data is already loaded.

2. Now that the data is already loaded, simply click on the Export button to download the data (here Facilities.csv).

3. It takes some time for the file to get downloaded at the given path, so we need to wait until the file download is 
completed. To do this, we keep checking if the file is present at the given path, and once the file is there, we break 
the loop.

reference:
https://stackoverflow.com/questions/76436438/selenium-cant-find-element-by-xpath
"""
