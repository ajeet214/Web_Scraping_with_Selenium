from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


url = 'https://cricos.education.gov.au/Course/CourseSearch.aspx'

options = ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])

browser = Chrome(options=options)
browser.get(url)

state = browser.find_element(By.ID, 'ctl00_cphDefaultPage_courseSearchCriteria_ddlCourseLocation')
nsw = Select(state)
nsw.select_by_value('NSW')
browser.find_element(By.ID, 'ctl00_cphDefaultPage_btnSearch').click()
