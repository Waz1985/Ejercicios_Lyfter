from datetime import date
from functools import wraps

def adult_validation(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not isinstance(self, User):
            raise TypeError("Method must be called on a User")
        if self.age < 18:
            raise PermissionError("You're not an adult")
        return func(self, *args, **kwargs)
    return wrapper

class User:
    def __init__(self, date_of_birth: date):
        self.date_of_birth = date_of_birth

    @property
    def age(self) -> int:
        today = date.today()
        return(
            today.year
            - self.date_of_birth.year
            - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        )    

    @adult_validation
    def get_driver_license(self):
        return "License permitted"

