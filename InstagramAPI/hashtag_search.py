"""
Project : 
Author : Ajeet
Date : June 20, 2023
"""
import time
from typing import List, Dict
from selenium.webdriver.common.by import By
from InstagramAPI.instagram_baseline import Instagram
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC


def hashtag(browser, tag: str) -> List[Dict]:
    data = []
    url = f'https://www.instagram.com/explore/tags/{tag}/'
    browser.get(url)
    container = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'article')))

    for _ in range(3):
        browser.execute_script('window.scrollBy(0, 5000);')
        time.sleep(1)

    images = container.find_elements(By.TAG_NAME, 'img')
    for image in images:
        data.append({
            "description": image.get_attribute('alt'),
            "image_link": image.get_attribute('src')
        })

    return data


if __name__ == '__main__':
    obj = Instagram()
    driver = obj.load_cookies("D:\\automation\InstagramAPI\instgram_cookies.json")
    print(hashtag(driver, 'tree'))
