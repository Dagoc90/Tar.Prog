#Problema 22

import random

def dado():
    return random.randint(1, 6)

def moneda():
    return random.choice(["águila", "sol"])

print ('''
1-Lanzar un dado.
2-Lanzar una moneda al aire.
''')

opcion = int(input("Seleccione una opción del menú de arriba: "))

if opcion == 1:
    print (f"El dado cayó en {dado()}")
elif opcion == 2:
    print (f"La moneda cayó {moneda()}")
else:
    print ("Seleccione una opción correcta, porfis.")