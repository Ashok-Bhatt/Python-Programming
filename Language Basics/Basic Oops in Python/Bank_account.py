class Bank_Account:

    def __init__(self,accountNumber,name,balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def Deposite(balance,deposite):
        balance += deposite
    
    def Withdrawl(balance,withdrawal):
        balance -= withdrawal
    
    def bankFees(balance):
        balance -= balance*(5/100)

    def display(self):
        return [self.accountNumber, self.name, self.balance]

beginning_balance = float(input("Enter the balance at the beginning of the account creation:"))
Account_Holder = Bank_Account(1234567890,"Ashok Bhatt",beginning_balance)

transition = "w"
while transition in "wd":
    transition = input("Enter the choice, w to withdraw the money and d to deposite the money and anything else to leave.")
    if transition == "w":
        amount = float(input("Enter the amount you want to withdraw:"))
        Account_Holder.Withdrawl(beginning_balance)
        Account_Holder.bankFees(beginning_balance)
    elif transition == "d":
        amount = float(input("Enter the amount you want to deposite:"))
        Account_Holder.Deposite(beginning_balance)
        Account_Holder.bankFees(beginning_balance)