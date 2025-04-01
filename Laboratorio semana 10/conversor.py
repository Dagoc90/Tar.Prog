#Problema 5- Conversión de unidades.

'''
Se busca:
1- Km a millas
2- Celsius a Fahrenheit
3- Litros a galones
'''



def km_mil():
    km = float(input("Ingrese la cantidad de Km a convertir a millas: "))
    metros = km * 1000
    centi = metros * 100
    pulg = centi / 2.54
    feet = pulg / 12
    mill = feet / 5280
    return mill
    
def cel_far():
    cel = float(input("Ingrese la cantidad de Celsius a convertir a Fahrenheit: "))
    kel = cel + 273.15
    rankine = kel * 1.8 
    fahrenheit = rankine - 459.67
    return fahrenheit

def lit_gal():
    lit = float(input("Ingrese la cantidad de Litros a convertir a Galones: "))
    mili = lit * 1000 
    onz = mili / 29.5735
    pint = onz / 16 
    cuartos = pint / 2 
    galones = cuartos / 4
    return galones

