# Cree una función que retorne la suma de todos los números de una lista.
# La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
# [4, 6, 2, 29] → 41
def sum_list(num_list):
    total = 0
    for num in num_list:
        if not isinstance(num, (int, float)):
            raise TypeError("Elements must be numbers")
        total = total + num
    return total


print(sum_list(list(range(150))))  # Output: 41