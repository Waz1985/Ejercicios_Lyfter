# Cree una función que le de la vuelta a un string y lo retorne.
# Esto ya lo hicimos en iterables.
# “Hola mundo” → “odnum aloH”

def reverse_strings(str):
    reversed_str = ""
    for char in range(len(str)-1, -1, -1):
        reversed_str += str[char]
    return reversed_str
print(reverse_strings("Hola mundo"))  # Output: odnum aloH