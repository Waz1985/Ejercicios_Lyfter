class Student:
    def __init__(self, name, section, spanish, english, socials, science):
        self.name = name
        self.section = section
        self.spanish = spanish
        self.english = english
        self.socials = socials
        self.science = science

    def average(self) -> float:
        return (self.spanish + self.english + self.socials + self.science) / 4
    
    