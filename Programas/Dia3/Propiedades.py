# Propiedades de los strings, o de las cadenas:
# Inmutables (no puedes cambiar el contenido de un string
#   si se puede cambiar el contenido de la variable pero no
#   modificar la cadena contenida en el string).

#Multiplicación

texto = "casa"
print(texto*5)

# Saltos de linea
poema = """Mil pequeños peces blancos
como si hirviera
el color del agua"""
print(poema)

# Contenido
print("peces" in poema)
print("sol" in poema)

print("peces" not in poema)
print("sol" not in poema)

#Longitud
print(len(poema))