#!/usr/bin/env python3
import subprocess
import time
from utils import base_data, Course, record as rec
import pynput.mouse as ms

enter_meeting_id = base_data.zoom_setup()[0]
join_a_meeting = base_data.zoom_setup()[1]
on_screen = base_data.zoom_setup()[2]

#creating mouse controller to navigate PC automatically
mouse = ms.Controller()

#  METHOD - getting newest meeting id from canvas course
def get_meeting_id(browser, course: Course):

    #  courseNum is a variable for the number used in the HTML elements on canvas. for example: my csc 131 class is n-th child(1)
    time.sleep(5)
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

    #close browser
    browser.quit()

#METHOD: start zoom app and move mouse into correct positions to join a meeting
def join_meeting(course: Course):

    #  starting a subprocess that opens up the Zoom app
    zoom = subprocess.Popen(["C:\\Users\\{}\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe".format(base_data.current_user)], shell=True)

    time.sleep(2)

    #  automatically navigating the UI of the zoom window. clicking the "join a meeting" button
    mouse.position = join_a_meeting
    mouse.click(ms.Button.left, 1)

    time.sleep(2)

    #  clicking text box to enter a meeting ID
    mouse.position = enter_meeting_id
    mouse.click(ms.Button.left, 2)

    time.sleep(2)

    #  typing the meeting ID we found into the text box and pressing enter
    rec.keyboard.type(course.meeting_id)
    rec.keyboard.press(rec.kb.Key.enter)
    rec.keyboard.release(rec.kb.Key.enter)

    time.sleep(2)

    #  moving mouse to a position that will be on the new zoom window. different for each computer.
    mouse.position = on_screen
    mouse.click(ms.Button.left, 1)

    #  windows + up arrow puts a lot of applications into fullscreen.
    rec.keyboard.press(rec.kb.Key.cmd)
    rec.keyboard.press(rec.kb.Key.up)
    time.sleep(0.5)
    rec.keyboard.release(rec.kb.Key.up)
    rec.keyboard.release(rec.kb.Key.cmd)
