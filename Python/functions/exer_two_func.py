# Experimente con el concepto de scope:
# Intente accesar a una variable definida dentro de una función desde afuera.
# Intente accesar a una variable global desde una función y cambiar su valor.
global_var = "I am global"

def func():
    global_var = "I am modified Global"
    local_var = "I am local"
    print(global_var)
    print(local_var)

func()
print(local_var) # this will raise an error # trying to access local variable from outside