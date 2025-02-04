#Problema 5

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
       if n % i == 0:
           return False
    return True

num =  int(input ("Introduzca el número a detectar: "))
if es_primo(num):
    print (f"El número {num} es primo.")
else:
    print (f"El número {num} no es primo.")