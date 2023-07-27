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
                # Look for the "Next" button to navigate to the next page of job listings
                next_button = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((
                    By.CSS_SELECTOR, 'a[data-testid="pagination-page-next"]')))
                next_button.click()
            except TimeoutException:
                # If the "Next" button is not found, it means there are no more pages, so break the loop
                break

            try:
                # Check if a popup appears and close it (if present)
                popup_button = WebDriverWait(self.driver, 2).until(
                    EC.presence_of_element_located((
                        By.CSS_SELECTOR, 'div#mosaic-desktopserpjapopup>div>button[aria-label="close"]')))
                popup_button.click()
            except TimeoutException:
                # If no popup is found, continue without any action
                pass

        return total_job_list



if __name__ == "__main__":
    obj = Indeed()
    print(obj.all_page_job_search(query='data analyst', location='Kitchener-Waterloo, ON'))


"""
output:

[{'job_title': 'Analyst (Data Analytics and Reporting Team)', 'company_name': 'University of Waterloo', 'location': 'Waterloo, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=6a54004a21e70c6e&fccid=5bcffa6277080afe&vjs=3'}, {'job_title': 'Data Analyst', 'company_name': 'University of Waterloo', 'location': 'Waterloo, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=fcf1281ca2ad0bae&fccid=5bcffa6277080afe&vjs=3'}, {'job_title': 'Data Analyst', 'company_name': 'MAXON Computer', 'location': 'Waterloo, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=9db552e2dbdb7caa&fccid=b6a6198234d75b79&vjs=3'}, {'job_title': 'Bank Digital Insights Analyst', 'company_name': 'Manulife', 'location': 'Waterloo, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=395618acf63c34d1&fccid=1747adf6142beb48&vjs=3'}, {'job_title': 'analyst, database', 'company_name': 'Aarorn Technologies Inc.', 'location': 'Guelph, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=44488c921c711c73&fccid=928eebc726e33a2e&vjs=3'}, {'job_title': 'Health Promotion & Research Analyst (Public Health)', 'company_name': 'Region of Waterloo', 'location': 'Waterloo, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=8513d6c9ab34a216&fccid=cb43ce2ddf90903e&vjs=3'}, {'job_title': 'Enterprise Data Governance Analyst', 'company_name': 'D2L', 'location': 'Kitchener, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=887668286c9e6133&fccid=7c3a25cdc8e47610&vjs=3'}, {'job_title': 'Business Intelligence Analyst', 'company_name': 'Manulife', 'location': 'Waterloo, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=be0a827fd84b0835&fccid=1747adf6142beb48&vjs=3'}, {'job_title': 'Business Systems Analyst', 'company_name': 'University of Waterloo', 'location': 'Waterloo, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=17cd3cdcfc2a2dff&fccid=5bcffa6277080afe&vjs=3'}, {'job_title': 'HR Workday Business Analyst', 'company_name': 'University of Waterloo', 'location': 'Waterloo, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=0ea862aed09333e0&fccid=5bcffa6277080afe&vjs=3'}, {'job_title': 'Cloud Infrastructure Analyst', 'company_name': 'Sun Life', 'location': 'Waterloo, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=3205ecb5680b2d91&fccid=618943d89d0005a6&vjs=3'}, {'job_title': 'Programmer/Analyst, Data Services', 'company_name': 'Sleeman Breweries', 'location': 'Guelph, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=99d84bb40952b79b&fccid=2fef090306160696&vjs=3'}, {'job_title': 'Junior Analyst, Sustainable Investing', 'company_name': 'Addenda Capital', 'location': 'Guelph, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=47058318a0ce8f09&fccid=e0bbddd21984445e&vjs=3'}, {'job_title': 'Manager, Data Analytics and Business Intelligence', 'company_name': 'University of Waterloo', 'location': 'Waterloo, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=cfcbcb0bf5d97c24&fccid=5bcffa6277080afe&vjs=3'}, {'job_title': 'Business Analyst, Health Information System', 'company_name': 'Grand River Hospital', 'location': 'Kitchener, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=22eb1849f9bd95ea&fccid=a463ca7249c5270f&vjs=3'}, {'job_title': 'Program Analyst (Client Services & Waterloo Region Housing)', 'company_name': 'Region of Waterloo', 'location': 'Waterloo, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=2af8de2ad6c17e29&fccid=cb43ce2ddf90903e&vjs=3'}, {'job_title': 'Corporate Energy Analyst', 'company_name': 'Region of Waterloo', 'location': 'Kitchener, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=04027a65abd77755&fccid=cb43ce2ddf90903e&vjs=3'}, {'job_title': 'Sr. Investigation Analyst - Drug', 'company_name': 'Manulife', 'location': 'Waterloo, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=631779f713e6fcb5&fccid=1747adf6142beb48&vjs=3'}, {'job_title': 'Sr. Business Systems Analyst', 'company_name': 'Open Text Corporation', 'location': 'Waterloo, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=01e7f04fe1610b1a&fccid=c908408e676247d6&vjs=3'}, {'job_title': 'SCADA & Information System Analyst (Water)', 'company_name': 'Region of Waterloo', 'location': 'Waterloo, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=bcd6c3ed5096d263&fccid=cb43ce2ddf90903e&vjs=3'}, {'job_title': 'Lead Service Management Analyst(Problem\\Change Management)', 'company_name': 'Open Text Corporation', 'location': 'Waterloo, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=256031aef7db1c82&fccid=c908408e676247d6&vjs=3'}, {'job_title': 'Operations, Risk and Controls, Senior Analyst', 'company_name': 'Manulife', 'location': 'Waterloo, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=fff23605a7bdffd2&fccid=1747adf6142beb48&vjs=3'}, {'job_title': 'Sr. Business Systems Analyst', 'company_name': 'opentext', 'location': 'Waterloo, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=356ff992ffedbde5&fccid=c908408e676247d6&vjs=3'}, {'job_title': 'Lead Service Management Analyst(Major Incident Management)', 'company_name': 'Open Text Corporation', 'location': 'Waterloo, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=8563d5fde3de9edb&fccid=c908408e676247d6&vjs=3'}, {'job_title': 'Lead Service Management Analyst(Problem\\Change Management)', 'company_name': 'opentext', 'location': 'Waterloo, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=289172ee3cfc0e79&fccid=c908408e676247d6&vjs=3'}, {'job_title': 'Lead Service Management Analyst(Major Incident Management)', 'company_name': 'opentext', 'location': 'Waterloo, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=a2818036ce7c7628&fccid=c908408e676247d6&vjs=3'}, {'job_title': 'Senior Actuarial Analyst (Pricing), Personal Insurance', 'company_name': 'Definity Financial Corporation', 'location': 'Hybrid remote in Waterloo, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=15fe3dcfd34367a0&fccid=236ef8b5fc73dcdc&vjs=3'}, {'job_title': 'Business Data Analyst', 'company_name': 'RideCo', 'location': 'Hybrid remote in Waterloo, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=5d822d7df36dd954&fccid=e04c335ad3aed20a&vjs=3'}, {'job_title': 'Business Analyst', 'company_name': 'Reliance Home Comfort', 'location': 'Cambridge, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=6b69a47a70672a97&fccid=9aa40cd2accb7367&vjs=3'}, {'job_title': 'Senior Actuarial Analyst - Commercial Pricing', 'company_name': 'Definity Financial Corporation', 'location': 'Hybrid remote in Waterloo, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=bdfb27d7adfac60d&fccid=236ef8b5fc73dcdc&vjs=3'}, {'job_title': 'Business System Analyst', 'company_name': 'Heartland Farm Mutual Inc.', 'location': 'Remote in Waterloo, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=0a21fd408319d7a1&fccid=a45ec34697774b3f&vjs=3'}, {'job_title': 'Operations Business Analyst', 'company_name': 'AirBoss of America Corp.', 'location': 'Kitchener, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=af1c878d42141f98&fccid=293718897fd9eee7&vjs=3'}, {'job_title': 'Reports Analyst- Chengyeng', 'company_name': 'Majorel', 'location': 'Waterloo, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=5e169c6cb94d1183&fccid=afe85deef9b97f13&vjs=3'}, {'job_title': 'Data and BI Analyst', 'company_name': 'Challenger Motor Freight Inc.', 'location': 'Cambridge, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=1403a87b1f8d8fb8&fccid=ba5d3347df98493d&vjs=3'}, {'job_title': 'Senior Business Intelligence Analyst', 'company_name': 'System1', 'location': 'Hybrid remote in Guelph, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=83f15fc1e72f8aa4&fccid=0471f3a5f9f7f44f&vjs=3'}, {'job_title': 'Reports Analyst - Chengyeng - Onsite', 'company_name': 'Majorel', 'location': 'Waterloo, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=790c92cdf4c076f7&fccid=afe85deef9b97f13&vjs=3'}, {'job_title': 'Senior Technical Data Analyst', 'company_name': 'System1', 'location': 'Hybrid remote in Guelph, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=59a4342a8bc1dfe9&fccid=0471f3a5f9f7f44f&vjs=3'}, {'job_title': 'Lead Technical Data Analyst', 'company_name': 'System1', 'location': 'Hybrid remote in Guelph, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=47e8e0ff0457c3f7&fccid=0471f3a5f9f7f44f&vjs=3'}, {'job_title': 'Business Systems Analyst, Senior - Corporate', 'company_name': 'Equitable Life of Canada', 'location': 'Hybrid remote in Waterloo, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=edbca5b2d89a299e&fccid=ac28bc2d58529cfc&vjs=3'}, {'job_title': 'Actuarial Analyst', 'company_name': 'Heartland Farm Mutual Inc.', 'location': 'Waterloo, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=4b5f46f0b27a4587&fccid=a45ec34697774b3f&vjs=3'}, {'job_title': 'Logistics Analyst', 'company_name': 'Glen Dimplex Americas', 'location': 'Cambridge, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=197ca8ea5cebc71a&fccid=45d24101b4e14332&vjs=3'}, {'job_title': 'IT Governance, Risk and Compliance Analyst', 'company_name': 'Equitable Life of Canada', 'location': 'Hybrid remote in Waterloo, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=31cb7ea4604202d4&fccid=ac28bc2d58529cfc&vjs=3'}, {'job_title': 'Board Certified Behaviour Analyst (BCBA)', 'company_name': 'Barrantes & Associates Inc.', 'location': 'Guelph, ON', 'job_link': 'https://ca.indeed.com/company/Barrantes-&-Associates-Inc./jobs/Board-Certified-Behavior-Analyst-ff8add7ef1724226?fccid=1daa18b4ed89f871&vjs=3'}, {'job_title': 'Senior Compliance Analyst - Market Conduct Audit', 'company_name': 'Equitable Life of Canada', 'location': 'Hybrid remote in Waterloo, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=b3d6d719b9778538&fccid=ac28bc2d58529cfc&vjs=3'}, {'job_title': 'Technical Support Analyst, Supply Chain', 'company_name': 'Restaurant Brands International', 'location': 'Guelph, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=7c1ca9747c183fdb&fccid=1bf77f1dd2c2631f&vjs=3'}, {'job_title': 'Business Analyst, Enterprise Project Mgmt Office (Contract)', 'company_name': 'Gowling WLG', 'location': 'Waterloo, ON', 'job_link': 'https://ca.indeed.com/rc/clk?jk=8df7b7ed8ef56ef2&fccid=efc2213aea431503&vjs=3'}]

"""