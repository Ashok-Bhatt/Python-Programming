txt="ashok bhatt"
print(txt.capitalize())     # capitalize only capitalizes the first character of the entire string
print(txt.title())          # title capitalizes all the words present in the string

txt2="     Ashok Bhatt        "
print("The original version of txt2 is:",txt2)
print("The trimmed version of txt2 is:",txt2.strip())

txt3="Ashok Bhatt"
print("Using center method in txt3, we get:")
txt3_center=txt3.center(15)
print(txt3_center)

# If the value of center method is n, and the number of characters in a string is s, then no. of spaces from left = int((n-s)/2)
print("Penguine".center(30))