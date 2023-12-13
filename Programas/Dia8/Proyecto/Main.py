import GenDec

def inicio():
    opciones()
    opc = eleccion()
    if opc == 'x':
        return False
    else:
        GenDec.decorar(opc)

def opciones():
    print("""Elija el área al que desea ingresar:
    P) Perfumes.
    F) Farmacia.
    C) Cosmetica.
    X) Salir.""")

def eleccion():
    opc = 'o'
    opciones = ['p', 'f', 'c', 'x']
    while opc not in opciones:
        opc = input("opción: ").lower()
    return opc

band = True
while not band == False:
    band = inicio()