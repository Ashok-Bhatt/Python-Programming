import math

# ang is the angle whose cosine value we want to find
ang=float(input("Enter the angle at which you want to find the cosine function(in degree):"))
angle=math.radians(ang)     # angle is the radian counterpart of given ang specified in degree
initial_value=1
i=1
power=2
while i<=30:
    initial_value-=(((angle)**(power)/math.factorial(power))-((angle)**(power+2)/math.factorial(power+2)))
    i+=1
    power+=4
print("The value of cos {} is : {} (approx)".format(ang,initial_value))