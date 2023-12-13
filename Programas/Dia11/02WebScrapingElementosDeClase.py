import bs4
import requests

resultdo = requests.get('https://escueladirecta.com/p/excel-aplicado-al-analisis-financiero')

sopa = bs4.BeautifulSoup(resultdo.text, 'lxml')

# Para clases se busca con un punto al inicio. Si lo que buscamos son los parrafos del
# Script se coloca una p.

descripcion = sopa.select('.col-lg-9 p')[0].get_text()
print(descripcion)
