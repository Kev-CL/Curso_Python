class Pajaro:
    # Atributo de clase. Son los atributos que pertenecerán siempre a la clase
    alas = True

    # Atributos de instancias
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    # Metods de instancia
    def piar(self):
        print(f'pio. Mi color es {self.color}')
    def volar(self, metros):
        print(f'El pajaro ha volado una cantidad de {metros} metros.')

    # En los metodos de instancia, se pueden:
    # 1. acceder y modificar los atributos de instancia.
    # 2. acceder a otros metodos.
    # 3. modificar el estado/atributo de la clase
    def pintar_negro(self):
        self.color = 'negro'
        print(f'Ahora el pajaro es de color {self.color}')
        self.piar()

    # Metodos de clase
    # Los decoradores inician con un '@'. No necesitan instanciar para ser llamados.
    # Pero no pueden acceder o modificar a los atributos de instancia pero si a los
    # de la clase.
    @classmethod
    def poner_huevos(cls,cantidad):
        print(f'Un pajaro pone {cantidad} huevos.')

    # Métodos de clase estáticos
    # No puede modificar ni variables de instancia ni de clase.
    # Sirven para asegurar que no se modifiquen a tus objetos
    @staticmethod
    def mirar():
        print('El pajaro mira.')


piolin = Pajaro('amarillo', 'canario')
piolin.piar()
piolin.volar(17)
piolin.pintar_negro()
piolin.piar()

# Metodos de clase
Pajaro.poner_huevos(15)

class Jugador:
    vivo = False
    @classmethod
    def revivir(cls):
        Jugador.vivo = True