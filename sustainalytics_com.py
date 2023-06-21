"""
Project : 
Author : Ajeet
Date : June 21, 2023
"""
import time
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = ChromeOptions()
options.add_argument('--start-maximized')

driver = Chrome(options=options)
wait = WebDriverWait(driver, 10)
url = "https://www.sustainalytics.com/esg-ratings"
driver.get(url)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a#hs-eu-confirmation-button'))).click()

data = []


def data_processing(source):
    soup = BeautifulSoup(source, "html.parser")
    selected_page = soup.select_one('span.pagination-page.selected').text
    print(f"---------------------- This is page {selected_page} ----------------------")

    container = soup.select_one('section#company_ratings')
    company_rows = container.find_all(class_='company-row')

    for company_row in company_rows:
        company_name = company_row.find(class_='primary-color').get_text()
        esg_risk_rating = company_row.find(class_='col-2').get_text()

        print(f"Company: {company_name} | Rating: {esg_risk_rating}")
        data.append({"Company": company_name, "Rating": esg_risk_rating})


def first_page():
    # process the 1st page
    data_processing(driver.page_source)
    return f"data:\n{data}"


def multiple_page(page_num):
    # process the first page
    data_processing(driver.page_source)

    # click and process next pages
    for i in range(2, page_num+1):
        driver.execute_script(f"""
        function getElementByXpath(path) {{
           return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        }};
        getElementByXpath('//*[@id="victor-pagination"]/a[@class="pagination-page" and text()="{i}"]').click();
        """)

        time.sleep(2)
        data_processing(driver.page_source)

    return f"data:\n{data}"


if __name__ == '__main__':
    # print(first_page())
    print(multiple_page(4))

"""
output:

---------------------- This is page 1 ----------------------
Company: 1-800-FLOWERS.COM, Inc. | Rating: 23.6
Company: 1&1 AG | Rating: 22.2
Company: 10X Genomics, Inc. | Rating: 22.6
Company: 11 Bit Studios SA | Rating: 16.3
Company: 1Life Healthcare, Inc. | Rating: 22.5
Company: 1st Source Corp. | Rating: 31.7
Company: 1stdibs.com, Inc. | Rating: 26.7
Company: 22nd Century Group, Inc. | Rating: 35.4
Company: 23andMe Holding Co. | Rating: 25.6
Company: 29metals Ltd. | Rating: 42.8
---------------------- This is page 2 ----------------------
Company: 2i Rete Gas SpA | Rating: 25.2
Company: 2seventy Bio, Inc. | Rating: 32.0
Company: 2U, Inc. | Rating: 26.8
Company: 360 DigiTech, Inc. | Rating: 28.4
Company: 360 One Wam Ltd. | Rating: 33.3
Company: 360 Security Technology, Inc. | Rating: 23.1
Company: 361 Degrees International Ltd. | Rating: 18.6
Company: 37 Interactive Entertainment Network Technology Group Co. Ltd. | Rating: 14.3
Company: 3D Systems Corp. | Rating: 23.0
Company: 3i Group Plc | Rating: 11.1
---------------------- This is page 3 ----------------------
Company: 3M Co. | Rating: 33.9
Company: 3M India Ltd. | Rating: 23.4
Company: 3R Petroleum Óleo e Gás SA | Rating: 56.7
Company: 3SBio, Inc. | Rating: 27.1
Company: 407 East Development Group GP | Rating: 45.7
Company: 407 International, Inc. | Rating: 11.4
Company: 4D Molecular Therapeutics, Inc. | Rating: 28.4
Company: 4imprint Group Plc | Rating: 17.2
Company: 5E Advanced Materials, Inc. | Rating: 42.0
Company: 5I5J Holding Group Co. Ltd. | Rating: 15.0
---------------------- This is page 4 ----------------------
Company: 7-Eleven Malaysia Holdings Bhd. | Rating: 24.6
Company: 7-Eleven, Inc. | Rating: 35.1
Company: 888 Holdings Plc | Rating: 18.7
Company: 8x8, Inc. | Rating: 29.9
Company: 908 Devices, Inc. | Rating: 36.8
Company: 91APP, Inc. | Rating: 25.8
Company: A-Living Smart City Services Co., Ltd. | Rating: 9.3
Company: A-Mark Precious Metals, Inc. | Rating: 30.3
Company: A. O. Smith Corp. | Rating: 25.4
Company: A.G. BARR Plc | Rating: 23.7
data:
[{'Company': '1-800-FLOWERS.COM, Inc.', 'Rating': '23.6'}, {'Company': '1&1 AG', 'Rating': '22.2'}, {'Company': '10X Genomics, Inc.', 'Rating': '22.6'}, {'Company': '11 Bit Studios SA', 'Rating': '16.3'}, {'Company': '1Life Healthcare, Inc.', 'Rating': '22.5'}, {'Company': '1st Source Corp.', 'Rating': '31.7'}, {'Company': '1stdibs.com, Inc.', 'Rating': '26.7'}, {'Company': '22nd Century Group, Inc.', 'Rating': '35.4'}, {'Company': '23andMe Holding Co.', 'Rating': '25.6'}, {'Company': '29metals Ltd.', 'Rating': '42.8'}, {'Company': '2i Rete Gas SpA', 'Rating': '25.2'}, {'Company': '2seventy Bio, Inc.', 'Rating': '32.0'}, {'Company': '2U, Inc.', 'Rating': '26.8'}, {'Company': '360 DigiTech, Inc.', 'Rating': '28.4'}, {'Company': '360 One Wam Ltd.', 'Rating': '33.3'}, {'Company': '360 Security Technology, Inc.', 'Rating': '23.1'}, {'Company': '361 Degrees International Ltd.', 'Rating': '18.6'}, {'Company': '37 Interactive Entertainment Network Technology Group Co. Ltd.', 'Rating': '14.3'}, {'Company': '3D Systems Corp.', 'Rating': '23.0'}, {'Company': '3i Group Plc', 'Rating': '11.1'}, {'Company': '3M Co.', 'Rating': '33.9'}, {'Company': '3M India Ltd.', 'Rating': '23.4'}, {'Company': '3R Petroleum Óleo e Gás SA', 'Rating': '56.7'}, {'Company': '3SBio, Inc.', 'Rating': '27.1'}, {'Company': '407 East Development Group GP', 'Rating': '45.7'}, {'Company': '407 International, Inc.', 'Rating': '11.4'}, {'Company': '4D Molecular Therapeutics, Inc.', 'Rating': '28.4'}, {'Company': '4imprint Group Plc', 'Rating': '17.2'}, {'Company': '5E Advanced Materials, Inc.', 'Rating': '42.0'}, {'Company': '5I5J Holding Group Co. Ltd.', 'Rating': '15.0'}, {'Company': '7-Eleven Malaysia Holdings Bhd.', 'Rating': '24.6'}, {'Company': '7-Eleven, Inc.', 'Rating': '35.1'}, {'Company': '888 Holdings Plc', 'Rating': '18.7'}, {'Company': '8x8, Inc.', 'Rating': '29.9'}, {'Company': '908 Devices, Inc.', 'Rating': '36.8'}, {'Company': '91APP, Inc.', 'Rating': '25.8'}, {'Company': 'A-Living Smart City Services Co., Ltd.', 'Rating': '9.3'}, {'Company': 'A-Mark Precious Metals, Inc.', 'Rating': '30.3'}, {'Company': 'A. O. Smith Corp.', 'Rating': '25.4'}, {'Company': 'A.G. BARR Plc', 'Rating': '23.7'}]
"""

"""
reference:
https://stackoverflow.com/questions/76513303/scraping-a-website-for-multiple-pages-that-url-does-not-c
"""