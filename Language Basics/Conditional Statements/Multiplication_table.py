# num denotes the number whose multiplication we want to find
num = int(input("Enter the number whose multiplication table you want to find:"))

print("\nThe multiplication of given number is given by:")
for i in range(10):
    print("{} X {} = {}".format(num,i+1,num*(i+1)))