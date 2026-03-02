# Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
# “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”

def find_upper_lower(my_str):
    if not isinstance(my_str, str):
        raise TypeError("Parameter must be a string")
    lowers = 0
    uppers = 0
    for char in my_str:
        if char.isupper():
            uppers += 1
        else:
            lowers += 1
    return f"There are {uppers} upper cases and {lowers} lower cases"


print(find_upper_lower("Hola Mundo"))
