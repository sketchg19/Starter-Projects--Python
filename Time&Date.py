#Prints out current time and date

from datetime import date
import datetime
todays_date = date.today()
current_time = datetime.datetime.now()

#Date Strings
year = str(todays_date.year)
month = str(todays_date.month)
day = str(todays_date.day)

#Time Strings
hour = str(current_time.hour)
minute = str(current_time.minute)
second = str(current_time.second)

print(year + "/" + month + "/" + day)
print(hour + ":" + minute + ":" + second)
