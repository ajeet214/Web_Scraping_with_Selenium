"""
Project : 
Author : Ajeet
Date : June 22, 2023
"""
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

driver = Chrome()
url = "https://vahan.parivahan.gov.in/vahan4dashboard/vahan/view/reportview.xhtml"
driver.get(url)
dropdown_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "j_idt31_input")))
dropdown = Select(dropdown_element)
option_names = [option.get_attribute('innerHTML') for option in dropdown.options]
print(len(option_names))
print(option_names)


"""
output:

35
['All Vahan4 Running States (34/36)', 'Andaman &amp; Nicobar Island(8)', 'Andhra Pradesh(80)', 'Arunachal Pradesh(26)', 'Assam(36)', 'Bihar(49)', 'Chhattisgarh(30)', 'Chandigarh(1)', 'UT of DNH and DD(3)', 'Delhi(23)', 'Goa(13)', 'Gujarat(37)', 'Himachal Pradesh(113)', 'Haryana(179)', 'Jharkhand(30)', 'Jammu and Kashmir(21)', 'Karnataka(68)', 'Kerala(87)', 'Ladakh(3)', 'Maharashtra(53)', 'Meghalaya(13)', 'Manipur(12)', 'Madhya Pradesh(52)', 'Mizoram(10)', 'Nagaland(9)', 'Odisha(39)', 'Punjab(93)', 'Puducherry(8)', 'Rajasthan(142)', 'Sikkim(8)', 'Tamil Nadu(146)', 'Tripura(9)', 'Uttarakhand(21)', 'Uttar Pradesh(78)', 'West Bengal(56)']

reference:
https://stackoverflow.com/questions/76528109/how-do-i-obtain-a-list-of-values-from-a-website-dropdown-using-selenium
"""