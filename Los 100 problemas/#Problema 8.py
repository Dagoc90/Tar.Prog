#Problema 8


def formatear_numero(n):
     return int(n) if isinstance(n, float) and n.is_integer() else n 


def sabe_radio():
     s_n = (input("¿Conoce el radio del circulo? (si/no): ")).strip().lower()
     while s_n != "si" and s_n != "no":
          print("Ingrese 'si' o 'no', por favor.")
          s_n = input("¿Conoce el radio del circulo? (si/no): ").strip().lower()
     if s_n == "si":
             r = float(input("Bien! Ingrese el radio, porfavor: "))
             return r
     elif s_n == "no":
           r = float(input("Ingrese el diametro del circulo: ")) /2
           return r

          
r = sabe_radio()

pi = 3.14
c = 2 * pi * formatear_numero(r)
a = pi * formatear_numero(r) ** 2

print(f"La circunferencia del círculo es: {c}")
print(f"El área del círculo es: {a}")