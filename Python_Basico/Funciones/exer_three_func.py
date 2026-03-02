# Cree una función que retorne la suma de todos los números de una lista.
# La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
# [4, 6, 2, 29] → 41
def sum_list(num_list):
    total = 0
    for num in num_list:
        total = total + num
    return total


print(sum_list([4, 6, 2, 29]))  # Output: 41