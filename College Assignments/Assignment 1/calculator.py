class Calculator:
    
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2
    def sub(self):
        return self.num1 - self.num2
    def mul(self):
        return self.num1 * self.num2
    def div(self):
        return self.num1 / self.num2

n1 = int(input("Enter the first number:"))
n2 = int(input("Enter the second number:"))

solution1 = Calculator(n1,n2)

choice = "+"
while choice in "*+/-":
    choice = input("\nEnter '+' for addition, '-' for subtraction, '*' for multiplication, '/' for division:")

    if choice == "+":
        print(f"{n1} + {n2} = {solution1.add()}")
    elif choice == "-":
        print(f"{n1} - {n2} = {solution1.sub()}")
    elif choice == "*":
        print(f"{n1} * {n2} = {solution1.mul()}")
    elif choice == "/":
        print(f"{n1} / {n2} = {solution1.div()}")
    else:
        print("Invalid Service!")