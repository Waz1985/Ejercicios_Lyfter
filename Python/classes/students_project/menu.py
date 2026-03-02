from actions import StudentManager
from data import CSVHandler
from student import Student


class Menu: 
    def __init__(self, manager: StudentManager, csv_handler: CSVHandler):
        self.manager = manager
        self.csv_handler = csv_handler

    def start(self):
        while True:
            self.show_options()
            option = input("Choose an option: ").strip()

            if not self.is_valid_option(option):
                print("Invalid option. Try again.")
                continue

            if option == "7":
                print("Goodbye!")
                break

            self.handle_option(option)

    
    def show_options(self):
        print("\n--- STUDENT MANAGEMENT SYSTEM ---")
        print("1. Add student")
        print("2. Show all students")
        print("3. Show top 3 students")
        print("4. Show general average")
        print("5. Export data to CSV")
        print("6. Import data from CSV")
        print("7. Exit")


    def is_valid_option(self, option: str) -> bool:
        return option in {"1", "2", "3", "4", "5", "6", "7"}
    

    def handle_option(self, option: str):
        if option == "1":
            self.add_student_flow()

        elif option == "2":
            self.show_students_flow()

        elif option == "3":
            self.show_top_students_flow()

        elif option == "4":
            self.show_general_average_flow()

        elif option == "5":
            self.export_flow()

        elif option == "6":
            self.import_flow()
    

    def add_student_flow(self):
        name = input("Full name: ").strip()

        while not StudentManager.is_valid_name(name):
            name = input("Invalid name. Try again: ").strip()

        section = input("Section (example: 11B): ").strip()

        while not StudentManager.is_valid_section(section):
            section = input("Invalid section. Try again: ").strip()

        spanish = self.ask_grade("Spanish")
        english = self.ask_grade("English")
        socials = self.ask_grade("Social Studies")
        science = self.ask_grade("Science")

        student = Student(name, section, spanish, english, socials, science)

        if not self.manager.add_student(student):
            print("Student already exists.")
        else:
            print("Student added successfully.")


    def ask_grade(self, subject: str) -> float:
        while True:
            try:
                grade = float(input(f"{subject} grade: "))
                if StudentManager.is_valid_grade(grade):
                    return grade
                print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid number.")

    
    def show_students_flow(self):
        students = self.manager.get_all_students()

        if not students:
            print("No students registered.")
            return

        for s in students:
            print(f"{s.name} | {s.section} | Avg: {s.average():.2f}")

    
    def show_top_students_flow(self):
        top = self.manager.get_top_students()

        if not top:
            print("No students available.")
            return

        for s in top:
            print(f"{s.name} | {s.section} | Avg: {s.average():.2f}")


    def show_general_average_flow(self):
        avg = self.manager.get_general_average()
        print(f"General average: {avg:.2f}")


    def export_flow(self):
        self.csv_handler.export_students(self.manager.get_all_students())
        print("Data exported successfully.")


    def import_flow(self):
        try:
            students = self.csv_handler.import_students()
            self.manager.students = students
            print("Data imported successfully.")
        except FileNotFoundError:
            print("No CSV file found. Export data first.")
