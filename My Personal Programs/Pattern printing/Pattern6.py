num=int(input("Enter the number of stars at the base of a pyramid:"))

for i in range(num):
    print(" "*(2*(num-i+1))+"* "*(i+1))