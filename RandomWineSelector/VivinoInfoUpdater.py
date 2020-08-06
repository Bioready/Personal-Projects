import requests
from bs4 import BeautifulSoup
import gspread
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

# Pull out list of wines and select only names
googleaccount = gspread.service_account(filename='credentials.json')
googlesheet = googleaccount.open_by_key('1DKWj1mHuLp453tzbcTfWpvEkUfGp_VzgCsmcQl0gBw8')
RedWines = googlesheet.worksheet("Red Wine")
WhiteWines = googlesheet.worksheet("White Wine")
RedsDF = pd.DataFrame(RedWines.get_all_records())
WhitesDF = pd.DataFrame(WhiteWines.get_all_records())
RedNames = RedsDF['Name']
WhiteNames = WhitesDF['Name']

Cartograph = RedsDF['Name'][0]


# Search for wines on Vivino
# browser = webdriver.Chrome(r'C:\Users\Office\Documents\GitHub\Personal-Projects\RandomWineSelector\chromedriver')
# browser.get('https://www.vivino.com')
# SearchBar = browser.find_element_by_xpath('//*[@id="navigation-container"]/div/nav/div[1]/div/div/div/form/input')
# SearchBar.send_keys(Cartograph)

print(RedsDF)
