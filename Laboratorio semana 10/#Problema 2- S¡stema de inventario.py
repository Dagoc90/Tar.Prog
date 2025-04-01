#Problema 2- Sistema de inventario.
'''
Se busca:
1- Que el usuario agregue y elimine productos, especificando: nombre, categoría, precio y cantidad.
2- Buscar objetos por su nombre y mostrar su info.
3- Mostrar objetos por orden de precio (menor a mayor)
'''
def menu():
    print('''
                Menú
    1- Agregar objeto al inventario.
    2- Eliminar objeto del inventario.
    3- Buscar un producto.
    4- Mostrar objeto por precio (menor a mayor).
    5- Salir.
    ''')
inventario = {}

def agr_prod():
    objeto = input("Ingrése el nombre del objeto: ").lower()
    categ = input("Ingrése la categoría del objeto: ").lower()
    precio = float(input("Ingrése el precio del objeto: "))
    cantidad = int(input("Ingrése la cantidad de objetos: "))

    inventario[objeto] = {f"Objeto": objeto, "Categoría": categ, "Precio": precio, "Cantidad": cantidad}
    print (f"{objeto} agregado al inventario.")

def elim_prod():
    objeto = input("Ingrése el nombre del objeto a eliminar: ").lower()
    if objeto in inventario:
        del inventario[objeto]
        print ("Objeto eliminado con éxito.")
    else:
        print ("Objeto no encontrado.")


def busc_obj():
    objeto = input ("Ingrese el objeto a buscar: ").lower()
    if objeto in inventario:
        objeto_encontrado = inventario[objeto]
        print(f"Objeto encontrado: {objeto_encontrado}")
    else:
        print ("Producto no encontrado.")

def por_precio():
    if not inventario:
        print ("No hay inventario.")
        return
    prod_ord = sorted(inventario.items(), key=lambda x: x[1]['Precio'])
    print ("\nInventario ordenado por precio: ")
    for nombre, datos in prod_ord:
        print (f"{nombre.capitalize()}: ${datos['Precio']} y hay {datos['Cantidad']} unidades.")


while True:
    menu()
    option = input ("Ingrese una opción: ")
    if option == "1":
        agr_prod()
    elif option == '2':
        elim_prod()
    elif option == '3':
        busc_obj()
    elif option == '4':
        por_precio()
    elif option == '5':
        print ("Saliendo del sistema . . .")
        break
    else:
        print ("Opción invalida. Intente de nuevo.")