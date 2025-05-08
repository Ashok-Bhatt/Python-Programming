num=int(input("Enter the size of foot of the triangle:"))

for i in range(1,num+1):
    print(" "*(len(str((num-i)))),end="")
    for j in range(1,i+1):
        print(i,end="")
    print()