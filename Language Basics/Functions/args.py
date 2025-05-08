# Function without args:
def addition(num1,num2,num3,num4,num5):
    """
add function is used to add the passed numbers in arguments
This function can take only five arguments, not less or more
    """
    return num1+num2+num3+num4+num5
print(addition(1,2,3,4,5))

# Function with args:
def add(*args):
    """
add function is used to add the passed numbers in arguments
This function can take as many arguments as it can take
    """
    sum=0
    for i in args:
        sum=sum+i
    return sum

print(add(1,2,3,4,5))

# Passing list in the argument of the function:
introduction="The first and last fruit from the list are:"
def first(intro,*args):   # arguments passed in the function for this scenerio will be tuple
    """
first function will return the first and last element of the list
    """
    print(intro,args[0],args[-1])
fruits=("Apple","Banana","Cherry")
first(introduction,*fruits)

# Using kwargs to run a program which could have run without it:
position={"Ashok Bhatt":"Front-End Developer","Krunal Patel":"Back-End Developer","Mithun Sharma":"Project Manager"}
def position_assignment(**kwargs):
    for key,value in position.items():
        print(f"The position of {key} is {value}.")
position_assignment(**position)

# Running kwargs specific program:
def position_assignment(kwargs):
    for key,value in kwargs.items():
        print(f"The position of {key} is {value}.")
position_assignment({"Ashok Bhatt":"Front-End Developer","Krunal Patel":"Back-End Developer","Mithun Sharma":"Project Manager"})