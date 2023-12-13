from random import choice

def palabra_al_azar():
    palabras = ["Cartel","Sol","tres"]
    return choice(palabras)

def inicializando_juego(palabra):
    longitud = len(palabra)
    lista_lineas = []
    print(f"La palabra cuenta con {longitud} letras. ¿Cúal será?:\n")
    for letra in range(longitud):
        lista_lineas.append("_")
    for lineas in lista_lineas:
        print(lineas,end=" ")
    print("\n")
    return lista_lineas

def pregunta_letra():
    letra = input("Elige una letra: ")
    return letra.lower()

def validar_letra(letra,palabra):
    palabra_min = palabra.lower()
    palabra.count(letra)

    return letra in palabra_min

def chequear_respuesta(letra,palabra,validacion,lista_lineas,vidas,letras_correctas):

    existe_letralist = letra in lista_lineas

    if validacion == True:
        if existe_letralist==False:
            print("¡Acertaste!.\n")
            letras_correctas.append(letra)
            lista_lineas=guiones_palabra_actualizada(letra,palabra,lista_lineas)
            for lineas in lista_lineas:
                print(lineas, end=" ")
            print("\n")
            return lista_lineas,letras_correctas, vidas
        else:
            print("Esta letra ya la has ingresado. Elige otra.\n")
            return lista_lineas,letras_correctas, vidas
    else:
        vidas = resta_vidas(vidas)
        print(f"La letra '{letra}' no está dentro de la palabra. Te quedan {vidas} vidas.\n")
        return lista_lineas,letras_correctas, vidas

def guiones_palabra_actualizada(letra,palabra,lista_lineas):
    palabra=palabra.lower()
    lista_lineas[palabra.index(letra)]=letra
    return lista_lineas


def resta_vidas(vidas):
    return vidas-1

print("\nEste es el juego de Ahorcado. adivina la palabra...\n")
vidas = 5
letras_correctas = []
ban = False

palabra=palabra_al_azar()
print(palabra)

lista_lineas=inicializando_juego(palabra)

while vidas >= 0:
    letra=pregunta_letra()
    validacion=validar_letra(letra,palabra)
    lista_lineas,letras_correctas,vidas = chequear_respuesta(letra,palabra,validacion,lista_lineas,vidas,letras_correctas)
    if len(palabra) == len(letras_correctas):
        print("¡Felicidades! Has ganado.")
        break
    if vidas == 0:
        print("Has perdido, trata de nuevo.")
        break


