# Se emplean para el cuidado de memoria. A medida que
# se pida una respuesta, el programa la irá generando.

def mi_funcion():
    return 4

def mi_generador():
    yield 4

print(mi_funcion())
print(mi_generador())

g = mi_generador()

print(next(g))

def mi_funcion2():
    lista = []
    for x in range(1,5):
        lista.append(x * 10)
    return lista

def mi_generador2():
    for x in range(1,5):
        yield x * 10

print(mi_funcion2())
print(mi_generador2())

g = mi_generador2()

print(next(g))
print(next(g))
print(next(g))
print(next(g))

def funcion():
    num=0
    while True:
        num += 1
        yield num

generador = funcion()

print(next(generador))
print(next(generador))


def juego():
    vidas = 4
    while True:
        vidas -= 1
        if vidas > 1:
            yield f"Te quedan {vidas} vidas"
        elif vidas == 1:
            yield f"Te queda {vidas} vida"
        elif vidas == 0:
            yield "Game Over"


perder_vida = juego()
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))