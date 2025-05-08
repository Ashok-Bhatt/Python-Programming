def gcd(x,y):
    if x==0:
        print(y)
    elif y==0:
        print(x)
    else:
        gcd(y, x%y)

num1, num2 = map(int, input("Enter two numbers separated by space:").split())
gcd(num1, num2)