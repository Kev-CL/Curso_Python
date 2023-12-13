from random import randint
us = input("Ingresa tu nombre: ")
print(f"\nHola {us}, este juego consiste en que adivines el número del 1 al 100\n"
      f" en el que estoy pensando. ¿Estás listo? ¡Comencemos!")

num = randint(1,10)
print(num)

respuestas = []
cont = 1
band = False

while band!=True:
    resp = int(input("\nEn qué número estoy pensado? "))
    if resp not in range(1,100) :
        print("XX Tu respuesta no está dentro del 1 al 100. Intenta de nuevo. XX")
    else:
        if resp in respuestas:
            print(f"\n** Esta respuesta {resp} ya la diste en el intento {respuestas.index(resp)+1}. "
                  f"Intenta nuevamente. **")
            continue
        else:
            if resp < num:
                print("\nEl número es muy bajo.")
                respuestas.append(resp)
            elif resp > num:
                print("\nEl número es muy alto.")
                respuestas.append(resp)
            elif resp == num:
                respuestas.append(resp)
                print(f"\n¡FELICIDADES! Has adivinado en el intento {respuestas.index(resp)+1}.")
                band == True
                break
            else:
                print("Ha habido un error en el programa.")
                break



