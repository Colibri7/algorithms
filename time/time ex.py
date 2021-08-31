from datetime import date, datetime
import pytz

datetime_object = date.today()
print("Current date =", datetime_object)
print("Current year =", datetime_object.year)
print("Current month =", datetime_object.month)
print("Current day =", datetime_object.day)
date_string = "21 June, 2018"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

local = datetime.now()
print(f'local {local.strftime("%m/%d/%Y,time: %H:%M:%S")}')

tz_NY = pytz.timezone('America/New_York')
datetime_NY = datetime.now(tz_NY)
print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))
