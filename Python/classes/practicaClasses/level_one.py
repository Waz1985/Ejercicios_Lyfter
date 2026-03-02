class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def printCar(self):
        print(f"{self.brand} {self.model} ({self.year})")

car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Hyunday", "Elantra", 2026)

car1.printCar()
car2.printCar()


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount) -> float:
        try:
            if(self.balance < 0):
                print("Your balance must be greater than 0")
                return
            self.balance += amount
            print(f"{self.balance}")
        except TypeError:
            print("You must use a positive number")
        
    def withdraw(self, amount) -> float:
        try:
            if(self.balance < 0):
                print("Your balance must be greater than 0")
                return
            elif(self.balance < amount):
                print("Fondos infusicientes")
            else:
                self.balance -= amount
                print(f"{self.balance}")
        except TypeError:
            print("You must use a positive number")

cuenta1 = BankAccount("Wilmer", 10000)

cuenta1.deposit(10)

cuenta1.withdraw(11000)