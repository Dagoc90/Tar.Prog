#Problema 1- Estructura de datos.

'''
Se busca desarrollar un programa que pida una palabra al usuario y haga:
1- El total de palabras en el texto.
2- Palabras únicas para usando conjuntos y sin repeticiones.
3- Frecuencia de cada palabra usando un diccionario con lapalabra y veces usadas.
4- Palabra más usada.
'''
import re


def bus_pal():
    text = input ("Ingrése un texto u oración a identificar: ").lower()
    text = re.sub(r'[^\w\s]', '', text)

    palabras = text.split()
    tot_pal = len(palabras)
    palabras_unicas = set(palabras)

    frecu = {}
    for palabra in palabras:
        frecu [palabra] = frecu.get(palabra, 0) + 1
    
    pal_mas_us = max(frecu, key= frecu.get)

    print (f'''
        Resultados:
            1- Palabras en el texto: {palabras}
            2- Palabras únicas: {palabras_unicas}
            3- Frecuencia de las palabras: {frecu}
            4- La palabra más usada es: {pal_mas_us} ({frecu[pal_mas_us]}) veces.
     ''')
    
bus_pal()