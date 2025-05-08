class bankaccount:

    def __init__ (self,Account_number,name,balance):
        self.Account_number = Account_number
        self.name = name
        self.balance = balance

    def deposit(self):
        d = int(input("Enter the value you want to deposit: \n"))
        self.balance = self.balance + d

    def withdrawal(self):
        w = int(input("Enter the amount to withdraw :\n"))
        if w > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= w
            self.balance = self.balance - w
    
    def bankfees(self):
        b = 0.05 * self.balance
        self.balance = self.balance - b

    def Display(self):
        print(f"The name is {self.name},\n account number is {self.Account_number},\n and your balance is {self.balance}.")

Account_number = input("Enter your account number :\n")
name = input("Enter your name :\n")
balance = 750
account = bankaccount(Account_number,name,balance)

i = 0
while i <= 1:
    check = int(input("Enter 1 to depsit\nEnter 2 to withdraw\nenter 3 to display details\nenter 4 to exit\n"))
if (check == 1):
    account.deposit()
    account.bankfees()
elif (check == 2):
    account.withdrawal()
    account.bankfees()
elif (check == 3):
    account.Display()
elif (check == 4):
    exit()
else: 
    print("Invalid input")