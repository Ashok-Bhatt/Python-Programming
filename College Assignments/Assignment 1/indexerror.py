my_list = [1, 2, 3, 4, 5]
try:
    index = int(input("enter the index number: "))
    print(my_list[index])
except IndexError:
    print("Index out of range.")