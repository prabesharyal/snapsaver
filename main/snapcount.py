from datetime import datetime
from datetime import date
import time
import re
from datetime import timedelta
from unittest import skip


today = date.today()
today = date.today()
aaja = today.strftime("%m-%d-%y")
logfile = (str(aaja) + ".log")
try:
    filename = input("Enter your Logfile Name : ")
    with open (filename,'r'):
        print("File was input")
except FileNotFoundError:
    filename = logfile
total = 0
saved = 0
not_saved = 0
with open(filename,'r',encoding="unicode_escape") as f:
    logs = f.readlines()
    for lines in logs:
        chars = "[:0123456789.\-\, \n]"
        lines = re.sub(chars,'',lines).lower()
        if lines == "snapsavedsuccessfully":
            total = total + 1
            saved = saved + 1
        elif lines == "notsavedsnapissentwithplaylimit":
            total = total + 1
            not_saved = not_saved + 1
        else:
            continue

#For Time
w=open(filename,'r',encoding="unicode_escape")
first_line=w.readline()
for line in w:  
    x= line
last_line = x
w.close()
#Further for,atting
t1 = first_line[:19]
t2 = last_line[:19]
t1 = datetime.strptime(t1,"%Y-%m-%d %H:%M:%S")
t2 = datetime.strptime(t2,"%Y-%m-%d %H:%M:%S")

time_taken  = (t2-t1)
timestr = str(time_taken).split(":")
formattedtimestr = timestr[0]+" Hours "+timestr[1]+" Minutes "+ timestr[2]+" Seconds."


time_wasted=formattedtimestr
print("%50s"%"")
print("%50s"%"")
print("%50s"%"")
print("%50s"%"")
print("%50s"%"")
print("%50s"%"")
print("%50s"%"")
print("%50s"%"")
print("%50s"%"")
print("%50s"%"")
print("%50s"%"")
print("%50s"%"")
print("%50s"%"")
print("%70s"%"<--- Snap's Received as of {} -->".format(today.strftime("%B %d, %Y")))
print("%50s"%"")
print("%50s"%"Saved Snaps: {}".format(saved))
print("%50s"%"Snaps with Limit: {}".format(not_saved))
print("%50s"%"Total Snaps: {}".format(total))
print("%50s"%"")
print("%70s"%"Total time wasted : {} ".format(time_wasted))
print("%50s"%"")
print("%50s"%"")
print("%50s"%"")
print("%50s"%"")
print("%50s"%"")
print("%50s"%"")
print("%50s"%"")
print("%50s"%"")
print("%50s"%"")
print("%50s"%"")
print("%50s"%"")
print("%50s"%"")
