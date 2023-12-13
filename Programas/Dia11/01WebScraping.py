import bs4
import requests

resultdo = requests.get('https://escueladirecta.com/p/excel-aplicado-al-analisis-financiero')

sopa = bs4.BeautifulSoup(resultdo.text, 'lxml')

#print(resultdo.text)

print(len(sopa.select('p')))  # total de elementos
print(sopa.select('p'))  # lista de elemento buscado

# **************************************************************
print('*'*50)


print(sopa.select('title')[0])  # elemento sin corchetes o en pos 0
print(sopa.select('title')[0].getText())  # texto de elemento sin corchetes o en pos 0

# Asi extreaemos un elemento en especifico
