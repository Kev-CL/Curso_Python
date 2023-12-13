class Pajaro:
    # Atributo de clase. Son los atributos que pertenecerán siempre a la clase
    alas = True

    # Atributos de instancias
    def __init__(self,color,especie):
        self.color = color
        self.especie = especie

mi_pajaro = Pajaro('verde','perico')
mi_pajaro2 = Pajaro('amarillo','tucan')

print(f"Mi primer pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}")


