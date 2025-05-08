class Bank:
    
    def __init__(self) -> None:
        self._money = 0

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, amount):
        if amount >= 0:
            self._money = amount
        else:
            raise ValueError("Bank balance cannot be negative")

bank = Bank()
print(bank.money)
bank.money = 100
print(bank.money)
bank.money = 20
print(bank.money)
bank.money = -100
print(bank.money)