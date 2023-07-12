"""
Project : Wallet Polygon Technology
Author : Ajeet
Date : July 12, 2023
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
wait = WebDriverWait(driver, 10)
url = "https://wallet.polygon.technology/?redirectOnConnect=zkEVM_bridge"

driver.get(url)
# click on the "Connect to a Wallet" button
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.navbar__apps-section__auth__login"))).click()
time.sleep(2)
driver.execute_script("""document.querySelector('w3m-modal').shadowRoot.querySelector('w3m-modal-router').shadowRoot.querySelector('w3m-connect-wallet-view').shadowRoot.querySelector('w3m-desktop-wallet-selection').shadowRoot.querySelector('w3m-modal-footer').querySelectorAll('w3m-wallet-button')[0].shadowRoot.querySelector('button').click();""")
time.sleep(5)

"""
- Various elements on this website are embedded inside the shadow-root.
- for example, your target/desired button is embedded in a 5-layer nested shadow-root.
- After clicking on the Connect to a Wallet, we wait for 1-2 seconds just to make sure that the overlay window is 
  visibly present, although it appears very quickly.
- The used javascript query to locate and click on the desired button:

  document.querySelector('w3m-modal').shadowRoot.querySelector('w3m-modal-router').shadowRoot.querySelector('w3m-connect-wallet-view').shadowRoot.querySelector('w3m-desktop-wallet-selection').shadowRoot.querySelector('w3m-modal-footer').querySelectorAll('w3m-wallet-button')[0].shadowRoot.querySelector('button').click();
  
  will click on the very first wallet, if you like to click on the 2nd or 3rd wallet option, just simply replace 
  the querySelectorAll('w3m-wallet-button')[0] with querySelectorAll('w3m-wallet-button')[1] or 
  querySelectorAll('w3m-wallet-button')[2] respectively in the above-mentioned javascript query.

reference:
https://stackoverflow.com/questions/76658230/selenium-how-to-get-element-in-shadow-root-of-html-page-code
"""