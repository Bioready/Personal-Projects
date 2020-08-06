from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://c19study.com/'
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

table1 = soup.find(class_='rtable')
Dates = table1.find_all(class_='rotate2')
Results = table1.find_all(class_='desktop')

line = []
for tr in table1:
    dates = table1.find_all(class_='rotate2')
    row = [table1.text for tr in dates]
    line.append(row)
df = pd.DataFrame(line, columns=["Dates"])

print(df)
