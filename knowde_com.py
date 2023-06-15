"""
Project : Knowde
Author : Ajeet
Date : June 15, 2023
"""
# import libraries
import os
import logging
import pandas as pd
from bs4 import BeautifulSoup
from typing import List, Dict, Optional
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# logging configurations
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
    def find_siblings(container: BeautifulSoup.string, category: str) -> str:
        """this method returns the text value across the given category if found/available.
        Args:
        container: a 'BeautifulSoup.string' containing all the textual details of an individual product.
        category: the name of the category across which we are trying to get the details.

        Returns:
        category_text: the details/value across the given text category
        """
        label = container.find("span", string=f"{category}: ")
        if label:
            category_text = label.next_sibling.text
        else:
            category_text = None

        return category_text

    def data_processing(self, page_source: str) -> None:
        """this method process/parse the individual product information

        Args:
        page_source: this is the page source of the selenium webdriver

        Returns: None
        """
        soup = BeautifulSoup(page_source, 'html.parser')
        product_containers = soup.select('div[data-cy="product-card"]')

        for container in product_containers:
            text_container = container.select_one('div[direction="column"]')

            brand = text_container.select_one('p[data-cy="product-brand-name"]').text
            item = text_container.select_one('p[data-cy="product-name"]').text

            inci_name = self.find_siblings(text_container, 'INCI Name')
            ingredient_origin = self.find_siblings(text_container, 'Ingredient Origin')
            function = self.find_siblings(text_container, 'Function')
            benefit_claims = self.find_siblings(text_container, 'Benefit Claims')
            labeling_claims = self.find_siblings(text_container, 'Labeling Claims')
            compliance = self.find_siblings(text_container, 'Certifications & Compliance')
            hlb_value = self.find_siblings(text_container, 'HLB Value')
            end_uses = self.find_siblings(text_container, 'End Uses')
            cas_no = self.find_siblings(text_container, 'CAS Number')
            chemical_name = self.find_siblings(text_container, 'Chemical Name')
            synonyms = self.find_siblings(text_container, 'Synonyms')
            chemical_family = self.find_siblings(text_container, 'Chemical Family')
            features = self.find_siblings(text_container, 'Features')
            grade = self.find_siblings(text_container, 'Grade')

            description = text_container.select('p')[-1].text
            logging.info(f'Saving: {brand}')

            self.data.append({
                    'brand': brand,
                    'item': item,
                    'inci_name': inci_name,
                    'ingredient_origin': ingredient_origin,
                    'function': function,
                    'benefit_claims': benefit_claims,
                    'labeling_claims': labeling_claims,
                    'compliance': compliance,
                    'hlb_value': hlb_value,
                    'end_uses': end_uses,
                    'cas_no': cas_no,
                    'chemical_name': chemical_name,
                    'synonyms': synonyms,
                    'chemical_family': chemical_family,
                    'features': features,
                    'grade': grade,
                    'description': description
            })

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

            count += 1

        self.data_processing(self.driver.page_source)

        return self.data

    def multiple_page(self, start: int, end: int) -> List[Dict]:
        """ the method iterates over the range of given page numbers.

        Args:
        start: the page number to start with
        end: the page number to end with

        Returns: None
        """

        for page in range(start, end+1):
            self.single_page(page)

        return self.data

    @staticmethod
    def save_data(data: List[Dict], path: Optional[str] = os.getcwd()) -> None:
        """ save the data to a CSV file at the given path.

        Args:
        data: the data to save.
        path: the path to save the file (the default is os.getcwd(), which saves the file in the current directory)

        Returns: None
        """

        df = pd.DataFrame(data)
        file_location = f'{path}/cosmetics_data.csv'
        df.to_csv(file_location, index=False)
        logging.info(f"------------data is saved at {file_location}------------")


if __name__ == '__main__':

    obj = KnoedeData()
    # print(obj.single_page(1))
    # obj.save_data(obj.single_page(1))
    # print(obj.multiple_page(2, 3))
    # print(obj.save_data(obj.multiple_page(1, 3)))


"""
Few things to note:

1. The very first time we open the website, we need to click on the button Accept All Cookies.
2. Next, we can find all the 36 products on the page using the selector div[data-cy="product-card"]
3. You might notice that in a full window size, the page loads 4 products in a row and as we click on the down-arrow of 1st product to see more details, it also opens for the remaining 3 products on that row. So we just need to click once per row.
4. To implement the logic of clicking only once per row, we used a count variable as you can see in the code above.

reference:
https://stackoverflow.com/questions/76468614/selenium-python-timeoutexception
"""
