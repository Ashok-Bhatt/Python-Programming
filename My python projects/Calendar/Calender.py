# year and month are two years that will take year and month as input in numbers
year = int(input("Enter the year number:"))
month = int(input("Enter the month number:"))

from datetime import datetime,timedelta
import time

# reqdate will denote the first date of the provided month and year.
# On printing the reqdate, the output will be: YYYY-MM-01 00:00:00
reqdate = datetime(year , month , 1)

# weekday function will return the day number to the corresponding date, i.e. '0' for Monday, '1' for Tuesday upto '6' for Sunday
# reqday is the day when the calendar will show first day of the month
reqday = reqdate.weekday()

# calender is the list that will take the dates at specific index to make a calander
# The calendar list has five sub-lists which denotes the five week of the month. 
# Incase, the month that contains only 4 weeks the last sub-list will remain empty and for 6 weeks the date will be printed in week 1
# Each sub-list has seven empty strings that symbolises the seven days of the week. First element will be sunday and last one will be saturday
calendar = [["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""]]

# month_date is the date of month which has been taken 1 initilly which will increase upto 28, 29, 30 or 31 depending on month and leap year
month_date = 1

# month_week will symbolise the week number of the month. The first week number is taken 0 instead of 1 as the first list index is 0
# It will get increased by 1 after all days in a week are assigned to the list
month_week = 0

# eachdate is the copy of reqdate. 
# We are not taking the reqdate to enter in loop because we want to compare the month number of reqdate and eachdate as the date of eachdate  will get increased by one after each cycle of loop which would jump to next month in some period of time
eachdate = reqdate

# eachdate: YYYY-MM-01 =====> Month indices are 5 and 6, so the range will be [5:7] (7 is not inclusive)
# We are comparing the the month indices of eachdate and reqdate and the loop will only continue till both values are equal
while int(str(eachdate)[5:7])==int(str(reqdate)[5:7]):

    # We are using the conditional statement to check whether the 6th index (i.e. Saturday element) of the sub-list is filled or not
    # If the 6th index is filled then the element won't be empty and thus we will move to the next sub-list (i.e. next week)
    if calendar[month_week][6]!="":

        # If the filled saturday element belongs to week 0,1,2,3 then it has completed first four weeks and will enter the fifth week by increasing the value of month_week by 1
        if month_week<4:
            month_week +=1

        # If the value of month_week is 4, it means it has crossed the five weeks of the month and will enter the sixth week
        # We hasn't created the 6th sub-list as the dates of sixth week will be printed on the first week i.e. index 0
        # For better understanding, try to print the calendar of year 2024 March
        else:
            month_week = 0

    # eachday will we the corresponding day to the eachdate as same as of reqdate and reqday
    eachday = eachdate.weekday()

    # The first day of the calendar is Sunday while that of weekday() function is Monday. So, to handle that problem we are using the below formula
    # The value of month_date will be assigned to the calendar list having the month_week and the day corresponding to the date as their first and second indices respectively
    calendar[month_week][(eachday+1)%7]=month_date

    # After each cycle the month_date wil be increased by 1 to assign the date to the required day of required week
    month_date += 1
    
    # eachdate will jump to the next date to track down the month number to check whether the month is changed or not
    # If the month number is changed then the month of eachdate and reqdate will be differnt and the loop will be terminated
    eachdate = eachdate + timedelta(days=1)

# day_list and month_list is the list of days of the week and months of the year that will be needed in our furthur program
day_list = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
month_list = ["JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE","JULY","AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER"]

print("")

# We are printing "-" 78 times to create the outline of the calendar and the number of characters in each line of execution will remain 78
print("-"*78)
# We will be using the time.sleep() function to pause the program for 0.05 seconds to make the printing effect for the calendar
time.sleep(0.05)

print("|"," "*76,"|",sep="")
time.sleep(0.05)

# We are printing the element of month_list with index (month-1) from month_list as indexing starts from 0 and end at 11
# Total no. of characters = 2 (1 for each "|") + 72 (for year number and centered month name) + 4 (for distance between outline and year) = 78
print("|",str(month_list[month-1]).center(72-len(str(year))),str(year),"    |",sep="")
time.sleep(0.05)

print("|"," "*76,"|",sep="")
time.sleep(0.05)

# No. of characters = 10*7 (for "-" symbol) + 8 (for "|" symbol) = 70+8 = 78
print("|----------|----------|----------|----------|----------|----------|----------|")
time.sleep(0.05)

# No. of characters = 10*7 (for " " symbol) + 8 (for "|" symbol) = 70+8 = 78
print("|          |          |          |          |          |          |          |")
time.sleep(0.05)

# There are 10 "-" characters between two "|" symbols, so each element of day_list (i.e. each day) is printed with center method of length 10
print(f"|{day_list[0].center(10)}|{day_list[1].center(10)}|{day_list[2].center(10)}|{day_list[3].center(10)}|{day_list[4].center(10)}|{day_list[5].center(10)}|{day_list[6].center(10)}|")
time.sleep(0.05)

print("|          |          |          |          |          |          |          |")
time.sleep(0.05)

print("|----------|----------|----------|----------|----------|----------|----------|")

for weeks in calendar:

    time.sleep(0.05)
    print("|          |          |          |          |          |          |          |")

    time.sleep(0.05)
    # We are printing every elment of sub-list weeks from the list calendar with centered string of length 10
    print(f"|{str(weeks[0]).center(10)}|{str(weeks[1]).center(10)}|{str(weeks[2]).center(10)}|{str(weeks[3]).center(10)}|{str(weeks[4]).center(10)}|{str(weeks[5]).center(10)}|{str(weeks[6]).center(10)}|")

    time.sleep(0.05)
    print("|          |          |          |          |          |          |          |")

    time.sleep(0.05)
    print("|----------|----------|----------|----------|----------|----------|----------|")