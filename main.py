import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import chromedriver_autoinstaller
import csv
import credentials
import sys

chromedriver_autoinstaller.install()
options = Options()
options.headless = True
driver = webdriver.Chrome()
dataFile = ""

def login():
    login = driver.find_element_by_name("username")
    login.clear()
    login.send_keys(credentials.username)
    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys(credentials.password)
    password.send_keys(Keys.RETURN)

def goToAddPersonMenu():
    driver.switch_to.frame("mainFrame")
    driver.switch_to.frame(0)
    driver.find_element_by_xpath('//*[@id="buttonDiv"]/a[3]').click()
    time.sleep(3)
    driver.switch_to.default_content()
    driver.switch_to.frame('mainFrame')
    driver.switch_to.frame(1)
    driver.find_element_by_xpath('//*[@id="menus"]/table/tbody/tr[2]/td[1]/div[2]/ul/li[1]/a').click()
    time.sleep(3)

def addStudentData(row):
    driver.switch_to.default_content()
    driver.switch_to.frame('mainFrame')
    driver.switch_to.frame(1)

    lastName = driver.find_element_by_id("lastname")
    lastName.send_keys(row['lastName'])
    firstName = driver.find_element_by_id("firstname")
    firstName.send_keys(row['firstName'])
    expDate = driver.find_element_by_id("expirationdate_date")
    expDate.send_keys(row['expDate'])

    addNewHotStamp = driver.find_element_by_id("addButton")
    addNewHotStamp.click()
    time.sleep(1)
    hotStampNumber = driver.find_element_by_id("friendlynumber0")
    hotStampNumber.send_keys(row['hotStamp'])
    hotStampNumber.send_keys(Keys.TAB)
    time.sleep(1)

    accesslevel = row['accessLevel']
    if accesslevel.find(','):
        access = accesslevel.split(',')
        for levels in access:
            select = Select(driver.find_element_by_id("accessLevel_available"))
            select.select_by_visible_text(levels)
            addAccessLevel = driver.find_element_by_id("accessLevel_add")
            addAccessLevel.click()
            time.sleep(1)
    else:
        select = Select(driver.find_element_by_id("accessLevel_available"))
        select.select_by_visible_text(accesslevel)
        addAccessLevel = driver.find_element_by_id("accessLevel_add")
    
    save = driver.find_element_by_name("save")
    save.click()
    print("{fName} {lName} has been added".format(fName=row['firstName'], lName=row['lastName']))
    time.sleep(1)
    addAnother = driver.find_element_by_name("addAnother")
    addAnother.click()

def mainLoop():
    for file in os.listdir():
        if ".csv" in file:
            dataFile = file
        else:
            pass

    if ".csv" not in dataFile:
        print(dataFile)
        driver.quit()
        sys.exit("No CSV file found")

    driver.get(credentials.url)
    login()
    goToAddPersonMenu()

    try:
        with open(dataFile) as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                addStudentData(row)
                time.sleep(2)
            print("All Done")
            driver.quit()
    except Exception as e: #this is kinda jank!
        print(e.message)

mainLoop()
