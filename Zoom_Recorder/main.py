from Zoom_Recorder import ZoomRecorder as zr
from utils import canvas as cv, record as rec
from utils.Course import Course

#  creating specific course objects i want to record
stat50 = Course('stat50')
stat50.courseName = 'stat50'
csc137 = Course('csc137')
csc137.courseName = 'csc137'

#  login to canvas, get zoom id for specific class
zr.get_meeting_id(cv.login(), csc137)

#  open zoom and join meeting
zr.join_meeting(csc137)
zr.time.sleep(5)

#  start recording
rec.record()
