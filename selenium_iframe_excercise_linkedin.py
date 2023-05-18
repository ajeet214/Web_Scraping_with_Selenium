"""
This script prints the total number of pages of document that is being attached to a LinkedIn post.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from linkedIn_base import Linkedin

obj = Linkedin()
driver = obj.load_cookies(path="linkedin_cookies.json")

# for example, this post has a doc with 7 pages
post_url = "https://www.linkedin.com/feed/update/urn:li:activity:7050104978106974208"
driver.get(post_url)

driver.execute_script("window.scrollBy(0,900);")
WebDriverWait(driver, 10).until(
    EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[class='document-s-container__document-element document-s-container__document-element--loaded']")))

element = driver.find_element(By.CSS_SELECTOR, 'div.ssplayer-actions.center-actions')
pages = element.find_element(By.CSS_SELECTOR, 'div.ssplayer-progress-bar.meter-animated').get_attribute('aria-valuemax')
print(pages)

