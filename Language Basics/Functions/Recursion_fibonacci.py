def fibonacci(n):
    """
fibonacci function is used to print n fibonacci terms
The number passed in arguments should be only positive number
    """
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
n = int(input("Enter number of terms:"))
print("Fibonacci sequence for given number of terms is given by:",end=" ")
for i in range(n):
    print(fibonacci(i),end=" ")