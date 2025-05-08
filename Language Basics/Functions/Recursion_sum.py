def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)

num = int(input("Enter the num:"))
if num<=0:
    print("Please! Enter the natural number.")
else:
    print(f"The sum of first {num} number is {sum(num)}.")