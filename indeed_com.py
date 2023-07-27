"""
Project : Indeed Job Search
Author : Ajeet
Date : July 27 , 2023
"""

# import modules and libraries
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import TimeoutException


class Indeed:
    """
    A web scraper class to extract job data from Indeed job listings.

    Attributes:
        driver (selenium.webdriver.Chrome): Chrome web driver instance for automated browsing.
        wait (selenium.webdriver.support.ui.WebDriverWait): WebDriverWait instance for waiting
         until elements are present.
    """

    def __init__(self):
        """
        Initialize the Indeed class with Chrome driver and WebDriverWait settings.
        """
        options = ChromeOptions()
        options.add_argument("--incognito")

        self.driver = Chrome(service=ChromeService(
            ChromeDriverManager().install()), options=options)
        self.wait = WebDriverWait(self.driver, 10)

    @staticmethod
    def data_extraction(jobs):
        """
         Extract job details from a list of job elements.

         Args:
             jobs (list): A list of web elements representing job listings.

         Returns:
             list: A list of dictionaries containing job details like title,
             company, location, and link.
         """

        data = []
        for job in jobs:

            job_title= job.find_element(By.CSS_SELECTOR, "h2.jobTitle").text
            company_name= job.find_element(By.CSS_SELECTOR, "span.companyName").text
            location= job.find_element(By.CSS_SELECTOR, "div.companyLocation").text
            job_link= job.find_element(By.CSS_SELECTOR, "h2.jobTitle>a").get_attribute("href")


            data.append({
                "job_title": job_title,
                "company_name": company_name,
                "location": location,
                "job_link": job_link
            })
        return data


    def specific_page_job_search(self, query, location, page_no):
        """
         Perform a job search on a specific page and extract job details.

         Args:
             query (str): The job search query.
             location (str): The job location.
             page_no (int): The page number of the search results.

         Returns:
             list: A list of dictionaries containing job details like title,
             company, location, and link.
        """

        self.driver.get(f"https://ca.indeed.com/jobs?q={query}&l={location}&start={(page_no-1)*10}")

        job_containers = self.wait.until(EC.presence_of_all_elements_located((
            By.CSS_SELECTOR, 'div.job_seen_beacon')))
        return  self.data_extraction(job_containers)


    def all_page_job_search(self, query, location):
        """
        Perform a job search on all available pages and extract job details.

        Args:
            query (str): The job search query.
            location (str): The job location.

        Returns:
            list: A list of dictionaries containing job details like title,
            company, location, and link.
        """

        self.driver.get(f"https://ca.indeed.com/jobs?q={query}&l={location}")

        total_job_list = []

        while True:

            job_containers = self.wait.until(EC.presence_of_all_elements_located((
                By.CSS_SELECTOR, 'div.job_seen_beacon')))
            total_job_list += self.data_extraction(job_containers)

            try:
                next_button = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((
                    By.CSS_SELECTOR, 'a[data-testid="pagination-page-next"]')))
                next_button.click()
            except TimeoutException:
                break

            try:
                popup_button = WebDriverWait(self.driver, 2).until(
                    EC.presence_of_element_located((
                        By.CSS_SELECTOR, 'div#mosaic-desktopserpjapopup>div>button[aria-label="close"]')))
                popup_button.click()
            except TimeoutException:
                pass

        return total_job_list



if __name__ == "__main__":
    obj = Indeed()
    print(obj.all_page_job_search(query='data analyst', location='Kitchener-Waterloo, ON'))
