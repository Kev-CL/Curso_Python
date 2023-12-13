"""Lectura de archivos del ordenador.
Este archivo de prueba esta almacenado en la misca carpeta del
programa.
1. Primero abrimos el archivo
* Es importante que el archivo se cierre por cuestiones de memoria
del ordenador.
"""

mi_archivo = open('Prueba.txt') # Abriendo archivo

#print(mi_archivo.read()) # Leyendo todo el archivo con .read y print

#print(mi_archivo.readline())# Leyendo solo una linea
#print(mi_archivo.readline().rstrip())# Leyendo solo una linea sin salto de linea

# Se pueden usar los metodos de los string
#print(mi_archivo.readline().rstrip().upper())# Mayuscula

# Se puede iterar
#for linea in mi_archivo:
#    print("Aqui dice: " + linea)

# Se puede haceer una lista del contenido del archivo
todas = mi_archivo.readlines() # Lista
todas = todas.pop() # Eliminando ultima
print(todas)

mi_archivo.close() # cerrando archivo