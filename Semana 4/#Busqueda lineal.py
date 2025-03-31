#Busqueda lineal

from random import randint

listaP = list()
listaN = list()

elementos = int(input("Introduce la cantidad de elementos: "))
for cont in range (-elementos, elementos):
    if cont < 0:
        listaN.append(randint(-100, 0))
    elif cont > 0:
        listaP.append(randint(1, 100))
    else:
        listaP.append(0, 1)

listaCom = listaN + listaP

print(listaCom)

listaN.extend(listaP)

print(listaN)

num = int(input("Introduce un número a buscar"))




##Busqueda binaria

#Leer sobre el algoritmo de Divide y Venceras.