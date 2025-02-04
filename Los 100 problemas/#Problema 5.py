#Problema 6


def calcu_inte_comp(capital, tasa, tiempo):
    monto_final = capital * (1 + tasa) ** tiempo
    return monto_final

capital = float (input("Ingrese la capital inicial: "))
tasa = float(input("Ingrese la tasa de interes en %: ")) / 100
tiempo = float(input("Ingrese el tiempo en años"))
monto = calcu_inte_comp(capital, tasa, tiempo)

print(f"El monto final al pasar {tiempo} años será de {monto:.2f}")

