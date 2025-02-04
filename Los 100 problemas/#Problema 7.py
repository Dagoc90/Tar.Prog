#Problema 7

def par_o_no(n):
    if (n) % 2 == 0:
        return True
    else:
        return False

def mult(n):
    if num % num2 == 0:
        return True
    else:
        return False

def formatear_numero(n):
     return int(n) if isinstance(n, float) and n.is_integer() else n   

def pedir_num():
    while True:
        try:
            num = float(input("Ingrese un número: "))
            return num
        except ValueError:
            print ("ERROR. INGRESE NÚMERO VÁLIDO.")

def pedir_num2():
    while True:
        try:
            num2 = float(input("Ingrese un número: "))
            return num2
        except ValueError:
            print ("ERROR. INGRESE NÚMERO VÁLIDO.")            


num = pedir_num()
num = formatear_numero(num)


if par_o_no(num):
    print (f"El número {num} es par.")
else:
    print (f"El número {num} es impar.")

num2 = pedir_num2()
num2 = formatear_numero(num2)

if mult(num2):
    print (f"El número {num} es multiplo de {num2}!")
else:
    print (f"El número {num} no es multiplo de {num2}")