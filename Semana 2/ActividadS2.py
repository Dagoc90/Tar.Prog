limite = input()
par = list()
impar = list()

for num in range (1,limite+1):
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

tamanyo = max(len(par), len(impar))

for item in range(tamanyo):
    try:
        print("%4d \t %4d" % par[item], impar[item]) sep= '|'


impresion = max(len(par), len (impar))
print impresion