# La herencia es la capacidad de heredar o conservar los atributos de otras
# clases, pudiendo ver y modificar.

class Animal:
    def __init__(self,tamano,color):
        self.tamano = tamano
        self. color = color

    def nacer(self):
        print(f"El animal ha nacido. Es de color {self.color} y mide {self.tamano} cm.")


class Pajaro(Animal):
    pass

piolin = Pajaro(13,'amarillo')
piolin.nacer()