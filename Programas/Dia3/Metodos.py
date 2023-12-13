#Otros métodos ya vistos:
# .format()
# Index[]
#
textoA = "este es el texto a"
textoB = "ESTE ES EL TEXTO B"

#Mayúsculas(upper()) y minúsculas(lower())
resultado = textoA.upper()
print(resultado)
resultado = textoA[2].upper()

print(resultado)
resultado = textoB.lower()
print(resultado)
resultado = textoB[2].lower()
print(resultado)

#Listas (split())
resultado = textoA.split() # Espacio como separador
print(resultado)

resultado = textoA.split("t") # "t" como separador
print(resultado)

#Unión (join())
a = "Aprendiendo"
b = "a"
c = "programar"
d = "Python"
e = " ".join([a,b,c,d]) #Se unen con un espacio
print(e)

lista_palabras = ["La","legibilidad","cuenta."]
print(" ".join(lista_palabras))

#find (find())
# Funciona igual que index(), la diferencia es que si la letra o palabra
# no existe el resultado que arroja es -1.
resultado = textoA.find("t",1,5) # "t" como separador
print(resultado)

# replace()
resultado = textoA.replace("e","x")
print(resultado)