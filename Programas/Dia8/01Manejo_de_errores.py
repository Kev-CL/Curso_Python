def suma():
    n1 = int(input("Ingresa n1: "))
    n2 = int(input("Ingresa n1: "))
    print(n1+n2)


try:
    # Código que queremos probar
    suma()
except ValueError:
    # Código a ejecutar si hay error
    print("Algo no ha salido bien. Ingresaste caraceters en lugar de numeros.")
else:
    # Código a ejecutar si hay error
    print("Funcionó correctamente")
finally:
    # Código a ejecutar aunque exista error
    print("Final de nuestro programa con o sin errores.")
