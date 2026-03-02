# Cree un programa que intercambie el primer y ultimo elemento de una lista. 
# Debe funcionar con listas de cualquier tamaño.
my_list = [4, 3, 6, 1, 7]
first_element = my_list.pop(0)
last_element = my_list.pop(-1)
my_list.insert(0, last_element)
my_list.append(first_element)
print(my_list)
