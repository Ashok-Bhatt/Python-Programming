# Write a Python program to find the set of distinct characters in a given string, ignoring case.

text=input("Enter the string:")
text2=text.lower()
set_text=set(text2)
print("The set of distinct characters in given string is:",list(set_text))