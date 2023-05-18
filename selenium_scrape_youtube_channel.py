import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# CHROME DRIVER
options = Options()

options.add_argument("--start-maximized")
# options.add_experimental_option("useAutomationExtension", False)
# options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options=options)


def scrape_ytchannel(url):
    driver.get(url)

    handle = driver.find_element(By.XPATH, '//yt-formatted-string[@id="channel-handle"]').text
    subscriber_count = driver.find_element(By.XPATH, '//yt-formatted-string[@id="subscriber-count"]').text

    # SCRIPTINO TO SCROLL PAGE UNTIL IT ENDS
    WAIT_IN_SECONDS = 5
    last_height = driver.execute_script("return document.documentElement.scrollHeight")

    while True:
        # Scroll to the bottom of page
        driver.execute_script("window.scrollTo(0, arguments[0]);", last_height)
        # Wait for new videos to show up
        time.sleep(WAIT_IN_SECONDS)

        # Calculate new document height and compare it with last height
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    thumbnails = driver.find_elements(By.XPATH, '//a[@id="thumbnail"]/yt-image/img')
    views = driver.find_elements(By.XPATH, '//div[@id="metadata-line"]/span[1]')
    titles = driver.find_elements(By.ID, "video-title")
    links = driver.find_elements(By.ID, "video-title-link")

    videos = []
    for title, view, thumb, link in zip(titles, views, thumbnails, links):
        video_dict = {
            'title': title.text,
            'views': view.text,
            # 'thumbnail': thumb.get_attribute('src'),
            'thumbnail': thumb.get_dom_attribute('src'),
            'link': link.get_attribute('href')
        }
        videos.append(video_dict)
    result = [videos, handle, subscriber_count]

    return result


url_conf = "https://www.youtube.com/@confindustria/videos"
print(scrape_ytchannel(url_conf))