import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By

options = ChromeOptions()

options.add_argument("--start-maximized")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options=options)

url = "http://www.hamiltoncountyherald.com/PublicNotices.aspx"


def scrape_data():
    # Create list of labels of data you want to scrape
    labels = ["lbl1", "lbl2", "lbl3", "lbl4", "lbl5", "lbl6", "lbl7", "lbl8", "lbl9", "lbl10", "lbl11"]

    # Empty list to append data values to
    list_of_data = []

    # Create loop to iterate through list and print values of labels
    for items in labels:
        link = driver.find_element("id", items)
        link_label = link.text
        list_of_data.append(link_label)

    # Create list of titles to use as dict keys
    titles = ["Borrower", "Address", "Original Trustee", "Attorney", "Instrumental No.", "Substitute Trustee",
              "Advertised Auction Date", "Date of First Public Notice", "Trust Date", "DR No."]

    # Zip the titles and labels data together into one dict
    zipped_data = dict(zip(titles, list_of_data))

    return zipped_data


driver.get(url)
tables = driver.find_elements(By.TAG_NAME, 'table')[0]
foreclosure_table = tables.find_elements(By.TAG_NAME, 'table')[7]
views = foreclosure_table.find_elements(By.TAG_NAME, 'tr')[1:]

final_data = []
for view in views:
    # Store the current window handle
    win_handle_before = driver.current_window_handle

    # Perform the click operation that opens new window
    view.find_element(By.TAG_NAME, 'a').click()
    time.sleep(2)

    # Switch to new window opened
    for win_handle in driver.window_handles:
        driver.switch_to.window(win_handle)

    # Perform the actions on new window
    final_data.append(scrape_data())

    # Close the new window, if that window no more required
    driver.close()

    # Switch back to original browser (first window)
    driver.switch_to.window(win_handle_before)
    time.sleep(2)

print(final_data)
