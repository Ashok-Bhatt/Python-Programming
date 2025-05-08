import time

# mytime indicates the current time according to 24 hour HH:MM:SS format
mytime=time.strftime("%H:%M:%S")
print("The current time is:",mytime)

# The indices from 0 to 2-1=1 refers to the hour count of current time
if (int(mytime[0:2])<=11):
    print("Good Morning Sir!")
elif (12<=int(mytime[0:2])<=15):
    print("Good Afternoon Sir!")
elif (16<=int(mytime[0:2])<24):
    print("Good Evening sir!")