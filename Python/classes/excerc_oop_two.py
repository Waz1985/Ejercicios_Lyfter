class Person:
    def __init__(self, name):
        self.name = name

class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, person):
        if not isinstance(person, Person):
            print("Only Person objects can enter the bus.")
            return
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"{person.name} is in the bus.")
        else:
            print("The bus is full.")

    def remove_passenger(self):
        if len(self.passengers) >= 1:
            self.passengers.pop()
            print("One person left the bus.")
        else:
            print("The Bus is empty.")

bus = Bus(2)
p1 = Person("Ana")
p2 = Person("Luis")
p3 = Person("Maria")

bus.add_passenger(p1)
bus.add_passenger(p2)
bus.add_passenger("person")

bus.remove_passenger()
bus.remove_passenger()
bus.remove_passenger()
