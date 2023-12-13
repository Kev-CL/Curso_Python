from collections import Counter
from collections import defaultdict
from collections import namedtuple
from  collections import deque
#*************************************************
frase = 'al pan pan y al vino vino'
palabra = 'mississippi'
lista = [1,2,3,3,3,3,4,4,1,1,2,3,5]

print(Counter(frase.split()))
print(Counter(palabra))
print(Counter(lista))

serie = Counter(lista)

print(serie.most_common(2)) # Dos numeros más comunes
print(list(serie)) #Numeros que aparecen

#*************************************************

mi_diccionario = defaultdict(lambda : 'nada')
mi_diccionario['uno'] = 'primero'

print(mi_diccionario['dos'])
print(mi_diccionario['uno'])

#*************************************************

Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
kevin = Persona('kevin',1.74,78)
print(kevin.peso)

#***************************************************

lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])

lista_ciudades.appendleft("ssss")

print(lista_ciudades)