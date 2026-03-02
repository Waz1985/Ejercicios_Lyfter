#Pida al usuario ingresar una temperatura en Celsius
#Conviértala a Fahrenheit y Kelvin
#Muestre los tres valores
#Entrada:
#"Ingrese temperatura en Celsius:"25
#Salida:
#Fahrenheit:77.0
#Kelvin:298.15

celsius_temp = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius_temp * 9/5) + 32
kelvin = celsius_temp + 273.15
print(f"Temperature in Celsius: {celsius_temp}")
print(f"Fahrenheit: {fahrenheit}")
print(f"Kelvin: {kelvin}")  




