#Problema 3- Programa gestionador de contactos.

'''
Se busca:
1- Agregar contactos como tupla con nombre, correo y número telefonico.
2- La agenda debe almacenarse en una lista.
3- Permitir agregar más contactos.
4- 
'''

def menu():
    print ('''
                Menú
        1- Agregar contacto.
        2- Buscar contacto.
        3- Lista de contactos.
        4- Salir de la agenda.
    ''')

agenda = []

def agr_con():
    nombre = input ("Ingrese el Nombre del contacto: ").capitalize()
    núm = input ("Agregue el número del contacto: ")
    correo = input ("Agregue el correo del contacto: ")

    contacto = (nombre, núm, correo)
    agenda.append(contacto)
    print (f"{nombre} agregado a tu agenda.")

def busc_con():
    nombre = input ("Ingrese el Nombre del contacto: ").capitalize()
    encontrado = False
    for contacto in agenda:
        if contacto[0] == nombre:
             print(f"Contacto encontrado: Nombre: {contacto[0]}, Teléfono: {contacto[1]}, Correo: {contacto[2]}")
             encontrado = True
             break
    if not encontrado:
        print("Contacto no encontrado.")

def lista():
    if not agenda:
        print ("No hay contactos en la agenda.")
        return
    agenda_ordenada = sorted(agenda, key=lambda x: x[0])
    print ("\n Lista de contactos: ")
    for contacto in agenda_ordenada:
      print(f"Nombre: {contacto[0]}, Teléfono: {contacto[1]}, Correo: {contacto[2]}")


while True:
    menu()
    option = input("Ingrese una opción: ")
    if option == "1":
        agr_con()
    elif option == "2":
        busc_con()
    elif option == "3":
        lista()
    elif option == "4":
        print("Saliendo del sistema . . .")
        break
    else:
        print("Opción inválida. Intente de nuevo.")