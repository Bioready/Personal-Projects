#coding:utf-8
import sys
import os
from selenium import webdriver
import time

# Open Browser to Cacti
browser = webdriver.Chrome(r'C:\Users\Office\Documents\GitHub\Personal-Projects\ClarionInnReport\chromedriver')
browser.get('http://monit.eatel.net')

# Find username box and password boxes
usernamebox = browser.find_elements_by_xpath('//*[@id="user_row"]/td[2]/input')[0]
passwordbox = browser.find_elements_by_xpath('//*[@id="password_row"]/td[2]/input')[0]

# Input username and password
usernamebox.send_keys('USERNAME')
passwordbox.send_keys('PASSWORD')

# Click Login
LoginButton = browser.find_elements_by_xpath('//*[@id="login"]/tbody/tr[9]/td/input')[0]
LoginButton.click()

# Click 'Graphs'
graphs = browser.find_elements_by_xpath('//*[@id="tabs"]/a[2]/img')[0]
graphs.click()

# Click 'CE Devices' Dropdown
CeDevicesDropdown = browser.find_elements_by_xpath('//*[@id="nodeIcon17"]')[0]
CeDevicesDropdown.click()

# Click 'EATEL' Dropdown
EatelDropdown = browser.find_elements_by_xpath('//*[@id="nodeIcon18"]')[0]
EatelDropdown.click()

# Click 'PHIL-ASR920-CE2'
PHILASR920CE2 = browser.find_elements_by_xpath('//*[@id="itemTextLink45"]')[0]
PHILASR920CE2.click()

# Click Clarion Inn Graph
ClarionInnGraph = browser.find_elements_by_xpath('//*[@id="graph_20819"]')[0]
ClarionInnGraph.click()

# Click 'Export to CSV on Monthly Graph'
MonthlyGraph = browser.find_elements_by_xpath('//*[@id="main"]/table/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/a[2]/img')[0]
MonthlyGraph.click()

time.sleep(2)

browser.close()
