#Problema 24
def formatear_numero(n):
     return int(n) if isinstance(n, float) and n.is_integer() else n

def sum_prog_ari(a, d , n):
    suma = (n / 2) * (2 * a + (n - 1) * d)
    return suma

a = float(input("Ingrese el valor del primer término de la sucesión: "))
d = float(input("Ingrese el valor de la diferencia común: "))
n = int(input("Ingrese la cantidad de términos a sumar: "))

res = sum_prog_ari (a, d, n)
print (f"El resultado de la sucesión de los primeros {n} términos es: {formatear_numero(res)}")