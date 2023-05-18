from selenium import webdriver
from selenium.webdriver.common.by import By

import ddddocr

driver = webdriver.Chrome()

driver.get('https://ma.mohw.gov.tw/masearch/')

captcha = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ImageCheck")

# ----------------------------------------------------------------------------------------------------------------
captcha.screenshot(f'captcha.png')
# ----------------------------------------------------------------------------------------------------------------

ocr = ddddocr.DdddOcr()
# open and read the image
with open(f'captcha.png', 'rb') as f:
    img_bytes = f.read()

res = ocr.classification(img_bytes)
print(res.upper())
