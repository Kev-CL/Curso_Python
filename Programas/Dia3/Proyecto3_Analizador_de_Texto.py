# 1. Cuántas veces las letras aparecen en el resultado (Contando mayusculas
#   y minusculas).
# 2. Cuántas palabras hay en total.
# 3. Primer y última letra.
# 4. Palabras en orden inverso.
# 5. Aparece Python en el texto?.


# Ingresando texto y letra, convirtiendolo todo en minúsculas.


texto = input("Ingresa el texto a analizar:\n")

texto_min = texto.lower()

letra1 = input("\nIngresa la primer letra a evaluar: ")
letra2 = input("Ingresa la segunda letra a evaluar: ")
letra3 = input("Ingresa la tercera letra a evaluar: ")

# Primer ejercicio.
print(f"\nEl número de veces que aparece la letra {letra1} en el texto es : {texto_min.count(letra1.lower())}")
print(f"El número de veces que aparece la letra {letra2} en el texto es : {texto_min.count(letra2.lower())}")
print(f"El número de veces que aparece la letra {letra3} en el texto es : {texto_min.count(letra3.lower())}")
# Segundo ejercicio
lista_texto = texto.split()
print(f"\nEl número de palabras del texto es: {len(lista_texto)}")
# Tercer ejercicio
print(f'\nLa primer letra del texto es: "{texto[0]}"')
print(f'La ultima letra del texto es: "{texto[-1]}"')
#Cuarto ejercicio
lista_textoNormal = texto.split()
lista_textoNormal.reverse()
print("\nEl texto al revés queda:\n")
print(" " .join(lista_textoNormal))

# Primer forma
"""#Quinto ejercicio
evaluando = texto.find("python")

if evaluando == -1:
    print("\nLa palabra python NO existe en el texto.")
else:
    print("\nLa palabra python SI existe en el texto.")
"""

# Segunda forma
evaluando = 'python' in texto
dic = {True:'SI', False: 'NO'}
print(f"\nLa palabra python {dic[evaluando]} existe en el texto.")
