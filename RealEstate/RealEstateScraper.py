from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import itertools
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

Redfin70802 = 'https://www.redfin.com/zipcode/70802/filter/sort=lo-days,property-type=house,min-price=250k,max-price=450k,min-beds=3,min-baths=2,status=active'
Redfin70806 = 'https://www.redfin.com/zipcode/70806/filter/sort=lo-days,property-type=house,min-price=250k,max-price=450k,min-beds=3,min-baths=2,status=active'
Redfin70808 = 'https://www.redfin.com/zipcode/70808/filter/sort=lo-days,property-type=house,min-price=250k,max-price=450k,min-beds=3,min-baths=2,status=active'

response70802 = get(Redfin70802, headers=headers)
response70806 = get(Redfin70806, headers=headers)
response70808 = get(Redfin70808, headers=headers)

html_soup70802 = BeautifulSoup(response70802.text, 'html.parser')
html_soup70806 = BeautifulSoup(response70806.text, 'html.parser')
html_soup70808 = BeautifulSoup(response70808.text, 'html.parser')


house_containers_70802 = html_soup70802.find_all('div', class_='HomeCardContainer selectedHomeCard')
house_containers_70806 = html_soup70806.find_all('div', class_='HomeCardContainer selectedHomeCard')
house_containers_70808 = html_soup70808.find_all('div', class_='HomeCardContainer selectedHomeCard')


FirstHouse70802 = house_containers_70802[0]
FirstHouse70806 = house_containers_70806[0]
FirstHouse70808 = house_containers_70808[0]

Price70802 = FirstHouse70802.find_all('span')[0].text
Price70806 = FirstHouse70806.find_all('span')[0].text
Price70808 = FirstHouse70808.find_all('span')[0].text

Prices = [Price70802, Price70806, Price70808]

print(Prices)
