#  Write a Python program to split a given string (s) into strings if there is a space in s, otherwise split on commas if there is a comma,
#  otherwise return the list of lowercase letters in odd order (order of a = 0, b = 1, etc.).

string=input("Enter the string:")

if (" " in string):
    list1=string.split(" ")
    print(f"The required list is {list1}.")
elif ("," in string):
    list1=string.split(",")
    print(f"The required list is {list1}.")
else:
    if string=="":
        print("Please! Don't leave an string empty.")
    else:
        list1=[]
        for index,letter in enumerate(list(string)):
            if index%2==0:
                list1.append(letter.lower())
        print(f"The required list is given by {list1}.")