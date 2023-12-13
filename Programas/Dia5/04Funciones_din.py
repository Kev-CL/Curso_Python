def todos_positivos(lista):
    for n in lista:
        if n < 0:
            return False
        else:
            pass
    return True


lista_numeros = [1, 2, 3, 4, 5]
print(todos_positivos(lista_numeros))


def suma_menores(lista_numeros):
    suma = 0
    for n in lista_numeros:
        if n in range(0, 1000):
            suma = suma + n
        else:
            pass
    return suma

lista_numeros = [1, 2, 3, 4, 5]