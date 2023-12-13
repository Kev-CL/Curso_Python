class Animal:
    def __init__(self,tamano,color):
        self.tamano = tamano
        self. color = color

    def nacer(self):
        print(f"El animal ha nacido. Es de color {self.color} y mide {self.tamano} cm.")

    def hablar(self):
        print("Este aniaml emite un sonido")

class Pajaro(Animal):

    def __init__(self,tamano,color,altura_vuelo):
        super().__init__(tamano,color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print(f"PIO!... Soy de color {self.color} y mido {self.tamano} cm. Llego a volar {self.altura_vuelo} m.")


piolin = Pajaro(13,'amarillo',15)
piolin.hablar()

