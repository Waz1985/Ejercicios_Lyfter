import csv
import os
from typing import List
from student import Student 

FILENAME = "students.csv"

class CSVHandler:
    def __init__(self, filename: str = "students.csv"):
        self.filename = filename
    
    def file_exists(self):
        return os.path.exists(self.filename)
    
    def export_students(self, students: list[Student]):
        with open(self.filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "section", "spanish", "english", "socials", "science"])

            for student in students:
                writer.writerow([
                    student.name,
                    student.section,
                    student.spanish,
                    student.english,
                    student.socials,
                    student.science,
                ])


    def import_students(self) -> List[Student]:
        if not self.file_exists():
            raise FileNotFoundError("CSV file does not exist")

        students = []
        with open(self.filename, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                student = Student(
                    name= row["name"],
                    section= row["section"],
                    spanish= float(row["spanish"]),
                    english= float(row["english"]),
                    socials= float(row["socials"]),
                    science= float(row["science"]),
                )
                students.append(student)

        return students