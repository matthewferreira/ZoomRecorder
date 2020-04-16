from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pynput.keyboard as kb
import pynput.mouse as ms
import os, subprocess, platform, time
from Course import Course


desktop = 'DESKTOP-6BL58T5'
laptop = 'LAPTOP-K5N3I4ET'

#  detecting if program is being run on my laptop or desktop since my User names are different
if platform.uname().node == desktop:
    current_user = 'Matthew'
elif platform.uname().node == laptop:
    current_user = 'Matthew Ferreira'


#  creating a browser
browser = ''

#  making keyboard and mouse controllers to navigate the PC automatically
keyboard = kb.Controller()
mouse = ms.Controller()

stat50 = Course('stat50')
stat50.courseName = 'stat50'
csc137 = Course('csc137')
csc137.courseName = 'csc137'


username = os.environ.get('CSUS_USERNAME')
password = os.environ.get('CSUS_PASSWORD')


    #  METHOD - logging in to csus canvas
def login():

    browser = webdriver.Firefox(executable_path='C:\\Users\\' + current_user + '\\Downloads\\geckodriver.exe')
    browser.set_window_position(0, 0)
    browser.set_window_size(1920, 1080)
    browser.get('https://csus.instructure.com/')

    #  entering username into username text field
    user_elem = browser.find_element_by_css_selector('#username')
    user_elem.send_keys(username)

    #  entering password into password text field
    password_elem = browser.find_element_by_css_selector('#password')
    password_elem.send_keys(password)
    password_elem.send_keys(Keys.RETURN)

    #  giving time for browser to load.
    time.sleep(5)
    return browser


    #  METHOD - getting newest meeting id from canvas course
def get_meeting_id(browser, course: Course):
    #  courseNum is a variable for the number used in the HTML on canvas. for example: my csc 131 class is n-th child(1)
    if course.courseName == 'csc137':
        course.courseNum = 2
    elif course.courseName == 'stat50':
        course.courseNum = 4

    #  clicking on link to respective course
    course_elem = browser.find_element_by_css_selector('div.ic-DashboardCard:nth-child(' + str(course.courseNum) + ') > div:nth-child(1) > div:nth-child(2)')
    course_elem.click()

    time.sleep(5)
    #  clicking on the 'zoom' link in the course sidebar. Uses same class for every course
    zoom_link_elem = browser.find_element_by_css_selector('.context_external_tool_1818')
    zoom_link_elem.click()

    time.sleep(5)

    #  since the content i need is in a different <iframe> tag in the HTML code, need to switch to the correct frame 'tool_content'
    browser.switch_to.frame('tool_content')

    #  grabbing values of every row. Notice the most recent meeting id will always be the 6th val in the array
    row_values = browser.find_elements_by_css_selector('.ant-table-row-cell-break-word')
    meeting_id = row_values[5].text
    course.meeting_id = meeting_id

    browser.quit()


def join_meeting(course: Course):

    #  starting a subprocess that opens up the Zoom app on my pc
    zoom = subprocess.run(['start', 'C:\\Users\\' + current_user + '\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe'], shell=True)

    time.sleep(2)

    #  automatically navigating the UI of the zoom window. clicking the "join a meeting" button
    mouse.position = (1275, 700)
    mouse.press(ms.Button.left)
    mouse.release(ms.Button.left)

    time.sleep(2)

    #  clicking text box to enter a meeting ID
    mouse.position = (1265, 661)
    mouse.press(ms.Button.left)
    mouse.release(ms.Button.left)

    time.sleep(2)
    #  typing the meeting ID we found into the text box and pressing enter
    keyboard.type(course.meeting_id)
    keyboard.press(kb.Key.enter)
    keyboard.release(kb.Key.enter)

    time.sleep(2)
    mouse.click(ms.Button.left, 1)
    keyboard.press(kb.Key.cmd)
    keyboard.press(kb.Key.up)
    time.sleep(0.5)
    keyboard.release(kb.Key.up)
    keyboard.release(kb.Key.cmd)


def record():
    #  windows + alt + R starts the game recorder in windows
    keyboard.press(kb.Key.cmd)
    keyboard.press(kb.Key.alt)
    keyboard.press('r')
    time.sleep(0.5)
    keyboard.release(kb.Key.cmd)
    keyboard.release(kb.Key.alt)
    keyboard.release('r')


get_meeting_id(login(), csc137)
join_meeting(csc137)
time.sleep(10)
record()


