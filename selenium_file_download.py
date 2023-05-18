import time

from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("prefs", {
  "download.default_directory": "C:\\Users\\PC\\OneDrive\\Documents\\",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
})
# specify the title of the study you want to download
study_title = "Pan-cancer single-cell landscape of tumor-infiltrating T cells"
# start the browser and navigate to the PubMed website

browser = Chrome(options=options)
browser.get("https://pubmed.ncbi.nlm.nih.gov/")
# find the search box, enter the study title, and submit the form
search_box = browser.find_element(By.ID, "id_term")
search_box.send_keys(study_title)
search_box.send_keys(Keys.RETURN)
# # find the save button to and click it
save_button = browser.find_element(By.XPATH, "//*[@id='save-results-panel-trigger']")
save_button.click()
# # Select Pubmed from drop down
dropdownlist  = browser.find_element(By.ID, "save-action-format")

dropdownlist.find_element(By.CSS_SELECTOR, 'option[value="pmid"]').click()

download_file = browser.find_element(By.XPATH, "//*[@id='save-action-panel-form']/div[2]/button[1]")
download_file.click()
time.sleep(2)
