# No se repetiran los valores
# No tienen un indice u orde.
# No se pueden incluir ni listas ni diccionarios.
# No se pueden modificar (Asignación de items)

mi_set = set([1,2,3,4,5,6,6])
mi_set2 = {1,2,3,4,5,6,7,8,9}

# Primer forma
print(type(mi_set))
print(mi_set)
#Segunda forma
print(type(mi_set2))
print(mi_set2)

print(2 in mi_set)

# Unión de elementos

mi_set3 = mi_set.union(mi_set2)
print(len(mi_set3))
print(mi_set3)

#Agregar
mi_set3.add(10)
print(mi_set3)

mi_set3.remove(10) # Si no existe marcará error
print(mi_set3)
mi_set3.discard(10) # Si no existe NO marcará error
print(mi_set3)