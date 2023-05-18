import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=options)


def scrape_yt(url):
    driver.get(url)
    # scroll the page until it ends
    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    while True:
        # Scroll to the bottom of page
        driver.execute_script("window.scrollTo(0, arguments[0]);", last_height)
        # Wait for new videos to show up
        time.sleep(2)
        # Calculate new document height and compare it with last height
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    time.sleep(2)
    videos = driver.find_elements(By.TAG_NAME, 'ytd-video-renderer')
    print(f"total videos: {len(videos)}")

    links_list = []
    for video in videos:
        link = video.find_element(By.TAG_NAME, 'h3').find_element(By.TAG_NAME, 'a').get_attribute('href')
        links_list.append(link)

    return links_list


# ser manual input
search_word = input("Enter the search keyword: ")
url = f"https://www.youtube.com/results?search_query={search_word}"
print(scrape_yt(url))