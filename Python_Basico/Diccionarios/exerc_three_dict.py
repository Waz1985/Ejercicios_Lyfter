# Cree un programa que use una lista para eliminar keys de un diccionario.
# Ejemplos:
list_of_keys = ['access_level', 'age']
employee = {'name': 'John', 'email': 'john@ecorp.com', 'access_level': 5, 'age': 28}

for key in list_of_keys:
    if key in employee:
        employee.pop(key)

print(employee)