import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = Chrome()

url = "https://platform.sustain-cert.com/public-project/2756"
driver.get(url)

files = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div.MuiBox-root.css-16uqhx7')))
print(f"total files: {len(files)}")

container = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.MuiContainer-root.MuiContainer-maxWidthLg.css-got2s4')))
categories = container.find_elements(By.CSS_SELECTOR, 'div>h6')

for category in categories:

    if category.text == "Design Review":
        # -------------------------------------------------------------------------------------------------------------
        design_files = category.find_element(By.XPATH, "parent::*").find_elements(By.CSS_SELECTOR, 'div.MuiBox-root.css-16uqhx7')
        # -------------------------------------------------------------------------------------------------------------
        print(f"total files under Design Review:: {len(design_files)}")

        delay = 5
        for file in design_files:
            file_detail = file.text.split('\n')

            if file_detail[0].endswith('.pdf)'):
                print(f"pdf files under Design Review:")
                print(file_detail[0].replace('(', '').replace(')', ''))
                # click button to download the pdf file
                file.find_element(By.TAG_NAME, 'button').click()
                time.sleep(delay)

            delay += 10


# reference:
# https://pythonexamples.org/python-selenium-get-previous-sibling-element/#:~:text=To%20get%20the%20preceding%20or,parameter%20in%20the%20function%20call.
# https://stackoverflow.com/questions/76369098/download-pdfs-under-a-specific-header-on-webpage-through-selenium-python
"""
output:

total files: 12
total files under Design Review:: 6
pdf files under Design Review:
03 Deviation Request Form-Zengjiang wind power project-20220209-V01.pdf
pdf files under Design Review:
20220901_GS4GG VAL FVR_Yunxiao Wind_clean.pdf
"""

"""
Few things to note:

1. As you are only interested in the pdf files in the Design Review section, so we first locate the element using h6 tag
2. next, we iterate over all h6 tags and pick only the one with the Design Review text.
3. Then, we refer back to the parent element/tag of the filtered h6 tag, find all the files, and store them in a variable design_files.
4. Now, we get all the files under the Design Review and we easily filter out the files which end with .pdf
5. finally, click on the located pdf file to download.

Downloading the files takes a bit of time, so we add incremental delay to wait for the current files to get downloaded before starting the next file download.
"""