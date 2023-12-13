#   *Son similares a las listas, pero ocupan menos memoria y ocupan parentesis
#       o también se pueden omitir en lugar de cortchetes.
#   *Pueden contener arreglos, listas, diccionarios y otros tuples.
#   *Se ubica mendiante indices a diferencia de los diccionarios y al igual que las
#       listas y arreglos.
#   *No pueden modificarse al igual que los strings
mi_tuple = (1,2,(1,3),3,4,5,1,1)

print(type(mi_tuple))
print(mi_tuple[2][1])

# Opciones nuevas que te da Tuple.
print(mi_tuple.count(1)) # número de veces que aparece el "1" en el tuple.

print(mi_tuple.index(2)) # En qué posición se encuentra el "2".

