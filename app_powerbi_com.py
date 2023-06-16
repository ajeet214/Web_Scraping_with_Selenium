"""
Project : App PowerBI
Author : Ajeet
Date : June 16, 2023
"""
# import libraries
import time
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import MoveTargetOutOfBoundsException

options = ChromeOptions()
options.add_argument('--start-maximized')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = Chrome(options=options)
wait = WebDriverWait(driver, 10)
driver.get("https://app.powerbi.com/view?r=eyJrIjoiNzA0MGM4NGMtN2E5Ny00NDU3LWJiNzMtOWFlMGIyMDczZjg2IiwidCI6IjM4MmZiOGIwLTRkYzMtNDEwNy04MGJkLTM1OTViMjQzMmZhZSIsImMiOjZ9&pageName=ReportSection")

# wait for the dashboard to load
wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'transform.bringToFront')))

state = driver.find_element(By.CSS_SELECTOR, 'div[aria-label="State"]')
state.find_element(By.CSS_SELECTOR, 'span[title="Select all"]').click()

job_name = driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Job Name"]')
# for example, select the option 4
job_name.find_element(By.CSS_SELECTOR, 'div[data-row-index="4"]').click()

time.sleep(2)

scrolls = driver.find_elements(By.CSS_SELECTOR, 'div.scroll-bar-part-bar')
h_scroll = scrolls[2]
v_scroll = scrolls[3]

# Perform horizontal scrolling
action_chains = ActionChains(driver)
action_chains.move_to_element(h_scroll).click_and_hold().move_by_offset(500, 0).release().perform()
time.sleep(1)

flag = True
while flag:
    try:
        # Perform vertical scrolling
        action_chains = ActionChains(driver)
        action_chains.move_to_element(v_scroll).click_and_hold().move_by_offset(0, 100).release().perform()

    except MoveTargetOutOfBoundsException:
        flag = False

# find the desired 2nd table
table = driver.find_elements(By.CSS_SELECTOR, 'div.tableExContainer')[1]

# now you can parse this desirable as you want.


"""
Few points to note:

1. We first wait for the dashboard on the webpage to be visible.
2. Next, locate the State web element and find Select all option in it to click.
3. Similarly, locate the Job Name web element and find the option number 4 in it to click.
4. Next, we locate the all vertical and horizontal scroll bars with the css selector and then get the horizontal and 
   vertical scroll bar of the desired table(2nd table here).
5. After getting the web element of the target scroll-bars, we first perform the horizontal scrolling.
6. Afterwards, we perform the vertical scrolling to load all the data in the target table.
7 Finally, locate the target/desired table, the variable "table" holds the desired web element of the table you want to scrape which you can use for further parsing to extract the table's data.

reference:
https://stackoverflow.com/questions/76214166/scrape-websites-power-bi-dashboard-using-python-selenium
"""