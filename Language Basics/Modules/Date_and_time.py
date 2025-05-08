from datetime import date
today=date.today()
print("Today's date is:",today)
print("Today's day is:",today.day)
print("Today's month is:",today.month)
print("Today's year is:",today.year)
print("Today's date in an isoformatted form is:",date.isoformat)

from datetime import datetime
date_time=datetime.fromtimestamp(1887639468)
print("Datetime from timestamp:",date_time)
current=datetime.now()
print("Current date and time is:",current)

from datetime import time
Time=time(11,34,56,4500)
print("The current hour is",Time.hour)
print("The current minute is",Time.minute)
print("The current second is",Time.second)
print("The current microsecond is",Time.microsecond)
Current_time=time()
print("The real current hour is",Current_time.hour)
print("The real current minute is",Current_time.minute)
print("The real current second is",Current_time.second)
print("The real current microsecond is",Current_time.microsecond)

from datetime import timedelta
print("today is :",(str(datetime.now())))
print("Date after one year is:",(str(datetime.now()+timedelta(days=365))))
print("Date after one week and 5 days is :",(str(datetime.now()+timedelta(weeks=1, days=5))))
print("Date after 15 days is:",(str(datetime.now()+timedelta(weeks=2, days= 1))))