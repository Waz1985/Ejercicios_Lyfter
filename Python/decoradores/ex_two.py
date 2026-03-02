def is_number_validation(function):
    def wrapper(*args, **kwargs):
        for value in args:
            if not isinstance(value, (int, float)):
                raise TypeError("All parameters must be numbers")
            
        for value in kwargs:
            if not isinstance(value, (int, float)):
                raise TypeError("All parameters must be numbers")
        
        return function(*args, **kwargs)
    return wrapper

@is_number_validation
def show_numbers(number_one, number_two):
    print(f"The numbers are: {number_one} and {number_two}")

show_numbers(1, 2)