import os
import shutil
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

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



login()
goToAddPersonMenu()

driver.switch_to.default_content()
driver.switch_to.frame('mainFrame')
driver.switch_to.frame(1)

lastName = driver.find_element_by_id("lastname")
firstName = driver.find_element_by_id("firstname")
expDate = driver.find_element_by_id("expiration_date")
addNewHotStamp = driver.find_element_by_id("addButton")
hotStampNumber = driver.find_element_by_id("friendlynumber0")
#Select access level
save = driver.find_element_by_name("save")
addAnother = driver.find_element_by_name("addAnother")

print(driver.title)
