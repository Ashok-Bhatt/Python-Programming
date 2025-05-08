num=int(input("Enter the number of stars at the base of pyramid:"))

for i in range(1,num+1):
    print(" "*(num-i)+"* "*i)