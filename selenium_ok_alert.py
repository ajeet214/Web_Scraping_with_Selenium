import time
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.common import NoAlertPresentException

options = ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument("force-device-scale-factor=0.95")

driver = Chrome(options=options)

urls = ['https://web.archive.org/web/20080221233711/http://www.berkshire.com/',
        'https://web.archive.org/web/20171107004101/http://www.berkshirefunds.com/',
        'https://web.archive.org/web/20200224044229/http://www.berkshirefunds.com/']

for i, url in enumerate(urls):
    driver.get(url)
    time.sleep(5)

    if url.endswith('www.berkshire.com/'):
        target_element = driver.find_element(By.TAG_NAME, 'tbody')
        target_element.screenshot(f'{i}_screen_capture.png')

    elif url.endswith('www.berkshirefunds.com/'):
        try:
            # ---------------------------------------------------------------------------------------------
            driver.switch_to.alert.accept()
            # ---------------------------------------------------------------------------------------------
        except NoAlertPresentException:
            pass
        target_element = driver.find_element(By.CSS_SELECTOR, 'div#page-wrap')
        target_element.screenshot(f'{i}_screen_capture.png')
