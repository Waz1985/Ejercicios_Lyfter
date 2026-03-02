from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

    def describe(self):
        return f"My name is {self.name} and I am a {self.__class__.__name__}"

class Dog(Animal):
    def make_sound(self):
        return "Woof"

class Cat(Animal):
    def make_sound(self):
        return "Meow"
    


animals = [
    Dog("Rex"),
    Cat("Mishi"),
    Dog("Rocky")
]

for animal in animals:
    print(animal.describe(), "-", animal.make_sound())