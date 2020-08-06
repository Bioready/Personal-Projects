# coding:utf-8
from selenium import webdriver
import time
import urllib.request
import shutil

# Open Browser to Cacti
browser = webdriver.Chrome(r'C:\Users\Office\Documents\GitHub\Personal-Projects\LASERSWeeklyBandwidth\chromedriver')
browser.get('http://monit.eatel.net')

# Find username box and password boxes
usernamebox = browser.find_elements_by_xpath('//*[@id="user_row"]/td[2]/input')[0]
passwordbox = browser.find_elements_by_xpath('//*[@id="password_row"]/td[2]/input')[0]

# Input username and password
usernamebox.send_keys('ljd2371')
passwordbox.send_keys('B4mb00zle!26')

# Click Login
LoginButton = browser.find_elements_by_xpath('//*[@id="login"]/tbody/tr[9]/td/input')[0]
LoginButton.click()

# Download Graph Image
file_name = 'LASERSWeeklyReport.png'
WeeklyGraph = 'http://monit.eatel.net/graph_image.php?action=view&local_graph_id=20858&rra_id=2'
response = urllib.request.urlopen(WeeklyGraph)
with urllib.request.urlopen(WeeklyGraph) as response, open(file_name, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

time.sleep(2)
browser.close()
