"""
Project : 
Author : Ajeet
Date : July 26, 2023
"""


import time
import threading
import pandas as pd
from math import nan
from datetime import datetime, timedelta
from multiprocessing.pool import ThreadPool
from bs4 import BeautifulSoup as bs
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

class Driver:
    def __init__(self):
        options = webdriver.ChromeOptions()
        self.driver = uc.Chrome(options=options)

    def __del__(self):
        self.driver.quit()  # clean up driver when we are cleaned up


threadLocal = threading.local()


def create_driver():
    the_driver = getattr(threadLocal, 'the_driver', None)
    if the_driver is None:
        the_driver = Driver()
        setattr(threadLocal, 'the_driver', the_driver)
    return the_driver.driver


class GameData:
    def __init__(self):
        self.date = []
        self.time = []
        self.game = []
        self.score = []
        self.home_odds = []
        self.draw_odds = []
        self.away_odds = []
        self.country = []
        self.league = []


def generate_matches(pgSoup, defaultVal=None):
    evtSel = {
        'time': 'div>div>div[class="flex basis-[10%]"]',
        'game': 'a div:has(>a[title])',
        'score': 'a[title]~div:not(.hidden)',
        'home_odds': 'div[class^="flex-center flex-col gap-1 border-l border-black-ma"]:nth-child(2)',
        'draw_odds': 'div[class^="flex-center flex-col gap-1 border-l border-black-ma"]:nth-child(3)',
        'away_odds': 'div[class^="flex-center flex-col gap-1 border-l border-black-ma"]:nth-child(4)'
    }

    events, current_group = [], {}
    pgDate = pgSoup.select_one('h1.title[id="next-matches-h1"]')
    if pgDate: pgDate = pgDate.get_text().split(',', 1)[-1].strip()
    for evt in pgSoup.select('div[set]>div:last-child'):
        if evt.parent.select(f':scope>div:first-child+div+div'):
            cgVals = [v.get_text(' ').strip() if v else defaultVal for v in [
                evt.parent.select_one(s) for s in
                [':scope>div:first-child+div>div:first-child',
                 ':scope>div:first-child>a:nth-of-type(2):nth-last-of-type(2)',
                 ':scope>div:first-child>a:nth-of-type(3):last-of-type']]]
            current_group = dict(zip(['date', 'country', 'league'], cgVals))
            if pgDate: current_group['date'] = pgDate

        evtRow = {'date': current_group.get('date', defaultVal)}

        for k, v in evtSel.items():
            v = evt.select_one(v).get_text(' ') if evt.select_one(v) else defaultVal
            evtRow[k] = ' '.join(v.split()) if isinstance(v, str) else v
        # evtTeams = evt.select('a div>a[title]')
        evtTeams = evt.select('div[class^="relative w-full flex-col"]>a')
        evtRow['game'] = ' – '.join(a['title'] for a in evtTeams)
        evtRow['country'] = current_group.get('country', defaultVal)
        evtRow['league'] = current_group.get('league', defaultVal)

        events.append(evtRow)
    return events


def parse_data(url, return_urls=False):
    print(f'Parsing URL: {url}\n')
    browser = create_driver()
    browser.get(url)
    WebDriverWait(browser, 20).until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "div[set]>div:last-child")))
    # ########## For page to scroll to the end ###########
    scroll_pause_time = 2

    # Get scroll height
    last_height = browser.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(scroll_pause_time)

        # Calculate new scroll height and compare with last scroll height
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    # ########## For page to scroll to the end ###########
    time.sleep(5)
    soup = bs(browser.page_source, "lxml")

    game_data = GameData()
    game_keys = [a for a, av in game_data.__dict__.items() if isinstance(av, list)]
    for row in generate_matches(soup, defaultVal=nan):
        for k in game_keys: getattr(game_data, k).append(row.get(k, nan))
    if return_urls:
        ac_sel = 'div:has(>a.active-item-calendar)'  # a_cont selector
        a_sel = f'{ac_sel}>a[href]:not([href^="#"]):not(.active-item-calendar)'
        a_tags = soup.select(a_sel)

        if a_tags:
            urls = ['https://www.oddsportal.com' + a_tag['href'] for a_tag in a_tags]
            print(f'urls after initial creation: {urls}')

            # Extract the date from the first URL
            last_date_str = urls[0].split('/')[-2]
            print(f'last date str: {last_date_str}')
            last_date = datetime.strptime(last_date_str, '%Y%m%d')

            # Generate the additional URLs
            for i in range(1, 4):
                new_date = last_date - timedelta(days=i)
                new_date_str = new_date.strftime('%Y%m%d')
                new_url = f'https://www.oddsportal.com/matches/football/{new_date_str}/'
                urls.append(new_url)
                print(f'urls after generating additional URL #{i}: {urls}')
        else:
            urls = []

        print(f'final urls: {urls}')

        if urls and urls[-1].startswith('https://www.oddsportal.com/matches/football/'):
            # Extract the date from the last URL
            last_date_str = urls[0].split('/')[-2]
            print(last_date_str)
        else:
            print('No valid URLs found')
        return game_data, urls
    return game_data


if __name__ == '__main__':
    games = None
    pool = ThreadPool(5)
    # Get today's data and the Urls for the other days:
    url_today = 'https://www.oddsportal.com/matches/soccer'
    game_data_today, urls = pool.apply(parse_data, args=(url_today, True))
    game_data_results = pool.imap(parse_data, urls)

    # ########################### BUILD  DATAFRAME ############################
    game_data_dfList, added_todayGame = [], False
    for game_data in game_data_results:
        try:
            game_data_dfList.append(pd.DataFrame(game_data.__dict__))
            if not added_todayGame:
                game_data_dfList += [pd.DataFrame(game_data_today.__dict__)]
                added_todayGame = True
        except Exception as e:
            game_n = len(game_data_dfList) + 1
            print(f'Error tabulating game_data_df#{game_n}:\n{repr(e)}')
    try:
        games = pd.concat(game_data_dfList, ignore_index=True)
    except Exception as e:
        print('Error concatenating DataFrames:', repr(e))
    # #########################################################################
    print('!?NO GAMES?!' if games is None else games)
    # ensure all the drivers are "quitted":
    del threadLocal  # a little extra insurance
    import gc

    gc.collect()

    games.to_csv()