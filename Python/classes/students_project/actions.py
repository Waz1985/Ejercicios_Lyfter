from typing import List, Optional
from student import Student
import re

class StudentManager:
    def __init__(self):
        self.students: List[Student] = []

    def add_student(self, student: Student):
        if self.student_exists(student.name, student.section):
            print(f"Student {student.name} already exists.")
            return False
        self.students.append(student)
        return True
    
    def student_exists(self, name: str, section: str) -> bool:
        for s in self.students:
            if s.name == name and s.section == section:
                return True
        return False
    
    def get_all_students(self) -> List[Student]:
        return self.students
    
    def get_top_students(self, n: int = 3) -> List[Student]:
        return sorted(
            self.students, 
            key=lambda student: student.average(), 
            reverse=True
            )[:n]
    
    def get_general_average(self) -> float:
        if not self.students:
            return 0.0
        
        total = sum(student.average() for student in self.students)
        return total / len(self.students)
    
    def remove_student(self, name: str, section: str) -> bool:
        for student in self.students:
            if student.name == name and student.section == section:
                self.students.remove(student)
                return True
        return False
    
    def get_failed_students(self) -> List[Student]:
        failed = []

        for s in self.students:
            if(
                s.spanish < 60 or
                s.english < 60 or
                s.socials < 60 or
                s.science < 60
            ):
                failed.append(s)
        return failed
    

    @staticmethod
    def is_valid_name(name: str) -> bool:
        return bool(name.strip()) and not any(char.isdigit() for char in name)
    
    @staticmethod
    def is_valid_section(section: str) -> bool:
        return bool(re.match(r"^\d{2}[A-Z]$", section))

    @staticmethod
    def is_valid_grade(grade: float) -> bool:
        return 0 <= grade <= 100


manager = StudentManager()
student = Student("Ana Ruiz", "11B", 80, 90, 85, 88)

manager.add_student(student)
top = manager.get_top_students()
avg = manager.get_general_average()