#1
def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(suma(5,6))

#2
def suma2(*args):
    return sum(args)

print(suma2(5,6,9))


def numeros_persona(nombre, *args):
    return f"{nombre}, la suma de tus numeros es {sum(args)}"

msn=numeros_persona("fbfggf",1,2,3,4,5)
print(msn)