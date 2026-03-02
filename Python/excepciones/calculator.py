def menu_operation(actual_number):
    print(f"Your actual number is: {actual_number}")
    print("Operations Menu:")
    print("1 = Sum" \
    " / 2 = Rest" \
    " / 3 = Multiplication" \
    " / 4 = Division" \
    " / 5 = Borrar resultado")

def start_operation():
    try:
        try:
            actual_number = float(input("Please enter a number: "))
            menu_operation(actual_number)
        except ValueError as e:
            print(f"Error [ValueError]: The entered value is not a number. Details: {e}")
            print("Please enter just numbers")
            actual_number = float(input("Please enter a number: "))
            menu_operation(actual_number)
        try:
            operation = int(input("Enter the number of operation you need: " ))
            if (operation == 5):
                actual_number = 0
                print(f"Your operation has been cleared")
                start_operation()
        except ValueError as e:
            print(f"Error [ValueError]: The entered value is not a number. Details: {e}")
            print("Please enter just numbers")
            operation = int(input("Enter the number of operation you need: " ))    
        try:
            second_number = float(input("Please enter the second number: "))
        except ValueError as e:
            print(f"Error [ValueError]: The entered value is not a number. Details: {e}")
            print("Please enter just numbers") 
            second_number = float(input("Please enter the second number: "))
    except Exception as e:
        print(f"ERROR: Please contact support {e}")

    if(operation == 1):
        actual_number = actual_number + second_number
        print(f"The result of your sum is: {actual_number}")
    elif(operation == 2):
        actual_number = actual_number - second_number
        print(f"The result of your rest is: {actual_number}")
    elif(operation == 3):
        actual_number = actual_number * second_number
        print(f"The result of your multiplication is: {actual_number}")
    elif(operation == 4):
        actual_number = actual_number / second_number
        print(f"The result of your division is: {actual_number}")        
    else:
        actual_number = float(input("Please enter a number: "))
        menu_operation(actual_number)
        operation = int(input("Enter the number of operation you need: " ))
        second_number = float(input("Please enter the second number: "))

start_operation()