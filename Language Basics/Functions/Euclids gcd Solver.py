n1, n2 = map(int, input("Enter two numbers separted by space:").split())

num1 = n1
num2 = n2
while (num1>0 and num2>0) :
    print(f"{num1} = {num2} X {num1//num2} + {num1%num2}")
    num3 = num1
    num1 = num2
    num2 = num3 % num2

if num1 == 0:
    print(f"\ngcd({n1},{n2}) = {num2}")
else:
    print(f"\ngcd({n1},{n2}) = {num1}")