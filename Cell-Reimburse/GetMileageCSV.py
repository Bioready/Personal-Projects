from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

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

# Click on reporting periods
ReportingPeriod = browser.find_elements_by_xpath('//*[@id="dateRangePicker"]/div')[0]
ReportingPeriod.click()
shortwait

# Click on "Last month"
LastMonthButton = browser.find_elements_by_xpath('/html/body/div[4]/div/div/div/div[3]/div/div/div[1]/div[1]/a[2]')[0]
LastMonthButton.click()
shortwait

# Click on "Create this report"
CreateReport = browser.find_elements_by_xpath('//*[@id="content"]/div/main/div/div[1]/div/div/div/div[4]/button')[0]
CreateReport.click()
shortwait

# Fill Report name
ReportNameBox = browser.find_elements_by_xpath('//*[@id="input-reportName"]')[0]
ReportNameBox.sendkeys('')
