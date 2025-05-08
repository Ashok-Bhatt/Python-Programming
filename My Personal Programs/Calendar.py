year = int(input("Enter the year:"))
month = int(input("Enter the month number:"))

import calendar

# To print the calendar of an entire year
cal = calendar.calendar(year)

# To print the calendar of specific month
cal2 = calendar.month(year,month)

print(cal)
print(cal2)