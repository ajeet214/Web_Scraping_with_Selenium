"""
Author: Ajeet
Created: 1/19/2025
Description: This script scrapes apartment details from the Voxhall property page using Selenium and BeautifulSoup.
Project: automation
"""
import time
import argparse
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from typing import List, Dict

from logger import logger
from helper import save_file


def configure_webdriver(headless: bool = True) -> webdriver.Chrome:
    """Configures and initializes the Selenium WebDriver."""
    options = Options()
    if headless:
        options.add_argument('--headless')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    return webdriver.Chrome(options=options)


def fetch_page_content(driver: webdriver.Chrome, url: str, selector: str, wait_time: int = 2) -> str:
    """
        Fetches the HTML content of a specific container on a web page.

        This function navigates to the provided URL, waits for the page to load, and retrieves the HTML content
        of the specified container identified by the CSS selector.

        Args:
            driver (webdriver.Chrome): The Selenium WebDriver instance to control the browser.
            url (str): The URL of the page to fetch.
            selector (str): The CSS selector to identify the container element whose content is to be fetched.
            wait_time (int, optional): The time (in seconds) to wait for the page to load before fetching content. Defaults to 2 seconds.

        Returns:
            str: The HTML content of the specified container.
        """
    # Navigate to the provided URL
    driver.get(url)

    # Wait for the page to load fully (with a default wait time)
    time.sleep(wait_time)

    # Find the container element using the provided CSS selector and retrieve its inner HTML
    container = driver.find_element(By.CSS_SELECTOR, selector).get_attribute('innerHTML')

    # Return the HTML content of the container
    return container


def parse_apartments(html_content: str) -> List[Dict[str, str]]:
    """
    Parses apartment data from the provided HTML content.

    This function extracts the apartment details such as the link, price, title, area, and floor from the given
    HTML content of a real estate page. It uses BeautifulSoup to parse the HTML and collects relevant information.

    Args:
        html_content (str): The HTML content of the page to parse.

    Returns:
        List[Dict[str, str]]: A list of dictionaries, each containing the details of an apartment (link, price, title, area, floor).
    """
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Initialize an empty list to store the apartments' details
    apartments = []

    # Find all the apartment containers on the page
    result_container = soup.find_all('div', class_="bg-white relative")

    # Loop through each apartment container to extract the required data
    for result in result_container:
        # Find the anchor tag that leads to the apartment's page
        root = result.find_next('a')

        # Extract area and floor information from the text in the corresponding span
        area_floor = root.select_one('section.flex.flex-col.gap-2>span.th-b1-regular').text.split(' | ')

        # Append the apartment's details as a dictionary to the apartments list
        apartments.append({
            "link": f"https://etalongroup.ru/{root['href']}",
            "price": root.select_one('span.th-h2').text,
            "title": root.select_one('span.th-h4').text,
            "area": area_floor[0],
            "floor": area_floor[1]
        })

    # Return the list of apartments with extracted details
    return apartments


def main():

    parser = argparse.ArgumentParser(
        description='A script scrapes apartment details from the Voxhall property page and write results to an JSON file.'
    )
    parser.add_argument('--file', type=str, help='Path of the file', default=None)
    args = parser.parse_args()

    """Main function to orchestrate the scraping process."""
    url = 'https://etalongroup.ru/msk/object/voxhall/'
    container_selector = '#card-object>div'

    logger.info("Configuring WebDriver...")
    driver = configure_webdriver()

    logger.info("Fetching page content...")
    html_content = fetch_page_content(driver, url, container_selector)

    logger.info("Closing WebDriver...")
    driver.quit()

    logger.info("Parsing apartments data...")
    apartments = parse_apartments(html_content)

    if args.file:
        save_file(args.file, apartments)
    else:
        logger.info("Scraped Data:")
        logger.info(apartments)


if __name__ == '__main__':
    main()
