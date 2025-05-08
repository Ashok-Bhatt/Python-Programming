number=int(input("Enter the number whose multiplication table you are seeking:"))
print(f"\nThe multiplication table of {number} is given by:")
for i in range(10):
    print(f"{number} X {i+1} = {number*(i+1)}")