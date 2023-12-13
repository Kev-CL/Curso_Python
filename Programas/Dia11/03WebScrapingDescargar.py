import bs4
import requests

resultdo = requests.get('https://escueladirecta.com/')

sopa = bs4.BeautifulSoup(resultdo.text, 'lxml')

imagenes = sopa.select('.course-box-image')[0]['src']
print(imagenes)

imagen_curso_1 = requests.get(imagenes)

f = open('mi_imagen.jpg','wb')
f.write(imagen_curso_1.content)
f.close()