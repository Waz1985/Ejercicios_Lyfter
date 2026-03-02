# Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
# [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
# Tip 1: Investigue la logica matematica para averiguar si un numero es primo, y conviertala a codigo. No busque el codigo, eso no ayudaria.
# Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). 
# Así que lo mejor es agregar otra función para revisar si el numero es primo o no.
def search_prime_numbers(num_list):
    prime_numbers = [] 
    for num in num_list:
        if num <= 1:
            continue
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            prime_numbers.append(num)
    return prime_numbers
print(search_prime_numbers([1, 4, 6, 7, 13, 9, 67]))