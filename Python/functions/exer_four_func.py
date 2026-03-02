# Cree una función que le de la vuelta a un string y lo retorne.
# Esto ya lo hicimos en iterables.
# “Hola mundo” → “odnum aloH”

def reverse_strings(my_string):
    if not isinstance(my_string, str):
        raise TypeError("Parameter must be a string")
    reversed_str = ""
    for char in range(len(my_string)-1, -1, -1):
        reversed_str += my_string[char]
    return reversed_str

print(reverse_strings("Hola Mundo"))
