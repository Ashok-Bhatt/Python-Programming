# normal function
""" def counting(n):
    value = []
    for i in range(1, n+1):
        value.append("*"*i)
    return value 
"""

# generator function
def counting(n):
    for i in range(1, n+1):
        yield "*"*i

n = int(input("Enter n: "))
for i in counting(n):
    print(i)