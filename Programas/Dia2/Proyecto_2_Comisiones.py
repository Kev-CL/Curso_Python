nombre=input("¿Cuál es tu nombre? ")
ventas=float(input("¿Cuánto fue el valor total de tus ventas? "))
print(f"\n¡Buen día {nombre}! Por el total de ventas que fue de ${round(ventas,2)}, tu comisión es de {round(ventas*13/100,2)}. Buen trabajo.")