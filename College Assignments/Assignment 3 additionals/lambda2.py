num = int(input("Enter the number:"))

y = lambda x:(x*2) if (x < 50) else (x*3) if(x > 50 and x < 100) else x 
z = y(num)
print(z)