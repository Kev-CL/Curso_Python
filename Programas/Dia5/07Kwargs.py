## Transforma lo recibido en un diccionario
#1
def lista_atributos(**kwargs):
    lista = []
    for arg in kwargs.values():
        lista.append(arg)
    return lista

#2
def describir_persona(nombre,**kwargs):
    print(f'Características de {nombre}:')
    for nom,valor in kwargs.items():
        print(f'{nom}: {valor}')


describir_persona("kevin",color_de_ojo='azul',color_de_pelo='cafe')
