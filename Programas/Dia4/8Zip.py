##1
nombres = ['A','B','C']
edades = [34,56,78]

combinados = list(zip(nombres,edades))

print(combinados)

##2
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

comb = list(zip(capitales,paises))
for capital,pais in comb:
    print(f"La capital de {pais} es {capital}")

