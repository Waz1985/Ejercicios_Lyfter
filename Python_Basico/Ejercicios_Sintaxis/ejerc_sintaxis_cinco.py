grades_qty = int(input("¿How many grades do you want to enter?"))
approved_grades = 0
failed_grades = 0
grades_sum = 0
approved_grades_sum = 0
failed_grades_sum = 0
for i in range(grades_qty):
    nota = int(input(f"Please enter your grade number {i + 1}: "))
    if nota < 0 or nota > 100:
        print("Invalid grade. It must be between 0 and 100.")
    elif nota >= 70:
        approved_grades += 1
        grades_sum += nota
        approved_grades_sum += nota
    else:
        failed_grades += 1
        grades_sum += nota
        failed_grades_sum += nota
print(f"Number of approved grades: {approved_grades}")
print(f"Number of failed grades: {failed_grades}")
print(f"Average of all grades: {grades_sum / grades_qty}")
print(f"Average of approved grades: {approved_grades_sum / approved_grades if approved_grades > 0 else 0}")
print(f"Average of failed grades: {failed_grades_sum / failed_grades if failed_grades > 0 else 0}")