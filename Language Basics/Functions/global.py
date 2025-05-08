b=5
def add():
    a=8
    global b
    b+=2
    return a+b
print(add())

x=100
def ashok():
    x=10
    def bhatt():
        global x
        x=20
    print("The value of x before calling bhatt function is :",x)
    bhatt()
    print("The value of x after calling bhatt function is:",x)
ashok()
print(x)