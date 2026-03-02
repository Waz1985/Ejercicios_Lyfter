from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass
    
    @abstractmethod
    def withdraw(self, amount):
        pass

    def _validate_amount(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number")
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")


class SavingsAccount(BankAccount):
    def deposit(self, amount):
        self._validate_amount(amount)
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        self._validate_amount(amount)
        if amount > self.balance:
            raise ValueError("Not enough savings balance")
        
        self.balance -= amount 

        return self.balance


class CheckingAccount(BankAccount):
    def __init__(self, name, balance, overdraft_limit=0):
        super().__init__(name, balance)    
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        self._validate_amount(amount)
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        self._validate_amount(amount)
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Overdraft limit exceeded")
        self.balance -= amount
        return self.balance




savings = SavingsAccount("Wilmer", 1000)
checking = CheckingAccount("Wilmer", 500, overdraft_limit=300)

print(savings.deposit(200))     # 1200
print(savings.withdraw(300))    # 900

print(checking.withdraw(700))   # -200
print(checking.deposit(500))    # 300