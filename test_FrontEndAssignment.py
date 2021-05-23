import requests
from selenium import webdriver
import time
import pytest
import re
import pandas as pd
driver = None

@pytest.fixture
def SetupBrowser():
    CHROMEDRIVER_PATH = r'C:\Users\Rashid mohammad\Documents\PYTHON DEVELOPMENT\chromedriver_win32\chromedriver.exe'
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    global driver
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,options=options)
    driver.maximize_window()
    yield
    driver.quit()

#TODO a) Assert Broken images http://the-internet.herokuapp.com/broken_images
def test_brokenImages(SetupBrowser):
    url = "http://the-internet.herokuapp.com/broken_images"
    flag = False
    driver.get(url)
    all_images = driver.find_elements_by_css_selector('Img')
    for image in all_images:
        img_url = image.get_attribute('src')
        responce = requests.get(img_url)
        if responce.status_code != 200:
            print(f"Broken Image found, Unable to load image from {img_url}")
            flag=True
    assert False==flag, "Broken Image found"

#TODO b) Assert forgot password success message on the page http://the-internet.herokuapp.com/forgot_password
# forgot password Functionality is not available in provided link. (Problem statement is NOT correctly stated)


#TODO c) Assert form validation functionality Post entering a dummy username and password on http://the-internet.herokuapp.com/login
def test_form_validation(SetupBrowser):
    url = "http://the-internet.herokuapp.com/login"
    driver.get(url)
    usernameInput = driver.find_element_by_id('username')
    passwordInout = driver.find_element_by_id('password')
    usernameInput.send_keys('tomsmith')
    passwordInout.send_keys('SuperSecretPassword!')
    driver.find_element_by_tag_name('button').click()
    expected_URL_afterLogin= "http://the-internet.herokuapp.com/secure"
    actualUrl = driver.current_url
    assert expected_URL_afterLogin == actualUrl, "Login Failed!"

#TODO d) Write a test to enter alphabets on this and mark it as a failure if we cannot enter on page http://the-internet.herokuapp.com/inputs
def test_enter_alphabets(SetupBrowser):
    url = "http://the-internet.herokuapp.com/inputs"
    driver.get(url)
    inputBox = driver.find_element_by_tag_name('input')
    inputBox.send_keys('abc')
    receivedText = inputBox.get_attribute('value')
    assert receivedText == 'abc', "Unable to enter Albhabets"

#TODO e) Write a test to sort the table by the amount due on page http://the-internet.herokuapp.com/tables
def test_SortTable(SetupBrowser):
    url = "http://the-internet.herokuapp.com/tables"
    driver.get(url)
    xpath_DueHeadingTable1 = '//*[@id="table1"]/thead/tr/th[4]'
    xpath_DueHeadingTable2 = '//*[@id="table2"]/thead/tr/th[4]'
    DueHeadingtable1 = driver.find_element_by_xpath(xpath_DueHeadingTable1)
    classbefore = DueHeadingtable1.get_attribute('class')
    driver.find_element_by_xpath(xpath_DueHeadingTable1).click()
    classHading1 = DueHeadingtable1.get_attribute('class')
    print(classHading1)
    DueHeadingtable2 = driver.find_element_by_xpath(xpath_DueHeadingTable1)
    driver.find_element_by_xpath(xpath_DueHeadingTable2).click()
    classHading2 = DueHeadingtable2.get_attribute('class')
    print(classHading2)
    assert re.search("headerSortDown", classHading1) and re.search("headerSortDown", classHading2)



#ToDO f) Right a looped script to assert a 'successful notification" after repeated unsuccessful notification on page http://the-internet.herokuapp.com/notification_message_rendered
def test_successful_notification(SetupBrowser):
    url = "http://the-internet.herokuapp.com/notification_message_rendered"
    Maxretry =10
    retry=0
    driver.get(url)
    driver.find_element_by_link_text('Click here').click()
    time.sleep(2)
    message_text = driver.find_element_by_id('flash').text
    print(f"message_text is {message_text}")
    while re.search("Action unsuccesful.*", message_text) and retry < Maxretry:
        driver.find_element_by_link_text('Click here').click()
        time.sleep(2)

        message_text = driver.find_element_by_id('flash').text
        print(f"message_text is {message_text}")
        retry+=1

    assert re.search("Action successful.*", message_text), "Successful Notification not found after multiple retry"


