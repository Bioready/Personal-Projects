from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Gather Historical Data
CovidTrackingwebsite = 'https://covidtracking.com/data/state/louisiana#historical'
websitehtml = requests.get(CovidTrackingwebsite)
soup = BeautifulSoup(websitehtml.content, 'html.parser')
historicaltable = soup.find_all(class_='table-module--table--1HfxU')[1]
tablecolumns = historicaltable.find_all('span')[0:8]

DateColumn = pd.read_html(str(historicaltable))[1]

print(DateColumn)
