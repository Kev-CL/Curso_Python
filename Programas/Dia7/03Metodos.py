class Pajaro:
    # Atributo de clase. Son los atributos que pertenecerán siempre a la clase
    alas = True

    # Atributos de instancias
    def __init__(self,color,especie):
        self.color = color
        self.especie = especie

    # Metods de instancia
    def piar(self):
        print(f'pio. Mi color es {self.color}')
    def volar(self,metros):
        print(f'El pajaro ha volado una cantidad de {metros} metros.')

piolin = Pajaro('amarillo','canario')
piolin.piar()
piolin.volar(17)
