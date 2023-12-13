#A diferencia de las listas, los diccionarios no tiene un orden asignado
diccionario = {
    'c1':'valor 1',
    'c2': 345.234,
    'c3': False,
    'c4': [3,4,5],
    'c5': {
        'c51': 33,
        'c52': 'segundo diccionario',
        'c53': True
        }

}
print(type(diccionario))

# Consulta
print(diccionario)
print(diccionario["c1"])
print(diccionario["c2"])
print(diccionario["c3"])
print(diccionario["c4"][1])
print(diccionario["c5"]['c52'])

diccionario['c6'] = 'nuevo'
print(diccionario)

diccionario['c1'] = 'modificado'
print(diccionario)

print(diccionario.keys()) #claves
print(diccionario.values()) #valores
print(diccionario.items()) #items

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict["puntos"]["points2"][2])