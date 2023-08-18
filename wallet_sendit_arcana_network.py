"""
Project : https://sendit.arcana.network/app/login
Author : Ajeet
Date : August 18, 2023
"""

import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options = ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)
driver.get(url="https://sendit.arcana.network/app/login")

# Click on the "Connect Wallet" button on the page
wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()=" Connect Wallet "]'))).click()
time.sleep(2)

# Click on the "View All" to see all wallet options
driver.execute_script(
    """document.querySelector('w3m-modal').shadowRoot.querySelector('w3m-modal-router').shadowRoot.querySelector('w3m-connect-wallet-view').shadowRoot.querySelector('w3m-desktop-wallet-selection').shadowRoot.querySelector('w3m-modal-footer').querySelector('div.w3m-grid').querySelector('w3m-view-all-wallets-button').shadowRoot.querySelector('button').click();""")

time.sleep(2)
# Click on the "MetaMask" wallet option
driver.execute_script(
"""document.querySelector('w3m-modal').shadowRoot.querySelector('w3m-modal-router').shadowRoot.querySelector('w3m-wallet-explorer-view').shadowRoot.querySelector('div.w3m-grid').querySelector('[name="MetaMask"]').shadowRoot.querySelector('button').click();""")

time.sleep(2)

"""
reference: 
https://stackoverflow.com/questions/76922866/how-to-authorise-in-walletconnect-using-python
"""