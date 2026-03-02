from datetime import datetime, date as dt_date

class Category:
    def __init__(self, name, color="#DDDDDD"):
        if not name or not name.strip():
            raise ValueError("Category name cannot be empty")

        self.name = name.strip()
        self.color = color

class Movement:
    def __init__(self, date, title, amount, category, type):
        self.date = date
        self.title = title.strip()
        self.category = category.strip()
        self.type = str(type).upper()

        try:
            movement_date = datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Date must have format YYYY-MM-DD")
        
        if movement_date > dt_date.today():
            raise ValueError("Date cannot be in the future")

        self.date = date
        
        if self.type not in ("INCOME", "EXPENSE"):
            raise ValueError("Type must be INCOME or EXPENSE")

        try:
            self.amount = float(amount)
        except (TypeError, ValueError):
            raise TypeError("Amount must be a number")
        
        if self.amount <= 0:
            raise ValueError("Amount must be greater than 0")
    
        if not isinstance(date, str):
            raise TypeError("Date must be a String")

        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date must be in format: YYY-MM-DD")
        
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Title can't be empty")
        
        
        if not isinstance(category, str) or not category.strip():
            raise ValueError("Category can't be empty")
        
        


