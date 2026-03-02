from abc import ABC, abstractmethod
import math 

class Shape(ABC):
    
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number") 
        if radius <= 0:
            raise ValueError("Radius must be greater than 0")
        self.radius = radius
        
    def calculate_area(self):
        return ((math.pi * self.radius ** 2))
    
    def calculate_perimeter(self):
        return ( 2 * math.pi * self.radius)
    
class Rectangle(Shape):
    def __init__(self, width, height):
        if not isinstance(width, (int, float)):
            raise TypeError("Width must be a number") 
        if not isinstance(height, (int, float)):
            raise TypeError("Height must be a number") 
        if width <= 0:
            raise ValueError("Width must be gra=eater than 0")
        if height <= 0:
            raise ValueError("height must be gra=eater than 0")
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height
    
    def calculate_perimeter(self):
        return 2*(self.width + self.height)
    
shapes = [
    Circle(10),
    Rectangle(4, 5),
    Circle(3)
]

for shape in shapes:
    print(shape.calculate_perimeter())