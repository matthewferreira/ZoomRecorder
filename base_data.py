import platform
import os

desktop = 'DESKTOP-6BL58T5'
laptop = 'LAPTOP-K5N3I4ET'

username = os.environ.get('CSUS_USERNAME')
password = os.environ.get('CSUS_PASSWORD')

#  detecting if program is being run on my laptop or desktop since my User names are different
if platform.uname().node == desktop:
    current_user = 'Matthew'
    join_a_meeting = (1275, 700)
    enter_meeting_id = (1265, 661)
    on_screen = enter_meeting_id

elif platform.uname().node == laptop:
    current_user = 'Matthew Ferreira'
    join_a_meeting = (755, 407)
    enter_meeting_id = (763, 373)
    on_screen = (962, 364)

