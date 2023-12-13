# Ejecuta metodos con el mismo nombre, pero pueden interactuar diferente
class Vaca:
    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + 'dice muu')

class Oveja:
    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + 'dice bee')

vaca1 = Vaca('Aurora')
oveja1 = Oveja('Bee')

animales = [vaca1,oveja1]
for animal in animales:
    animal.hablar()


class Mago():
    def atacar(self):
        print("Ataque mágico")


class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")


class Samurai():
    def atacar(self):
        print("Ataque con katana")


mago1 = Mago()
arquero1 = Arquero()
samurai1 = Samurai()

personajes = [mago1, arquero1, samurai1]

for personaje in personajes:
    personaje.atacar()