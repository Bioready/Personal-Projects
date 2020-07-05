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

addresses = []
prices = []
squarefootages = []
bedrooms = []
bathrooms = []
links = []

n_pages = 0


def ScrapeInfo(*args,):
    for page in range(0, 75):
        global n_pages
        n_pages += 1
        response = get(*args, headers=headers)
        page_html = BeautifulSoup(response.text, 'html.parser')
        house_containers = page_html.find_all('div', class_='HomeCardContainer selectedHomeCard')
        if house_containers != []:
            for container in house_containers:

                # Address
                address = container.find_all('div', class_='addressDisplay font-size-smaller')

                # Price
                price = container.find_all('span')[0].text

                # Square Footage
                sqft = container.find_all('div', class_='stats')[2].text

                # Bedrooms
                bedrooms = container.find_all('div', class_='stats')[0]

                # Bathrooms
                baths = container.find_all('div', class_='stats')[1]

                # URL
#                link = 'https://www.redfin.com/' + container.find_all('a').get('href')[1:-6]
#                urls.append(link)
        else:
            break
    print('You scraped {} pages containing {} properties.'.format(n_pages, len(addresses)))


#    sleep(randint(1,2))


ScrapeInfo(Redfin70802)
ScrapeInfo(Redfin70806)
ScrapeInfo(Redfin70808)


# cols = ['Address', 'Price', 'SqFt', 'Bedrooms', 'Bathrooms', 'URL']

# BatonRouge70802 = pd.DataFrame({'Address': addresses,
#                                'Price': prices,
#                                'SqFt': squarefootages,
#                                'Bedrooms': bedrooms,
#                                'Bathrooms': bathrooms,
#                                'URL': links})[cols]

# BatonRouge70802.to_excel('lisboa_raw.xls')
