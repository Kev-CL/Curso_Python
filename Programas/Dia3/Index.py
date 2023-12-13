mi_texto = "Esta es una prueba"
print(mi_texto[5])

resultado = mi_texto.index("n") # Busqueda de letras
print(resultado)

resultado = mi_texto.index("e") # Sensible a mayúsculas
print(resultado)
resultado = mi_texto.index("E")
print(resultado)

resultado = mi_texto.index("prueba") # Detecta palabras
print(resultado)

resultado = mi_texto.index("a") # indica la pos. de la primer letra que encuentra
print(resultado)

resultado = mi_texto.index("a",4,11) # Con límites para la busqueda
print(resultado)

resultado = mi_texto.rindex("a") # Buesqueda al revés. Indica la pos. de la primer letra que encuentra
print(resultado)

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.index("práctica"))