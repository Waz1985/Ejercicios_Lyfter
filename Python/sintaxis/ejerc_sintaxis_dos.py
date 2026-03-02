name = input("Enter your name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
def show_life_stage(age):
    if age < 0:
        return "Invalid age"
    elif age <= 2:
        return "Baby"
    elif age <= 11:
        return "Child"
    elif age <= 15:
        return "Preteen"
    elif age <= 19:
        return "Teenager"
    elif age <= 25:
        return "Young Adult"
    elif age <= 65:
        return "Adult"
    else:
        return "Senior Adult"
print(f"You are a {show_life_stage(age)}")
