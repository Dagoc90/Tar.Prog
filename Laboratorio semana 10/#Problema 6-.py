#Problema 6-
'''
Se busca:
1- Crear una clase y poder agregar:
    Atributos: Marca, Modelo, Año y Precio.
2- Método para mostrar lo anterior.
3- Subclases Automovil y Motocicleta con atributos adicionales como numero de puertas o cilindrada.
'''

class Vehiculo:
    def __init__(self, marca, modelo, anio, precio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio
    
    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}, Precio: ${self.precio}")

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, anio, precio, puertas):
        super().__init__(marca, modelo, anio, precio)
        self.puertas = puertas
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Puertas: {self.puertas}")

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, precio, cilindrada):
        super().__init__(marca, modelo, anio, precio)
        self.cilindrada = cilindrada
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Cilindrada: {self.cilindrada}cc")

vehiculos = []  # Lista para almacenar los vehículos

def agregar_vehiculo():
    tipo = input("¿Qué tipo de vehículo quieres agregar? (auto/moto): ").lower()
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    anio = input("Año: ")
    precio = float(input("Precio: "))

    if tipo == "auto":
        puertas = int(input("Número de puertas: "))
        vehiculo = Automovil(marca, modelo, anio, precio, puertas)
    elif tipo == "moto":
        cilindrada = int(input("Cilindrada en cc: "))
        vehiculo = Motocicleta(marca, modelo, anio, precio, cilindrada)
    else:
        print("Tipo no válido.")
        return

    vehiculos.append(vehiculo)
    print("Vehículo agregado con éxito.\n")

def listar_vehiculos():
    if not vehiculos:
        print("No hay vehículos registrados.")
        return

    print("\nLista de vehículos:")
    for i, v in enumerate(vehiculos, 1):
        print(f"\nVehículo {i}:")
        v.mostrar_info()

def menu():
    while True:
        print("\nMenú:")
        print("1. Agregar vehículo")
        print("2. Listar vehículos")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_vehiculo()
        elif opcion == "2":
            listar_vehiculos()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()