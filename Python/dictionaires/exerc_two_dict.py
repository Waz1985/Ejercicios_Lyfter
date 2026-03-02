# Cree un programa que cree un diccionario usando dos listas del mismo tamaño, 
# usando una para sus keys, y la otra para sus values.
list_a = ['first_name', 'last_name', 'role']
list_b = ['Alek', 'Castillo', 'Software Engineer']
my_dict = {}
for key in list_a:
    value = list_b[list_a.index(key)]
    my_dict[key] = value
print(my_dict)  