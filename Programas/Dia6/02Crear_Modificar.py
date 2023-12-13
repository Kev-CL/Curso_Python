"""Diferentes formas de abrir archivos:
r -- lectura
w -- escritura (Sobre escribe el texto y si no existe lo crea)
a -- Se posiciona al final del texto y si no existe lo crea. """

archivo = open('Prueba.txt','w')
archivo.write('Texto adicional n')
archivo.close()

archivo = open('Prueba.txt','r')
print(archivo.read())
archivo.close()