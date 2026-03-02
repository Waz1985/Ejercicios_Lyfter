class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Company:
    def __init__(self, name):
        self.name = name
        self.employees_list = []

    def add_employee(self, employee: Employee):
        if not isinstance(employee, Employee):
            raise TypeError("Only Employee instances allowed")
        
        if self.employee_exists(employee.name, employee.salary):
            print(f"Employee {employee.name} already exists.")
            return False
        self.employees_list.append(employee)
        return True
    
    def employee_exists(self, name: str, salary: float) -> bool:
        for e in self.employees_list:
            if e.name == name and e.salary == salary:
                return True
        return False
    
    def get_total_payroll(self):
        total = 0.0
        for e in self.employees_list:
            total += e.salary
        return total
    
    def get_employees(self):
        return self.employees_list
            



e1 = Employee("Ana", 1200)
e2 = Employee("Luis", 1500)
employees = []
company = Company("TechCorp")
company.add_employee(e1)
company.add_employee(e1)
company.add_employee(e2)
for e in company.get_employees():
    print(f"Name: {e.name}, Salary: {e.salary}")
print(company.get_total_payroll())