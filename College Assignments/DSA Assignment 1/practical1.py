# Call by value
def passed_string(string):
    string = "Data Structures and Algorithms"
    print("String inside Function:", string)
     
string = "DSA"
passed_string(string)
print("String outside Function:", string)

# Pass by value
def passed_list(x):
    x[0] = 10
    print("\nList inside function:",x)

list1 = [0,10,20,30,40]
passed_list(list1)
print("List outside function:",list1)