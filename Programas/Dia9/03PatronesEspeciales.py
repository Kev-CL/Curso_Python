import re

texto = 'Este texto es de ayuda para el ejercicio. Marca al 564-345-3445 para recibir ayuda'

patron = 'ayuda'

busqueda = re.search(patron,texto)

print(busqueda)
print(busqueda.span())
print(busqueda.start())

# lista de todas las que aparecen

busqueda2 = re.findall(patron,texto)
print(busqueda2)
print(len(busqueda2))

for palabra in re.finditer(patron,texto):
    print(palabra.span())
#***************************
print('*'*50)

patron2 = r'\d{3}-\d{3}-\d{4}'

busqueda_especal = re.search(patron2,texto)
print(busqueda_especal.group())
#***************************
# otra forma de buscar más especifica
print('*'*50)

patron3 = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

busqueda_especal = re.search(patron3,texto)
print(busqueda_especal.group(3))

#***************************

print('*'*50)
#Controlando el ingreso del us
clave = input('Clave: ')
patron_us = '\D{1}-\w{3}'
chequear = re.search(patron_us,clave)
print(chequear)
#***************************

print('*'*50)
# Tambien se puede agreagar mas de una coincidencia
frase = 'Las clases de Juan son los lunes'

busqueda_plural = re.search('clase.',frase) #para plural se agregan un punto o tres
busqueda_general = re.search('lunes|martes',frase)
busqueda_palabras = re.findall(r'[^\s]+',frase)
print(busqueda_palabras)