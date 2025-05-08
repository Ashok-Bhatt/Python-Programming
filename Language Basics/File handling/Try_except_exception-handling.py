num1=input("Enter the first number:")
num2=input("Enter the second number:")

# try statement is used to try some code if it contains some errors. If no error, then it will execute the code written in print statement
try:
    print(int(num1)+int(num2))
# The code written in this statement is used if the code written in try statement has some error
except Exception as e:
    print(e)
print("My important code.")

try:
    print(int(num1))
    print(int(num2))
except:
    print("Please! Enter the number.")

try:
    num_list=input("Enter the list index:")
    list1=[1,2,3,4]
    print(list1[num_list])
except TypeError as type_error:
    print(type_error)
except IndexError as index_error:
    print(index_error)

string=input("Enter the number of states in South India.")
try:
    integer=int(string)
    print(integer)
except ValueError:
    print("Please! Enter an integer.")