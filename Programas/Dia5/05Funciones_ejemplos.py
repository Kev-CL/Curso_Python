from random import *
def lanzar_dados():
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    return dado1,dado2

def evaluar_jugada(dado1,dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

dado1,dado2 = lanzar_dados()
resultado = evaluar_jugada(dado1,dado2)
print(resultado)

##2
lista_numeros = [1,2,15,7,2]

def reducir_lista(lista_numeros):
    lista_reducida = list(set(lista_numeros))
    lista_reducida.sort()
    lista_reducida.pop(-1)
    return lista_reducida

def promedio(lista_reducida):
    suma = 0
    for numero in lista_reducida:
        suma = numero + suma
    return suma/len(lista_reducida)

list1 = reducir_lista(lista_numeros)
prom = promedio(list1)
print(prom)

##3
def lanzar_moneda():
    return choice(["Cara", "Cruz"])

def probar_suerte(moneda,lista_numeros):
    if moneda == 'Cara':
        mensaje = "La lista se autodestruirá"
        lista_numeros.clear()
    else:
        mensaje = "La lista fue salvada"
    return mensaje,lista_numeros

moneda = lanzar_moneda()
mensaje,lista = probar_suerte(moneda,[1,2,3,4,5,6])
print(mensaje)
print(lista)