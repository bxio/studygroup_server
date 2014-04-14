from server.models import Course, University, Student
from datetime import datetime

u = University(name="University of Victoria", latitude="48.4630959", longitude="-123.3121053")
u.save()
c = Course(name="CSc 111", start_date=datetime(2014, 5, 1), end_date=datetime(2014, 8, 31), university=u)
c.save()
c = Course(name="CSc 110", start_date=datetime(2014, 5, 1), end_date=datetime(2014, 8, 31), university=u)
c.save()