texto = "ABCDEFGHIJ"

fragmento = texto[1:5] #Desde i hasta j
print(fragmento)

fragmento = texto[1:] #Desde i hasta terminar frase
print(fragmento)

fragmento = texto[:5] #Desde el inicio de la frase hasta j
print(fragmento)

fragmento = texto[1:6:2] #Desde i hasta j con saltos de 2
print(fragmento)

fragmento = texto[::2] #Desde inicio de frase hasta fin de frase con saltos de 2
print(fragmento)

fragmento = texto[::-1] #Desde inicio de frase hasta fin de frase con saltos de 1, iniciando a revés
print(fragmento)