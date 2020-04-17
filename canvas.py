from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import base_data
import time


#  METHOD - logging in to csus canvas
def login():

    browser = webdriver.Firefox(executable_path='C:\\Users\\' + base_data.current_user + '\\Downloads\\geckodriver.exe')
    browser.set_window_position(0, 0)
    browser.set_window_size(1920, 1080)
    browser.get('https://csus.instructure.com/')

    #  entering username into username text field
    user_elem = browser.find_element_by_css_selector('#username')
    user_elem.send_keys(base_data.username)

    #  entering password into password text field
    password_elem = browser.find_element_by_css_selector('#password')
    password_elem.send_keys(base_data.password)
    password_elem.send_keys(Keys.RETURN)

    #  giving time for browser to load.
    time.sleep(5)

    #returning browser so we can use same object with different functions
    return browser
