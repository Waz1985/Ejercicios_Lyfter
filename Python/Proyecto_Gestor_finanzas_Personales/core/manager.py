from core.models import Category, Movement
from datetime import datetime

class Manager:
    def __init__(self):
        self.categories = []
        self.movements = []

    def has_categories(self):
        return bool(self.categories)
    
    def add_category(self, category):        
        for existing in self.categories:
            if existing.name.lower() == category.name.lower():
                raise ValueError("Category already exists")        
        self.categories.append(category)

    def add_movement(self, date, title, amount, category, type):
        if not self.categories:
            raise ValueError("No categories available")
        category_exists = False
        for cat in self.categories:
            if cat.name.lower() == category.lower():
                category_exists = True
                break
        
        if not category_exists:
            raise ValueError("Category does not exist")

        movement = Movement(
            date = date,
            title = title,
            amount = amount,
            category = category,
            type = type
        )

        self.movements.append(movement)

    def total_incomes(self):
        return sum(m.amount for m in self.movements if m.type == "INCOME")


    def total_expenses(self):
        return sum(m.amount for m in self.movements if m.type == "EXPENSE")


    def balance(self):
        return self.total_incomes() - self.total_expenses()
    
    def get_movements_between(self, start_date, end_date):
        try:
            start = datetime.strptime(start_date, "%Y-%m-%d").date()
            end = datetime.strptime(end_date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Dates must have format YYYY-MM-DD")

        if start > end:
            raise ValueError("Start date must be before or equal to end date")

        filtered = []

        for m in self.movements:
            mov_date = datetime.strptime(m.date, "%Y-%m-%d").date()
            if start <= mov_date <= end:
                filtered.append(m)

        return filtered
