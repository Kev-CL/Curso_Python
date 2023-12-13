def num_perfumeria():
    for n in range (1,1000):
        yield f"P - {n}"


def num_farmacia():
    for n in range (1,1000):
        yield f"F - {n}"


def num_cosmetica():
    for n in range (1,1000):
        yield f"C - {n}"


p = num_perfumeria()
f = num_farmacia()
c = num_cosmetica()


def decorar(area):
    print('Su turno es:\n')
    if area == 'p':
        print(next(p))
    elif area == 'f':
        print(next(f))
    elif area == 'c':
        print(next(c))
    print('\nEn un momento se le atenderá.\n')

