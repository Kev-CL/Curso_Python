import bs4
import requests

# Url con dif. número de página.
url_base = 'http://books.toscrape.com/catalogue/page-{}.html'

# Lista de libros con más de 3 estrellas.
titulos_rating_alto = []

# Recorrido de páginas
for pag in range(0,51):
    # Crear sopa en cada pagina
    url_pagina = url_base.format(pag)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    # Seleccionar datos de los libros
    libros = sopa.select('.product_pod') # clase o elemento de cada libro

    # Iterar libros
    for libro in libros:
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:
            # Guardar titulo de libro en variable
            titulo_libro = libro.select('a')[1]['title']
            # Agregar libros
            titulos_rating_alto.append(titulo_libro)


# Ver libros con más de 3 estrellas
numeracion = 1
for t in titulos_rating_alto:
    print(f'{numeracion}. {t}')
    numeracion = numeracion + 1