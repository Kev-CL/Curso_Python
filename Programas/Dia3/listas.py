mi_lista = ["a","b","c"]
mi_lista_desorden = [5,3,2,6,84,2,4,7,4,4345,3,3334,0]

print(type(mi_lista))

# Cantidad de elementos
print(len(mi_lista))

# Indexar
print(mi_lista[0])

# Indexar con limites
print(mi_lista[0:2])

# Las propiedades que aplican para los String también aplican para las listas.

# Las propiedades que si se pueden aplicar en las listas son:

#Modificación de listas
mi_lista[1] = "modificado"

#Agregar datos
mi_lista.append("d")
print(mi_lista)

# Eliminar
eliminado = mi_lista.pop(2) #eliminando el elemento 2 y guardandolo en variable

print(mi_lista) #lista modificada
print(eliminado) #elemento eliminado

#Ordenando lista
mi_lista_desorden.sort()
print(mi_lista_desorden)

#invertir
mi_lista_desorden.reverse()
print(mi_lista_desorden)

mi_lista.clear()
print(mi_lista)