#Cree un diagrama de flujo que tenga un numero secreto del 1 al 10, y le pida al usuario adivinar ese número. 
#El algoritmo no debe terminar hasta que el usuario adivine el numero.

import random

secret_number = random.randint(1, 10)
user_number = int(input("Guess the secret number between 1 and 10. Enter your number: "))
while user_number != secret_number:
    print(f"The number {user_number} you entered is incorrect, please enter another number between 1 and 10: ")
    user_number = int(input())
print(f"Congratulations! You have guessed the secret number {secret_number}.")  


#Cree un diagrama de flujo que pida 3 números al usuario. Si uno de esos números es 30, o si los 3 sumados dan 30, mostrar “Correcto”. 
#Sino, mostrar “incorrecto”.
#Ejemplos:
#23, 30, 768 → Correcto (hay un 30)
#10, 15, 5 → Correcto (10 + 15 + 5 = 30)
#35, 56, 2 → Incorrecto (no hay ningún 30, y la suma de ellos tampoco da 30)

first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
third_num = int(input("Enter the third number: "))

if first_num == 30 or second_num == 30 or third_num == 30:
    print("Correct")
elif first_num + second_num + third_num == 30:
    print("Correct")
else:
    print("Incorrect")      

