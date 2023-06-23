"""
Project : 
Author : Ajeet
Date : June 23, 2023
"""

import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = Chrome()
driver.get('https://www.coroners.nsw.gov.au/coronial-findings-search.html?searchtext=death%20in%20custody&searchYear=All')

search_results = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.search-result-content')))
documents = search_results.find_elements(By.CSS_SELECTOR, 'ul.paginationList>li')
print(f"Total documents on the page: {len(documents)}")

doc_url = [doc.find_element(By.CSS_SELECTOR, 'h4.search-font> a').get_attribute('href') for doc in documents]

for i in doc_url:
    print(f"Downloading: {i.split('/')[-1]}")
    driver.get(i)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.download-button')))
    driver.execute_script("document.querySelector('div.download-button>a').click()")
    time.sleep(2)

time.sleep(5)

"""
output:
Total documents on the page: 10
Downloading: Inquest_into_the_death_of_Brandon_Clark._pdf.pdf
Downloading: Inquest_into_the_death_of_CJ.pdf
Downloading: Inquest_into_the_death_of_Azhar_Abdul.pdf
Downloading: Inquest_into_the_death_of_John_Cribb.pdf
Downloading: Inquest_into_the_death_of_Anthony_Gilbert.pdf
Downloading: Findings_-_Inquest_into_the_death_of_Gordon_Copeland_-_18_April_2023.pdf
Downloading: Inquest_into_the_death_of_John_Dodd.pdf
Downloading: Final_-_Findings_Inquest_into_the_death_of_Stanley_Russell_April_2023_14_April.pdf
Downloading: Inquest_into_the_death_of_KT.pdf
Downloading: Inquest_into_the_death_of_LT.pdf
"""
"""
Approach followed:
Wait for the desired web element container holding all the data to get loaded to find/locate it.

search_results = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.search-result-content')))
Find all the individual target data points within the container.

documents = search_results.find_elements(By.CSS_SELECTOR, 'ul.paginationList>li')    
Next, iterate over the web element containing the list of data points to parse, extract the URL, and put them all in the list.

doc_url = [doc.find_element(By.CSS_SELECTOR, 'h4.search-font> a').get_attribute('href') for doc in documents]
Finally, loop over the list of URLs,

get to the page,
wait for the target web element (Download) to be available on the page,
and execute the query to perform a click to download the file.
This is how you can download all the documents on a single page, and the same can be replicated on multiple pages.

reference:
https://stackoverflow.com/questions/76536814/scrape-website-for-pdfs-within-a-number-of-links
"""