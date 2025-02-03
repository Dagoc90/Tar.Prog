#Los 100 problemas de python#

#1
#print ("Hola Mundo!")

#2

# D.V #
import math
def formatear_numero(n):
     return int(n) if isinstance(n, float) and n.is_integer() else n   

select = input ("¿Qué quiere hacer: sumar, restar, dividir, multiplicar, elevar ó factorial?\n").strip().lower()
while select not in ["sumar", "restar", "dividir", "multiplicar", "elevar", "factorial"]:
     print ("Error, no seleccionó operación válida")
     select = input ("¿Qué quiere hacer: sumar, restar, dividir, multiplicar, elevar ó factorial?\n").strip().lower()

          

if select == "factorial":
     num = int(input("Ingrése un número:\n"))
     if num < 0:
          print ("Error, los negativos no tienen factorial.")
     else:
          print (f"El factorial de {num} es: {math.factorial(num)}")

else:
    n01 = float(input("Ingrese un número \n"))
    n02 = float(input("Ingrese otro número \n"))

    n01 = formatear_numero(n01)
    n02 = formatear_numero(n02)

    suma = n01 + n02
    resta = n01 - n02
    div = n01 / n02 if n02 != 0 else "Error, división por 0!"
    mult = n01 * n02
    elev = n01 ** n02

if select == "sumar":
    print (f"La suma de {n01} y {n02} es: {formatear_numero(suma)}")
elif select == "restar":
     print (f"La resta de {n01} y {n02} es: {formatear_numero(resta)}")
elif select == "dividir":
    if n02 == 0:
          print ("No se puede divir entre 0, intente de nuevo.")
    else:
         print (f"La división de {n01} y {n02} es: {formatear_numero(div)}")
elif select == "multiplicar":
     print (f"La multiplicación de {n01} y {n02} es: {formatear_numero(mult)}")
elif select == "elevar":
     print (f"La elevación de {n01} a la {n02} potencia es: {formatear_numero(elev)}")
