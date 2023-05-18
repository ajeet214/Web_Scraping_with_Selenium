import pandas as pd
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

driver = Chrome()

url = 'https://www.hko.gov.hk/en/cis/awsDailyElement.htm?stn=WB8&ele=PREV_DIR&y=2023'
driver.get(url)

table = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'table[id="t1"] > tr')))
columns = [i.text for i in table[0].find_elements(By.TAG_NAME, 'th')]
table_dict = {col: [] for col in columns}

for row in table[1:]:
    for data in zip(columns, [i.text for i in row.find_elements(By.TAG_NAME, 'td')]):
        table_dict[data[0]].append(data[1])

driver.close()

df = pd.DataFrame(table_dict)
# # saving the dataframe to a csv
df.to_csv('data.csv', index=False)

"""
Few things to note:

1. After hitting the URL, we need to wait for the table to get visibly located on the page and thus we find all the table rows tr which includes the first tr as the table's columns.
2. the variable columns is a list that holds the table column names (first row data table[0])
3. Next, we initiate a variable table_dict and assign the columns as the key of this dict with their values as an empty list.
4. after that, we iterate over the remaining rows of the table, couple the list of columns with the row data and iterate over it to assign the data to its column.
5. and finally, create a dataframe with table_dict and save it into a CSV file data.csv.
"""
