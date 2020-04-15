from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pynput.keyboard as kb
import pynput.mouse as ms
from bs4 import BeautifulSoup
import requests

#browser = webdriver.Firefox(executable_path=r'C:\Users\Matthew Ferreira\Downloads\geckodriver.exe')
#browser.set_window_position(0, 0)
#browser.set_window_size(1920, 1080)
#browser.get('https://csus.instructure.com/')
keyboard = kb.Controller()
mouse = ms.Controller()


username = 'matthewferreira'
password = 'nQMjKBJP78Le2rQ'

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


def csc137():
    #selecting and clicking csc137 element on dashboard to access class links
    csc137_elem = browser.find_element_by_css_selector('div.ic-DashboardCard:nth-child(2) > div:nth-child(1) > div:nth-child(2)')
    csc137_elem.click()

    #time for browser to load
    time.sleep(5)

    #selecting and clicking the zoom link for csc137
    csc137_zoom = browser.find_element_by_css_selector('.context_external_tool_1818') #NOTE: this is the same selector for every class
    csc137_zoom.click()
    time.sleep(5)


def join_lecture():
    mouse.position = (1218, 421)
    mouse.press(ms.Button.left)
    mouse.release(ms.Button.left)

    time.sleep(8)
    '''
    mouse.position = (787, 554)
    mouse.press(ms.Button.left)
    mouse.release(ms.Button.left)

    time.sleep(50)
    '''
def get_meeting_id():


    URL = 'https://csus.instructure.com/courses/62173/external_tools/1818'
    page = requests.get(URL, auth=(username, password))
    soup = BeautifulSoup(page.content, 'html.parser')
    #soup.select('#username')
    #results = soup.select('#integration-meeting-list > div > div > div > div > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > div')
    #print(results[0].text)
    print(page.content)


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

get_meeting_id()

#time.sleep(2)




#browser.quit()
