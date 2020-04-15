from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pynput.keyboard as kb
import pynput.mouse as ms
from bs4 import BeautifulSoup
import requests
import os
import pprint as pp
from Course import Course

browser = webdriver.Firefox(executable_path=r'C:\Users\Matthew\Downloads\geckodriver.exe')
browser.set_window_position(0, 0)
browser.set_window_size(1920, 1080)
browser.get('https://csus.instructure.com/')
keyboard = kb.Controller()
mouse = ms.Controller()


username = os.environ.get('CSUS_USERNAME')
password = os.environ.get('CSUS_PASSWORD')

def login():

    #entering username into username text field
    user_elem = browser.find_element_by_css_selector('#username')
    user_elem.send_keys(username)

    #entering password into password text field
    password_elem = browser.find_element_by_css_selector('#password')
    password_elem.send_keys(password)
    password_elem.send_keys(Keys.RETURN)

    #giving time for browser to load
    time.sleep(10)

def get_meeting_id(courseName):
    course = Course(courseName)
    if course.courseName == 'csc137':
        course.courseNum = 2
    elif course.courseName == 'stat50':
        course.courseNum = 4

    course_elem = browser.find_element_by_css_selector('div.ic-DashboardCard:nth-child(' + str(course.courseNum) + ') > div:nth-child(1) > div:nth-child(2)')
    course_elem.click()

    time.sleep(5)

    zoom_link_elem = browser.find_element_by_css_selector('.context_external_tool_1818')
    zoom_link_elem.click()

    time.sleep(5)

    browser.switch_to.frame('tool_content')
    meeting_ids = browser.find_elements_by_css_selector('.ant-table-row-cell-break-word')
    meeting_id = meeting_ids[5].text
    print(meeting_id)


def csc137():
    #selecting and clicking csc137 element on dashboard to access class links
    csc137_elem = browser.find_element_by_css_selector('div.ic-DashboardCard:nth-child(2) > div:nth-child(1) > div:nth-child(2)')
    csc137_elem.click()

    #time for browser to load
    time.sleep(5)

    #selecting and clicking the zoom link for csc137
    csc137_zoom = browser.find_element_by_css_selector('.context_external_tool_1818') #NOTE: this is the same selector for every class
    csc137_zoom.click()
    time.sleep(8)

    browser.switch_to.frame('tool_content')
    meeting_ids = browser.find_elements_by_css_selector('.ant-table-row-cell-break-word')

    meeting_id = meeting_ids[5].text
    print(meeting_id)


def stat50():
    stat50_elem = browser.find_element_by_css_selector('div.ic-DashboardCard:nth-child(4) > div:nth-child(1) > div:nth-child(2)') #NOTE: the value in nth-child can be used to select a class based on order
    stat50_elem.click()
    stat50_zoom = browser.find_element_by_css_selector('.context_external_tool_1818')
    stat50_zoom.click()

    time.sleep(5)

def csc131():
    # selecting and clicking csc137 element on dashboard to access class links
    csc131_elem = browser.find_element_by_css_selector(
        'div.ic-DashboardCard:nth-child(1) > div:nth-child(1) > div:nth-child(2)')
    csc131_elem.click()

    # time for browser to load
    time.sleep(5)

    # selecting and clicking the zoom link for csc137
    csc131_zoom = browser.find_element_by_css_selector(
        '.context_external_tool_1818')  # NOTE: this is the same selector for every class
    csc131_zoom.click()
    time.sleep(50)




def record():

    keyboard.press(kb.Key.cmd)
    keyboard.press(kb.Key.alt)
    keyboard.press('r')
    time.sleep(1)
    keyboard.release(kb.Key.cmd)
    keyboard.release(kb.Key.alt)
    keyboard.release('r')

login()
get_meeting_id('csc137')

#time.sleep(2)




#browser.quit()
