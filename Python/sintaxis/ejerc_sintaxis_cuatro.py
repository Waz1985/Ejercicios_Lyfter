num_one = int(input("Enter the first number: "))
num_two = int(input("Enter the second number: "))
num_three = int(input("Enter the third number: "))

if num_one >= num_two and num_one >= num_three:
    print(f"The first number {num_one} is the greatest")
elif num_two >= num_one and num_two >= num_three:
    print(f"The second number {num_two} is the greatest")
else:
    print(f"The third number {num_three} is the greatest")