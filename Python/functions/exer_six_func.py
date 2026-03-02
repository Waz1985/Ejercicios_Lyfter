# Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
# Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
# “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”
# print(list("python-variable-funcion-computadora-monitor"))

def order_string(my_string):
    if not isinstance(my_string, str):
        raise TypeError("Parameter must be a String")
    str_to_list = list(my_string)
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

print(order_string("python-variable-function-computer-monitor-keyboard"))  # Output: computadora-funcion-monitor-python-variable