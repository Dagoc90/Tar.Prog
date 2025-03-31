#Problema 21 
pi = 3.1415

def formatear_numero(n):
     return int(n) if isinstance(n, float) and n.is_integer() else n

print ('''
                               Área:             Volúmen:
1- Circulo               :   A = πr^2                /
2- Cuadrado / rectángulo :   A = bxh                 /
3- Esfera                :   A = 4πr^2           V = 4/3πr^3
4- Cubo                      A = 6a^2            V = a^3
5- Cilindro              :   A = 2πr(h + r)      V = πr^2h
''')


select = int(input("Igrese el número de la figúra deseada a usar: "))

def cal_fig (opcion):
     if opcion == 1:
          r = float(input("Ingrese el radio de el circulo: "))
          aCi = pi * r ** 2
          print (f"El área de el circulo es: {formatear_numero(aCi)}.")
     elif opcion == 2:
          b = float(input("Ingrese la base: "))
          h = float(input("Ingrese la altura: "))
          aCu = b * h
          print (f"El área del cuadrado/rectangulo es: {formatear_numero(aCu)}.")
     elif opcion == 3:
          r = float(input("Ingrese el radio de la esfera: "))
          aEs = 4 * pi * r ** 2
          volEs = (4 / 3) * pi ** 3
          print (f"El área de la esfera es: {formatear_numero(aEs)}.")
          print (f"El volúmen de la esfera es: {formatear_numero(volEs)}.")
     elif opcion == 4:
          a = float(input("Ingrese la longitúd del lado del cubo: "))
          aCub = 6 * a ** 2
          volCub = a ** 3
          print (f"El área del cubo es: {formatear_numero(aCub)}.")
          print (f"El volúmen del cubo es: {formatear_numero(volCub)}.")
     elif opcion == 5:
          r = float(input("Ingrese el radio del cilindro: "))
          h = float(input("Ingrese la altura de el cilindro: "))
          aCil = 2 * pi * r * (h + r)
          volCil = pi * r ** 2 * h
          print (f"El área del cilidro es: {formatear_numero(aCil)}.")
          print (f"El volúmen del cilindro es: {formatear_numero(volCil)}.")
     else:
          print ("Error. Por favor elija un número entre 1 y 5.")

cal_fig(select)