edad = 16
tiene_licencia = False

"No puedes conducir. Necesitas contar con una licencia"
if edad < 18:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
else:
    if tiene_licencia:
        print("Puedes conducir")
    else:
        print("No puedes conducir. Necesitas contar con una licencia")