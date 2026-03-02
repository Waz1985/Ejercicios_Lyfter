# Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
# Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
# “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

print(list("python-variable-funcion-computadora-monitor"))

def order_string(str):
    str_to_list = list(str)
    word = ""
    ordered_list = []
    for i, char in enumerate(str_to_list):
        if char != '-':
            word += char
            if i == len(str_to_list) - 1:
                ordered_list.append(word) 
        else:
            ordered_list.append(word)
            word = ""
    ordered_list.sort()
    ordered_string = "-".join(ordered_list)
    return ordered_string

print(order_string("python-variable-funcion-computadora-monitor"))  # Output: computadora-funcion-monitor-python-variable