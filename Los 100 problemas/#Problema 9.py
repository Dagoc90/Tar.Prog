#Problema 9
# Hacer una lista con división en el medio conpares a la izquierda, impares a la derecha.
par = list()
impar = list()
lim = int(input("Ingrese el número mayor a ordenar (solo enteros): "))


for num in range(1, lim + 1):
    if (num) % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

tamaño = max(len(par), len(impar))

for item in range(tamaño):
    p = par[item] if item < len(par) else ""
    i = impar[item] if item < len(impar) else ""
    print("%4s \t %4s" % (p, i)) 