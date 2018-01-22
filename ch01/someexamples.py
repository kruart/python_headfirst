import sys
print(sys.platform)       # linux
print(sys.version)        # 3.5.2 (default, Nov 23 2017, 16:37:01)

import os
print(os.getcwd())        # return a string representing the current working directory.
print(os.environ)         # env variables
print(os.getenv('HOME'))  # home os directory


import datetime
print(datetime.date.today())
print(datetime.date.today().day)
print(datetime.date.today().month)
print(datetime.date.today().year)

import calendar
today = calendar.day_name[datetime.date.today().weekday()]
if today == 'Monday':
    print("Monday... Party!!")
elif today == 'Sunday':
    print("Recover")
else:
    print("Work, work, work.")


import time
print(time.strftime('%H:%M'))   # get current time
print(time.strftime('%A %p'))


import html
print(html.escape("This HTML fragment contains a <script>script</script> tag."))
print(html.unescape("I &hearts; Python's &lt;standard library&gt;."))

