#Cree un pseudocódigo que le pida un precio de producto al usuario, calcule su descuento y muestre el precio final tomando en cuenta que:
#Si el precio es menor a 100, el descuento es del 2%.
#Si el precio es mayor o igual a 100, el descuento es del 10%.
#Ejemplos:
#120 → 108
#40 → 39.2
price = float(input("Enter product price: "))
discount = 0

if price < 100:
    discount = 0.02
elif price >= 100:
    discount = 0.10

print(f"Final price: {price * (1 - discount)}")


#Cree un pseudocódigo que le pida un tiempo en segundos al usuario y calcule si es menor o mayor a 10 minutos. Si es menor, 
#muestre cuantos segundos faltarían para llegar a 10 minutos. Si es mayor, muestre “Mayor”. 
#Si es exactamente igual, muestre “Igual”.
#1040 → Mayor
#140 → 460
#600 → Igual
#599 → 1

time_seconds = int(input("Enter time in seconds: "))
if time_seconds < 600:
    print(f"Seconds remaining to reach 10 minutes: {600 - time_seconds}")
elif time_seconds > 600:
    print("Greater")
else:
    print("Equal")  


#Cree un algoritmo que le pida un numero al usuario, y realice una suma de cada numero del 1 hasta ese número ingresado. Luego muestre el resultado de la suma.
#5 → 15 (1 + 2 + 3 + 4 + 5)
#3 → 6 (1 + 2 + 3)
#12 → 78 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12)

number = int(input("Enter a number: "))
sum_result = 0
counter = 1
while counter <= number:
    sum_result += counter
    counter += 1
print(f"Sum result: {sum_result}")  
