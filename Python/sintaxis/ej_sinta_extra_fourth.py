# Tabla de multiplicar personalizada
# Pida al usuario un número del 1 al 10
# Muestre su tabla de multiplicar del 1 al 12

number = int(input("Enter a number between 1 and 10: "))
counter = 1
while counter <= 12:
    result = number * counter
    print(f"{number} x {counter} = {result}")
    counter += 1    

