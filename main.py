import os
import shutil
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import csv

options = Options()
options.headless = True
driver = webdriver.Chrome('./chromedriver')
url = "http://192.168.161.240/login/"
driver.get(url)

def login():
    login = driver.find_element_by_name("username")
    login.clear()
    login.send_keys("asanchez")
    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("bndgh56p")
    password.send_keys(Keys.RETURN)

def goToAddPersonMenu():
    driver.switch_to.frame("mainFrame")
    driver.switch_to.frame(0)
    adminMenu = driver.find_element_by_xpath('//*[@id="buttonDiv"]/a[3]').click()
    time.sleep(3)
    driver.switch_to.default_content()
    driver.switch_to.frame('mainFrame')
    driver.switch_to.frame(1)
    addPeopleMenu = driver.find_element_by_xpath('//*[@id="menus"]/table/tbody/tr[2]/td[1]/div[2]/ul/li[1]/a').click()
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
    time.sleep(2)
    hotStampNumber = driver.find_element_by_id("friendlynumber0")
    hotStampNumber.send_keys(row['hotStamp'])
    hotStampNumber.send_keys(Keys.TAB)

    accessLevel = "Miami Student"
    select = Select(driver.find_element_by_id("accessLevel_available"))
    select.select_by_visible_text(accessLevel)
    addAccessLevel = driver.find_element_by_id("accessLevel_add")
    addAccessLevel.click()
    time.sleep(2)

    save = driver.find_element_by_name("save")
    save.click()
    print(row['firstName'] + " " + row['lastName'] + " " + "added.")
    time.sleep(2)
    addAnother = driver.find_element_by_name("addAnother")
    addAnother.click()

def mainLoop():
    with open('importData.csv') as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            addStudentData(row)
            time.sleep(5)
        print("All Done")
        driver.quit()

login()
goToAddPersonMenu()
mainLoop()
