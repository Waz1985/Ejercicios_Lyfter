import random

secret_number = random.randint(1, 10)
user_number = int(input("Guess the secret number between 1 and 10. Enter your number: "))

while user_number != secret_number:
    print(f"The number {user_number} you entered is incorrect, please enter another number between 1 and 10: ")
    user_number = int(input())
print(f"Congratulations! You have guessed the secret number {secret_number}.")
