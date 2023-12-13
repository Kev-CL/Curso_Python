"""Con la libreria Path, podemos insertar la ruta con la diagonal común y para leer el archivo
no es necesario abrir y cerrar el archivo."""


from pathlib import Path


archivo =Path("C:/Users/kevin/Documents/MEGAsync/2. Cursos/Python/Archivos_P/Prueba.txt")

print(archivo.read_text()) #lee texto
print(archivo.name) #nombre completo de archivo (nombre y tipo o terminación)
print(archivo.suffix) #tipo de archivo
print(archivo.stem) #unicamente nombre del archivo
print(archivo.exists()) #Muestra si existe

print(Path.home()) #ruta base