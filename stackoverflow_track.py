import time
import winsound
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

options = ChromeOptions()
# open and maximize the screen
options.add_argument("--start-maximized")
# below 2 lines diables the info bar
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = Chrome(options=options)

url_to_track = 'https://stackoverflow.com/search?tab=Newest&pagesize=15&q=web-scraping&searchOn=3'
driver.get(url_to_track)

questions = driver.find_elements(By.CSS_SELECTOR, 'div.s-post-summary.js-post-summary')

try:
    top_of_list = questions[0].find_element(By.CSS_SELECTOR, 'div.s-post-summary--content')
    title = top_of_list.find_element(By.TAG_NAME, 'h3').text
    print(title)
    top_title = title

    flag = True
    time_now = time.time()
    while flag:
        q = driver.find_elements(By.CSS_SELECTOR, 'div.s-post-summary.js-post-summary')[0]
        ti = q.find_element(By.CSS_SELECTOR, 'div.s-post-summary--content').find_element(By.TAG_NAME, 'h3').text
        # print(ti)
        cat = q.find_element(By.CSS_SELECTOR, 'div.s-post-summary--content').find_element(By.CSS_SELECTOR,
                                                                                          'h3>span').get_attribute(
            'title')
        # print(cat)
        tg = [tag.text for tag in
              q.find_element(By.CSS_SELECTOR, 'div.s-post-summary--content').find_element(By.CSS_SELECTOR,
                                                                                          'div.s-post-summary--meta').find_element(
                  By.CSS_SELECTOR, 'ul.ml0.list-ls-none.js-post-tag-list-wrapper.d-inline').find_elements(By.TAG_NAME,
                                                                                                          'li')]
        # print(tg)

        if ti != top_title and cat =='Question' and 'python' in tg:
            # winsound.Beep(frequency=350, duration=1000)
            print(f"new post arrives")
            winsound.PlaySound('delightful-4.wav', winsound.SND_FILENAME)
            flag = False

        # refresh the browser every 2 minutes
        if time.time() > time_now+120:
            driver.refresh()
            time_now = time.time()

except IndexError as e:
    print(e)
    time.sleep(10)
    driver.quit()




