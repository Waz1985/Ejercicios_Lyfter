from abc import ABC, abstractmethod

# class User(ABC):
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.active = True        

#     def deactivate(self):
#         self.active = False

#     def activate(self):
#         self.active = True

#     @abstractmethod
#     def get_info(self):
#         status = "Active" if self.active else "Inactive"
#         return f"{self.name} | {self.email} | {status}"
    

# class Employee(User):
#     def __init__(self, name, email, salary):
#         super().__init__(name, email)
#         self.salary = salary

#     def get_info(self):
#         base_info = super().get_info()
#         return f"{base_info} | Salary: ${self.salary}"
    
#     def annual_salary(self):
#         return self.salary * 12
    
class Payment:
    def __init__(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be higher than '0'")
        self.amount = amount
    
    @abstractmethod
    def process(self):
        raise NotImplementedError("Must implement process method")
    
class CreditCardPayment(Payment):
    def __init__(self, amount):
        super().__init__(amount)
    
    def process(self):
        return f"Processing Credit Card Payment Method of: {self.amount}"
    

class PayPalPayment(Payment):
    def __init__(self, amount):
        super().__init__(amount)

    def process(self):
        return f"Processing PayPal Payment Method of: {self.amount}"

payments = [
    CreditCardPayment(100),
    PayPalPayment(250)
]

for payment in payments:
    print(payment.process())