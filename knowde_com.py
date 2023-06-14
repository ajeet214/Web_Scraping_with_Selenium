"""
Project : Knowde
Author : Ajeet
Date : June 14, 2023
"""

# import libraries
import logging
import os
from typing import List, Dict, Optional
from selenium.webdriver import Chrome, ChromeOptions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
import pandas as pd

logging.basicConfig(filename='knoede_log.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)


class KnoedeData:
    def __init__(self):

        options = ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.driver = Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)
        self.website = "https://www.knowde.com/b/markets-personal-care/products/"
        self.data = []
        self.driver.get(self.website)
        # accept all cookies
        self.wait.until(EC.visibility_of_element_located((By.ID, 'onetrust-accept-btn-handler'))).click()

    @staticmethod
    def data_processing(prod: WebElement) -> Dict:
        """this method process/parse the individual product information

        Args:
        prod: this is the selenium Webelement with the product container

        Returns:
             a dict of all the extracted product information for a single product
        """
        brand = prod.find_element('xpath', './a/div[2]/div/p[1]').text
        item = prod.find_element('xpath', './a/div[2]/div/p[2]').text
        inci_name = prod.find_element('xpath', './a/div[2]/div/div[1]/span[2]').text

        try:
            ingredient_origin = prod.find_element('xpath', './a/div[2]/div/div[3]/span[2]').text
        except NoSuchElementException:
            ingredient_origin = 'null'
        try:
            function = prod.find_element('xpath', './a/div[2]/div/div[2]/span[2]').text
        except NoSuchElementException:
            function = 'null'
        try:
            benefit_claims = prod.find_element('xpath', './a/div[2]/div/div[4]/span[2]').text
        except NoSuchElementException:
            benefit_claims = 'null'
        try:
            description = prod.find_element('xpath', './a/div[2]/div/p[3]').text
        except NoSuchElementException:
            description = 'null'
        try:
            labeling_claims = prod.find_element('xpath', './a/div[2]/div/div[5]/span[2]').text
        except NoSuchElementException:
            labeling_claims = 'null'
        try:
            compliance = prod.find_element('xpath', './a/div[2]/div/div[6]/span[2]').text
        except NoSuchElementException:
            compliance = 'null'
        try:
            hlb_value = prod.find_element('xpath', './a/div[2]/div/div[4]/span[2]').text
        except NoSuchElementException:
            hlb_value = 'null'
        try:
            end_uses = prod.find_element('xpath', '/a/div[2]/div/div[4]/span[2]').text
        except NoSuchElementException:
            end_uses = 'null'
        try:
            cas_no = prod.find_element('xpath', './a/div[2]/div/div[5]/span[2]').text
        except NoSuchElementException:
            cas_no = 'null'
        try:
            chemical_name = prod.find_element('xpath', './a/div[2]/div/div[2]/span[2]').text
        except NoSuchElementException:
            chemical_name = 'null'
        try:
            synonyms = prod.find_element('xpath', './a/div[2]/div/div[6]/span[2]').text
        except NoSuchElementException:
            synonyms = 'null'
        try:
            chemical_family = prod.find_element('xpath', './a/div[2]/div/div[5]/span[2]').text
        except NoSuchElementException:
            chemical_family = 'null'
        try:
            features = prod.find_element('xpath', './a/div[2]/div/div[7]/span[2]').text
        except NoSuchElementException:
            features = 'null'
        try:
            grade = prod.find_element('xpath', './a/div[2]/div/div[5]/span[2]').text
        except NoSuchElementException:
            grade = 'null'

        logging.info(f'Saving: {brand}')
        return {
            'brand': brand,
            'item': item,
            'inci_name': inci_name,
            'ingredient_origin': ingredient_origin,
            'function': function,
            'benefit_claims': benefit_claims,
            'description': description,
            'labeling_claims': labeling_claims,
            'compliance': compliance,
            'hlb_value': hlb_value,
            'end_uses': end_uses,
            'cas_no': cas_no,
            'chemical_name': chemical_name,
            'synonyms': synonyms,
            'chemical_family': chemical_family,
            'features': features,
            'grade': grade
        }

    def single_page(self, page_num: int) -> List[Dict]:
        """ this method scraps the data from the given page number of the website.

        Args:
        page_num: the page number to extract the data from

        Returns: self.data(list of dict of all products on a given page)
        """

        self.driver.get(f"{self.website}{page_num}")
        logging.info(f"-------page number {page_num} -------")
        products = self.driver.find_elements(By.CSS_SELECTOR, 'div[data-cy="product-card"]')

        count = 0
        for product in products:
            if count == 0 or count == count + 4:
                product.find_element(By.CSS_SELECTOR, 'svg[data-testid="icon-icomoon--keyboard_arrow_down"]').click()

            self.data.append(self.data_processing(product))
            count += 1

        return self.data

    def multiple_page(self, start: int, end: int) -> None:
        """ the method iterates over the range of given page numbers.

        Args:
        start: the page number to start with
        end: the page number to end with

        Returns: None
        """

        for page in range(start, end+1):
            self.single_page(page)

    @staticmethod
    def save_data(data: List[Dict], path: Optional[str] = os.getcwd()) -> None:
        """ save the data to a CSV file at the given path.

        Args:
        data: the data to save.
        path: the path to save the file (the default is os.getcwd(), which saves the file in the current directory)

        Returns: None
        """

        df = pd.DataFrame(data)
        df.to_csv(f'{path}/cosmetics_data.csv', index=False)


if __name__ == '__main__':

    obj = KnoedeData()
    print(obj.single_page(3))
    # obj.save_data(obj.single_page(2))
    # print(obj.multiple_page(1, 3))


"""
Few things to note:

1. The very first time we open the website, we need to click on the button Accept All Cookies.
2. Next, we can find all the 36 products on the page using the selector div[data-cy="product-card"]
3. You might notice that in a full window size, the page loads 4 products in a row and as we click on the down-arrow of 1st product to see more details, it also opens for the remaining 3 products on that row. So we just need to click once per row.
4. To implement the logic of clicking only once per row, we used a count variable as you can see in the code above.

reference:
https://stackoverflow.com/questions/76468614/selenium-python-timeoutexception
"""
