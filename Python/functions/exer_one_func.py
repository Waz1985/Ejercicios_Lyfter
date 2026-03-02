# Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.
def print_one():
    print("Hello")
    print_two()

    
    

def print_two():
    print("World")


print_one()