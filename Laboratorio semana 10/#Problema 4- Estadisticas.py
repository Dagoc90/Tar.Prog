#Problema 4- Estadisticas.
'''
Se busca:
1- Encontrar media, moda y promedio.
2- Permitir números arbitrarios usando args
3- Usar lambdas
'''

def estadisticas(*args):
    prom = sum(args) / len(args)
    
    args_ord = sorted(args)
    n = len(args_ord)
    if n % 2 == 0:
        mediana = (args_ord[n//2-1] + [args_ord//2]) / 2
    else:
        mediana = args_ord[n//2]

    sum_cua = sum((x - prom) ** 2 for x in args)
    vari = sum_cua / len(args)
    desv_est = vari ** 0.5
    return prom, mediana, desv_est

def main():
    numeros = input("Ingrése una lista de números separados por espacio: ").split()
    numeros = [float(num) for num in numeros]
    prom, mediana, desv_est = estadisticas(*numeros)

    print (f'''
        Promedio: {prom}
        Mediana: {mediana}
        Desviación Estandar: {desv_est}
        ''')
    
main()