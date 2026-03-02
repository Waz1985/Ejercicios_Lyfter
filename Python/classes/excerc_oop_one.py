import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        try:
            if(self.radius <= 1):
                print("Error: you must use a number greater than 0")
            else:
                return math.pi * (self.radius ** 2)
        except TypeError:
            print(f"Error:You must use a positive number to make the operation") 


myCircle = Circle(-87)

print(myCircle.get_area())
