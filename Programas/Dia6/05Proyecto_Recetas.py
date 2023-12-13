# crsplpz-R3D*m0d3mpw
#LIBRERIAS
#********************************************
import os
from pathlib import Path
from os import system

# FUNCIONES
#********************************************
def saludo_inicial():
    print("*" * 80)
    print("\t" * 2 + "Bienvenido. Este es un programa de las recetas\n"
          + "\t" * 3 + "almacenadas en su equipo.\n"
          + "\t" * 1 + "la dirección de la carpeta de recetas en su ordenador es:\n"
          + "\t" * 3 + f"{direccion_carpeta()}")
    print("*" * 80 + "\n")


def direccion_carpeta():
    base = Path.home()
    ruta = Path(base, 'Recetas')
    return ruta


def lista_categorias():
    ruta = direccion_carpeta()
    return os.listdir(ruta)


def direccion_categoria(pos_categoria):
    categoria_elegida = lista_categorias()[pos_categoria]
    return Path(direccion_carpeta(), categoria_elegida)


def mostrar_categorias():
    pos = 0
    for categoria in lista_categorias():
        print(f"{pos+1}. {categoria}")
        pos += 1

def lista_recetas(pos_categoria):
    ruta = direccion_categoria(pos_categoria)
    return os.listdir(ruta)


def mostrar_recetas(pos_categoria):
    pos = 0
    for receta in lista_recetas(pos_categoria):
        print(f"{pos + 1}. {receta[:-4]}")
        pos += 1


def direccion_receta(pos_categoria,pos_receta):
    receta_elegida = lista_recetas(pos_categoria)[pos_receta]
    return Path(direccion_categoria(pos_categoria),receta_elegida)


def mostrar_todas_recetas():
    pos = 0
    pos2 = 0
    print("*" * 80)
    print("Recetas registradas:\n")
    for categoria in lista_categorias():
        print(categoria)
        for receta in lista_recetas(pos2):
            print(f"\t* {receta[:-4]}")
        pos2 += 1
    pos += 1
    print("*" * 80 + "\n")

def opciones():

    lista_opciones = ['Leer receta','Crear receta','Crear categoría','Eliminar receta',
                'Eliminar categoría','Finalizar programa']
    pos = 0

    for opc in lista_opciones:
        print(f"{pos+1}. {opc}")
        pos += 1
    return lista_opciones

def validar_respuestaOPC(lista):
    opc = int(input('Opción: '))
    if opc not in range(1,len(lista)+1):
        return opc, False
    else:
        return opc, True

def opciones_categorias():
    validar = False

    system('cls')
    print("\n" + "*" * 80
          + "\t" * 4 + "LEER RECETA\n"
          + "*" * 80 + "\n")

    while validar == False:
        print("A continuación elige una categoria:\n")
        mostrar_categorias()
        lista_cat = lista_categorias()
        opc, validar = validar_respuestaOPC(lista_cat)
        if validar == False:
            system('cls')
            print("Tú repuesta no está dentro de los parametros de las opciones.\n"
                  "Por favor, verifica tu respuesta e ingresala nuevamente. Recuerda\n"
                  f"que solo se aceptan valores númericos y solo son {len(lista_cat)} opciones.\n")
    if validar == True:
        return opc

def opciones_recetas(categoria):
    validar = False

    system('cls')
    print("\n" + "*" * 80
          + "\t" * 4 + "LEER RECETA\n"
          + "*" * 80 + "\n")

    while validar == False:
        print("A continuación elige la receta a leer:\n")
        mostrar_recetas(categoria)
        lista_rece = lista_recetas(categoria)
        opc, validar = validar_respuestaOPC(lista_rece)
        if validar == False:
            system('cls')
            print("Tú repuesta no está dentro de los parametros de las opciones.\n"
                  "Por favor, verifica tu respuesta e ingresala nuevamente. Recuerda\n"
                  f"que solo se aceptan valores númericos y solo son {len(lista_rece)} opciones.\n")
    if validar == True:
        return opc

def leer_receta(categoria,receta):
    ruta = direccion_receta(categoria,receta)
    archivo = open(ruta, 'r')
    print(archivo.read())
    archivo.close()
#************************************************************************
opc = 0  # Variable para la opción recibida
validar = False  # Validación de la respuesta

while opc != 6:
    saludo_inicial()
    mostrar_todas_recetas()

    while validar == False:
        print("A continuación elige una opción:\n")
        lista_opciones = opciones()
        opc, validar = validar_respuestaOPC(lista_opciones)
        if validar == False:
            system('cls')
            print("Tú repuesta no está dentro de los parametros de las opciones.\n"
                  "Por favor, verifica tu respuesta e ingresala nuevamente. Recuerda\n"
                  f"que solo se aceptan valores númericos y solo son {len(lista_opciones)} opciones.\n")
    if opc == 1:
        cat = opciones_categorias()
        receta = opciones_recetas(cat-1)
        leer_receta(cat-1,receta-1)
        input("")
    elif opc == 2:
        pass
    elif opc == 3:
        pass
    elif opc == 4:
        pass
    elif opc == 5:
        pass
    validar = False
