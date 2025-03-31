#Problema 23

def crea_mat(filas, columnas):
    matriz = []
    for i in range (filas):
        fila = []
        for j in range (columnas):
            valor = int(input(f"Ingrese el valor de "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def print_mat(matriz):
    for fila in matriz:
        print (" ".join(map(str, fila)))

def sum_mat(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    resultado = [[matriz1[i][j] + matriz2[i][j] for j in range(columnas)] for i in range(filas)]
    return resultado

def rest_mat(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    resultado = [[matriz1[i][j] - matriz2[i][j] for j in range(columnas)] for i in range(filas)]
    return resultado

def mult_escalar(matriz, escalar):
    return [[elemento * escalar for elemento in fila ] for fila in matriz]

def trans_mat (matriz):
    return [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]

print ("Operaciones con matrices.")
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

print ("Ingrese el valor de la primera matriz: ")
matriz1 = crea_mat(filas, columnas)

opcion = int(input("\nSeleccione una opción:\n1-Suma de matrices.\n2-Resta de matrices.\n3-Multiplicación por un número.\n4-Transponer la matriz."))

if opcion == 1:
    print("Ingrese el valor de la segunda matriz: ")
    matriz2 = crea_mat(filas, columnas)
    resultado = sum_mat(matriz1, matriz2)
    print ("El resultante de la suma entre matrices es: ")
    print_mat(resultado)
elif opcion == 2:
     print("Ingrese el valor de la segunda matriz: ")
     matriz2 = crea_mat(filas, columnas)
     resultado = rest_mat(matriz1, matriz2)
     print ("El resultante de la suma entre matrices es: ")
     print_mat(resultado)
elif opcion == 3:
    escalar = float(input("Ingrese el número al que se quiere multiplicar la matriz: "))
    resultado = mult_escalar(matriz1, escalar)
    print ("La matriz resultante es: ")
    print_mat(resultado)
elif opcion == 4:
    resultado = trans_mat(matriz1)
    print ("La matriz transpuesta es:")
    print_mat(resultado)
else:
    print ("Opción inválida, seleccione una correcta.")