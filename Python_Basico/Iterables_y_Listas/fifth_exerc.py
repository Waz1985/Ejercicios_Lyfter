# Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, 
# seguido del numero ingresado más alto.
user_numbers = []
while len(user_numbers) < 10:
    user_number = int(input("Enter a number: "))
    user_numbers.append(user_number)
print(f"The numbers you entered are: {user_numbers}")
highest = max(user_numbers)
print(f"The highest number is: {highest}")