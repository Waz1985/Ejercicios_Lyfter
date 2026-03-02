from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if not amount > 0:
            raise ValueError("The amount must be more than 0")
        self.balance += amount
        
    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(BankAccount):
    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.min_balance = min_balance
    
    def withdraw(self, amount):
        if not amount > 0:
            raise ValueError("The amount must be more than 0")
        elif amount > self.balance - self.min_balance:
            raise RuntimeError("Not enough money for this transaction")
        self.balance -= amount


acc = SavingsAccount(1000, 200)

print(acc.balance)      # 1000
print(acc.min_balance)  # 200

acc.withdraw(500)       # OK
acc.withdraw(400)
