"""
Project : Yomiuri
Author : Ajeet
Date : July 10, 2023
"""

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import time

options = ChromeOptions()
options.add_argument('--start-maximized')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 2})

driver = Chrome(options=options)
wait = WebDriverWait(driver, 10)
driver.get('https://www.yomiuri.co.jp/editorial/')

element = wait.until(EC.presence_of_element_located((By.ID, "ajax_more_button")))

count = len(wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'ul#latest_list>li[class="p-list-item "]'))))
print(f"initial number of articles: {count}")

while True:

    driver.execute_script("return arguments[0].click()", element)
    time.sleep(1)
    new_count = len(driver.find_elements(By.CSS_SELECTOR, 'ul#latest_list>li[class="p-list-item "]'))
    print(f"articles after clicking read/load more button: {new_count}")
    if new_count>count:
        count = new_count
    else:
        break

    if count==100:
        break

news_articles = [i.find_element(By.TAG_NAME, 'a').get_attribute('href') for i in driver.find_elements(By.CSS_SELECTOR, 'ul#latest_list>li[class="p-list-item "]')]

print(news_articles)
print(f"Total articles {len(news_articles)}")

"""
output:
initial number of articles: 20
articles after clicking read/load more button: 30
articles after clicking read/load more button: 40
articles after clicking read/load more button: 50
articles after clicking read/load more button: 60
articles after clicking read/load more button: 70
articles after clicking read/load more button: 80
articles after clicking read/load more button: 90
articles after clicking read/load more button: 100
['https://www.yomiuri.co.jp/editorial/20230707-OYT1T50249/', 'https://www.yomiuri.co.jp/editorial/20230707-OYT1T50246/', 'https://www.yomiuri.co.jp/editorial/20230706-OYT1T50325/', 'https://www.yomiuri.co.jp/editorial/20230706-OYT1T50322/', 'https://www.yomiuri.co.jp/editorial/20230705-OYT1T50244/', 'https://www.yomiuri.co.jp/editorial/20230705-OYT1T50241/', 'https://www.yomiuri.co.jp/editorial/20230704-OYT1T50239/', 'https://www.yomiuri.co.jp/editorial/20230704-OYT1T50236/', 'https://www.yomiuri.co.jp/editorial/20230703-OYT1T50226/', 'https://www.yomiuri.co.jp/editorial/20230703-OYT1T50223/', 'https://www.yomiuri.co.jp/editorial/20230702-OYT1T50218/', 'https://www.yomiuri.co.jp/editorial/20230702-OYT1T50215/', 'https://www.yomiuri.co.jp/editorial/20230701-OYT1T50247/', 'https://www.yomiuri.co.jp/editorial/20230701-OYT1T50244/', 'https://www.yomiuri.co.jp/editorial/20230630-OYT1T50265/', 'https://www.yomiuri.co.jp/editorial/20230630-OYT1T50259/', 'https://www.yomiuri.co.jp/editorial/20230629-OYT1T50195/', 'https://www.yomiuri.co.jp/editorial/20230629-OYT1T50192/', 'https://www.yomiuri.co.jp/editorial/20230628-OYT1T50240/', 'https://www.yomiuri.co.jp/editorial/20230628-OYT1T50237/', 'https://www.yomiuri.co.jp/editorial/20230627-OYT1T50257/', 'https://www.yomiuri.co.jp/editorial/20230627-OYT1T50254/', 'https://www.yomiuri.co.jp/editorial/20230626-OYT1T50297/', 'https://www.yomiuri.co.jp/editorial/20230626-OYT1T50292/', 'https://www.yomiuri.co.jp/editorial/20230625-OYT1T50191/', 'https://www.yomiuri.co.jp/editorial/20230625-OYT1T50188/', 'https://www.yomiuri.co.jp/editorial/20230624-OYT1T50186/', 'https://www.yomiuri.co.jp/editorial/20230624-OYT1T50183/', 'https://www.yomiuri.co.jp/editorial/20230623-OYT1T50305/', 'https://www.yomiuri.co.jp/editorial/20230623-OYT1T50302/', 'https://www.yomiuri.co.jp/editorial/20230623-OYT1T50083/', 'https://www.yomiuri.co.jp/editorial/20230623-OYT1T50070/', 'https://www.yomiuri.co.jp/editorial/20230621-OYT1T50273/', 'https://www.yomiuri.co.jp/editorial/20230621-OYT1T50270/', 'https://www.yomiuri.co.jp/editorial/20230620-OYT1T50203/', 'https://www.yomiuri.co.jp/editorial/20230620-OYT1T50200/', 'https://www.yomiuri.co.jp/editorial/20230619-OYT1T50253/', 'https://www.yomiuri.co.jp/editorial/20230619-OYT1T50250/', 'https://www.yomiuri.co.jp/editorial/20230618-OYT1T50138/', 'https://www.yomiuri.co.jp/editorial/20230618-OYT1T50135/', 'https://www.yomiuri.co.jp/editorial/20230617-OYT1T50290/', 'https://www.yomiuri.co.jp/editorial/20230617-OYT1T50287/', 'https://www.yomiuri.co.jp/editorial/20230616-OYT1T50258/', 'https://www.yomiuri.co.jp/editorial/20230616-OYT1T50254/', 'https://www.yomiuri.co.jp/editorial/20230616-OYT1T50013/', 'https://www.yomiuri.co.jp/editorial/20230616-OYT1T50010/', 'https://www.yomiuri.co.jp/editorial/20230614-OYT1T50286/', 'https://www.yomiuri.co.jp/editorial/20230614-OYT1T50284/', 'https://www.yomiuri.co.jp/editorial/20230613-OYT1T50164/', 'https://www.yomiuri.co.jp/editorial/20230613-OYT1T50161/', 'https://www.yomiuri.co.jp/editorial/20230612-OYT1T50193/', 'https://www.yomiuri.co.jp/editorial/20230612-OYT1T50189/', 'https://www.yomiuri.co.jp/editorial/20230610-OYT1T50273/', 'https://www.yomiuri.co.jp/editorial/20230610-OYT1T50270/', 'https://www.yomiuri.co.jp/editorial/20230609-OYT1T50270/', 'https://www.yomiuri.co.jp/editorial/20230609-OYT1T50267/', 'https://www.yomiuri.co.jp/editorial/20230608-OYT1T50261/', 'https://www.yomiuri.co.jp/editorial/20230608-OYT1T50257/', 'https://www.yomiuri.co.jp/editorial/20230607-OYT1T50239/', 'https://www.yomiuri.co.jp/editorial/20230607-OYT1T50236/', 'https://www.yomiuri.co.jp/editorial/20230606-OYT1T50228/', 'https://www.yomiuri.co.jp/editorial/20230606-OYT1T50225/', 'https://www.yomiuri.co.jp/editorial/20230605-OYT1T50252/', 'https://www.yomiuri.co.jp/editorial/20230605-OYT1T50244/', 'https://www.yomiuri.co.jp/editorial/20230604-OYT1T50144/', 'https://www.yomiuri.co.jp/editorial/20230604-OYT1T50141/', 'https://www.yomiuri.co.jp/editorial/20230603-OYT1T50230/', 'https://www.yomiuri.co.jp/editorial/20230603-OYT1T50227/', 'https://www.yomiuri.co.jp/editorial/20230602-OYT1T50262/', 'https://www.yomiuri.co.jp/editorial/20230602-OYT1T50259/', 'https://www.yomiuri.co.jp/editorial/20230601-OYT1T50232/', 'https://www.yomiuri.co.jp/editorial/20230601-OYT1T50229/', 'https://www.yomiuri.co.jp/editorial/20230531-OYT1T50307/', 'https://www.yomiuri.co.jp/editorial/20230531-OYT1T50304/', 'https://www.yomiuri.co.jp/editorial/20230530-OYT1T50254/', 'https://www.yomiuri.co.jp/editorial/20230530-OYT1T50251/', 'https://www.yomiuri.co.jp/editorial/20230529-OYT1T50201/', 'https://www.yomiuri.co.jp/editorial/20230529-OYT1T50198/', 'https://www.yomiuri.co.jp/editorial/20230528-OYT1T50116/', 'https://www.yomiuri.co.jp/editorial/20230528-OYT1T50113/', 'https://www.yomiuri.co.jp/editorial/20230527-OYT1T50305/', 'https://www.yomiuri.co.jp/editorial/20230527-OYT1T50301/', 'https://www.yomiuri.co.jp/editorial/20230526-OYT1T50307/', 'https://www.yomiuri.co.jp/editorial/20230526-OYT1T50304/', 'https://www.yomiuri.co.jp/editorial/20230525-OYT1T50378/', 'https://www.yomiuri.co.jp/editorial/20230525-OYT1T50371/', 'https://www.yomiuri.co.jp/editorial/20230524-OYT1T50273/', 'https://www.yomiuri.co.jp/editorial/20230524-OYT1T50270/', 'https://www.yomiuri.co.jp/editorial/20230523-OYT1T50272/', 'https://www.yomiuri.co.jp/editorial/20230523-OYT1T50269/', 'https://www.yomiuri.co.jp/editorial/20230522-OYT1T50192/', 'https://www.yomiuri.co.jp/editorial/20230522-OYT1T50189/', 'https://www.yomiuri.co.jp/editorial/20230521-OYT1T50225/', 'https://www.yomiuri.co.jp/editorial/20230520-OYT1T50354/', 'https://www.yomiuri.co.jp/editorial/20230520-OYT1T50351/', 'https://www.yomiuri.co.jp/editorial/20230519-OYT1T50244/', 'https://www.yomiuri.co.jp/editorial/20230518-OYT1T50235/', 'https://www.yomiuri.co.jp/editorial/20230518-OYT1T50232/', 'https://www.yomiuri.co.jp/editorial/20230517-OYT1T50298/', 'https://www.yomiuri.co.jp/editorial/20230517-OYT1T50295/']
Total articles 100

Few things to note:

- as we load the home page, initially it contains 20 articles under the 最新ニュース section.
- on every click on the button さらに読み込む , it loads 10 more articles and so on.
- as you may notice, to click on the desired button, we used driver.execute_script("return arguments[0].click()", element)
- there could be thousands of articles on the page. And if you wish to load more, simply remove the if count==100: statement 
or increase the count number to load a given number of articles. Please notice that as every click loads 10 more articles, 
the value of the variable count will be a multiple of 10 starting from 20. (20, 30, 40, 50,....and so on)

reference:
https://stackoverflow.com/questions/76643641/how-to-click-a-button-with-selenium-on-a-javascript-page
"""