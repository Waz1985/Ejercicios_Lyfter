class Student:
    def __init__(self, name):
        self.name = name
        self._grades = []

    def add_grade(self, grade):
        if not isinstance(grade, (int, float)):
            return False
        if grade < 0 or grade > 100:
            return False

        self._grades.append(grade)
        return True

    def average(self):
        if not self._grades:
            return 0.0
        else:
            return sum(self._grades) / len(self._grades)


s = Student("Ana")
s.add_grade(80)
s.add_grade(90)
s.add_grade(1000)

print(s._grades)
print(s.average())