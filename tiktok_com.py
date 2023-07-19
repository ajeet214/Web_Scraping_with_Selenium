"""
Project : TikTok video's view count
Author : Ajeet
Date : July 19, 2023
"""

import time
import json
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC


def save_view_counts(urls, filename):
    data = {}
    driver = Chrome(service=Service(ChromeDriverManager().install()))

    for url in urls:

        driver.get(url)
        recent_videos = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'strong[data-e2e="video-views"]')))
        print(f"number of recent videos: {len(recent_videos)}")
        data[url] = [i.get_attribute('innerHTML') for i in recent_videos]

        time.sleep(3) # delay between requests

    driver.quit()
    print(data)

    # save data
    with open(filename, 'w') as f:
        f.write(json.dumps(data, indent=4))

# urls 2 scrape
urls = [
    'https://www.tiktok.com/@netflix',
    'https://www.tiktok.com/@twitter'
]

save_view_counts(urls, 'views.txt')


"""
output:

number of recent videos: 34
number of recent videos: 23
{'https://www.tiktok.com/@netflix': ['99.7K', '136.7K', '27.6K', '18.1K', '12.8K', '7670', '87K', '15.8K', '14.5K', '102.1K', '25.7K', '203.2K', '4.1M', '43K', '32.9K', '101.5K', '2.3M', '233K', '440.9K', '92.4K', '25.9K', '53.3K', '33.3K', '449.5K', '92K', '53.2K', '215.5K', '32.1K', '1.6M', '415K', '224K', '319.1K', '469.8K', '420.1K'], 'https://www.tiktok.com/@twitter': ['361.4K', '138.5K', '54.4K', '169.3K', '67.6K', '90.4K', '4.6M', '115.4K', '48.4K', '45.6K', '73K', '223.8K', '107K', '11.8M', '155.7K', '100K', '1.4M', '94.6K', '55.3K', '67.4K', '48K', '40.7K', '40.4K']}

Few things to note:

- we can directly locate/find the element of view-count using the CSS selector strong[data-e2e="video-views"]
- To get the view-count text, use i.get_attribute('innerHTML') instead of i.text

reference:
https://stackoverflow.com/questions/76716861/bulk-scraping-tiktok-view-count-from-20-most-recent-posts
"""