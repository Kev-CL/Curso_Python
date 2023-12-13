from random import *

aleatorio1 = randint(1,6) #int
aleatorio2 = round(uniform(1,100),1) #float
aleatorio3 = random() # 0 al 1

print(aleatorio1)

list = [1,2,3,4,5,6,7]
sort = choice(list)
shuffle(list)
print(list)