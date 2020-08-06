from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import datetime
import time
from bs4 import BeautifulSoup
import requests

# Open Browser to AT&T
browser = webdriver.Chrome(r'C:\Users\Office\Documents\GitHub\Personal-Projects\Cell-Reimburse\chromedriver')
browser.get('https://dashboard.mileiq.com/login')

# Define wait periods
shortwait = browser.implicitly_wait(1)
wait = browser.implicitly_wait(5)

# Input username
usernamebox = browser.find_element_by_xpath('//*[@id="username"]')
usernamebox.send_keys('ljd2371@eatel.com')
shortwait

# Click Next
NextBox = browser.find_element_by_xpath('//*[@id="submit-form"]')
NextBox.click()

# Wait for redirect
wait

# Enter Password
passwordbox = browser.find_elements_by_xpath('//*[@id="i0118"]')[0]
passwordbox.send_keys('B4mb00zle!25')
shortwait

# Click Sign In
LoginButton = browser.find_elements_by_xpath('//*[@id="idSIButton9"]')[0]
LoginButton.click()
shortwait

# Click 'No'
NoButton = browser.find_elements_by_xpath('//*[@id="idBtn_Back"]')[0]
NoButton.click()
shortwait

# Click 'Reports'
ReportsButton = browser.find_elements_by_xpath('//*[@id="navTabs"]/div[2]/a')[0]
ReportsButton.click()
shortwait

# Click on "All Drives"
DrivesDropdown = browser.find_elements_by_xpath('//*[@id="content"]/div/main/div/div[1]/div/section/div/div[2]/span[2]')[0]
DrivesDropdown.click()
shortwait

# Click on "Business Drives"
BusinessDrives = browser.find_elements_by_xpath('//*[@id="2"]/div')[0]
BusinessDrives.click()
shortwait

# Click on reporting periods
ReportingPeriod = browser.find_elements_by_xpath('//*[@id="dateRangePicker"]/div')[0]
ReportingPeriod.click()
shortwait

# Click on "Last month"
LastMonthButton = browser.find_elements_by_xpath('/html/body/div[4]/div/div/div/div[3]/div/div/div[1]/div[1]/a[2]')[0]
LastMonthButton.click()
wait

# Click on "Create this report"
CreateReport = browser.find_element_by_css_selector('#content > div > main > div > div._1w2eFPmK._1J1xySVO > div > div > div > div._1GeMr3qC > button').click()
# CreateReport.click()

# URL = 'https://dashboard.mileiq.com/reports'
# page = requests.get(URL)
# soup = BeautifulSoup(page.content, 'html.parser')
# button = soup.find(id='content')
# print(button)

# Fill Report name
# ReportNameBox = browser.find_elements_by_xpath('//*[@id="input-reportName"]')[0]
# today = datetime.date.today()
# first = today.replace(day=1)
# lastMonth = first - datetime.timedelta(days=1)
# LastMonth = lastMonth.strftime("%Y%m")
# ReportNameBox.sendkeys(LastMonth, 'Mileage Report')
