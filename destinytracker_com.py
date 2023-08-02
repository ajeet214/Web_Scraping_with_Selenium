"""
Project : destinytracker
Author : Ajeet
Date : August 2, 2023
"""
from time import sleep
from selenium.common import TimeoutException
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


driver = Chrome()
url = "https://destinytracker.com/destiny-2/profile/psn/4611686018440125811/matches?mode=crucible"
driver.get(url)
wait = WebDriverWait(driver, 30)

crucible_content = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "div.trn-gamereport-list.trn-gamereport-list--compact")))
game_reports = crucible_content.find_elements(By.CLASS_NAME, "trn-gamereport-list__group")

for game_report in game_reports:
    group_entry = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "trn-gamereport-list__group-entries")))
    win_match = group_entry.find_elements(By.CSS_SELECTOR, "div.trn-match-row--outcome-win")
    driver.execute_script("arguments[0].scrollIntoView();", win_match[0])
    lose_match = group_entry.find_elements(By.CSS_SELECTOR, "div.trn-match-row--outcome-loss")
    for win_element in win_match:

        try:
            win_left = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.trn-match-row__section--left")))
            driver.execute_script("arguments[0].click();", win_left)
            print("reached here")
            date_time = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='info']")))
            date_time = date_time.text.split(",")[0]
            match_roster = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "match-rosters")))
            team_alpha = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.match-roster.alpha")))
            team_bravo = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.match-roster.bravo")))
            bravo_match_roster_entries = team_bravo.find_element(By.CLASS_NAME, "roster-entries")
            alpha_match_roster_entries = team_alpha.find_element(By.CLASS_NAME, "roster-entries")
            name = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "router-link-active")))
            entry_bravo = bravo_match_roster_entries.find_elements(By.CLASS_NAME, "entry")
            entry_alpha = alpha_match_roster_entries.find_elements(By.CLASS_NAME, "entry")
            print(date_time)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.close"))).click()
            sleep(1)
        except TimeoutException:
            pass

"""
reference:
https://stackoverflow.com/questions/76814861/i-keep-getting-a-timeout-error-for-an-element-even-though-it-prints-out-the-text
"""
