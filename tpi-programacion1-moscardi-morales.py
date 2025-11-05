import csv
import os
NOMBRE_ARCHIVO = "paises.csv"

# Función que valida los números ingresados
def validar_numero(numero):
    try:
        float(numero)
        return True
    except ValueError:
        return False

# Función que valida que el país no exista dentro del archivo
def existe_pais(pais):
    paises = obtenerPaises()

    for pais in paises:
        if pais["nombre"].lower() == pais.lower():
            return True
        
    return False

# Función que obtiene los países del archivo
def obtenerPaises():
    paises = []
    # Verifica que el archivo exista
    if not os.path.exists(NOMBRE_ARCHIVO):
        print("El archivo no existe. Se está creando uno en este momento.")
        # Si no existe, lo crea
        with open (NOMBRE_ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["nombre", "poblacion", "superficie"])
            escritor.writeheader()
            return paises

    # Si existe, lo lee
    with open(NOMBRE_ARCHIVO, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            paises.append({"nombre": fila["nombre"].strip().title(), "continente": fila["continente"].strip().title(),"poblacion": int(fila["poblacion"]), "superficie": int(fila["superficie"])})
    return paises

# Función que guarda un nuevo país en el archivo sin modificar los existentes
def agregarPais(pais):
    with open(NOMBRE_ARCHIVO, "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["nombre", "continente", "poblacion", "superficie"])
        escritor.writerow(pais)

# 1. Agregar país
def agregar_pais():
    paises = obtenerPaises()
    nuevos_paises = []

    pais = input("Ingrese el país que desea agregar: ").strip().title()

    # Validamos que el país no exista dentro del archivo
    if existe_pais(pais):
        print("El país ingresado ya existe. ")
        return
    # Validamos que no se ingrese un país vacío
    elif pais == "":
        print("El país ingresado no puede estar vacío. ")
        return

    continente = input("Ingrese el continente al que pertenece el país: ").strip().title()

    if continente == "":
        print("El continente ingresado no puede estar vacío. ")
        return
    
    poblacion = input("Ingrese la población del país unicamente con números: ").strip()

    if not validar_numero(poblacion) or poblacion == "":
        print ("El número ingresado no es válido. ")
        return
    else:
        poblacion = float(poblacion)

    superficie = input("Ingrese la superficie del país (en km²): ").strip()

    if not validar_numero(superficie) or superficie == "":
        print ("El número ingresado no es válido. ")
        return
    else:
        superficie = float(superficie)

    # Agrega el nuevo país al archivo
    agregarPais({"nombre": pais, "continente": continente, "poblacion": poblacion, "superficie": superficie})
    print(f"Se agregó correctamente: '{pais}' con sus datos correspondientes. ")

# Función que muestra el menú
def mostrar_menu():
    while True:
        print("\n============ PAÍSES DEL MUNDO ============")
        opcion = input("Seleccione una de las siguientes opciones: "
        "\n1. Agregar país. " 
        "\n2. Actualizar Población y Superficie. " 
        "\n3. Buscar un país por nombre. " 
        "\n4. Filtrar países (continente/rango de pobalción/rango de superficie). "
        "\n5. Ordenar paises (nombre/población/superficie). "
        "\n6. Mostrar estadísticas. "
        "\n7. Salir. ").strip()

        if not validar_numero(opcion):
            print ("El número ingresado no es válido. ")
            return
        else:
            opcion = int(opcion)
        
        print("-------------------------------------------")

        # Estructura Case para realizar las acciones del menú según la opción elegida
        match opcion:
            case 1: # Agregar un país con todos los datos necesarios para almacenarse (No se permiten campos vacios). 
                agregar_pais()
            case 2: # Actualizar los datos de Población y Superfice de un Pais. 
                pass
            case 3: # Buscar un país por nombre (coincidencia parcial o exacta). 
                pass
            case 4: # Filtrar países (continente/rango de pobalción/rango de superficie).
                pass
            case 5: # Ordenar paises (nombre/población/superficie).
                pass
            case 6: # Mostrar estadísticas. 
                pass
            case 7: # Salir
                print("Saliendo...")
                break
            case _:
                print("Por favor, seleccione una opción válida.")

mostrar_menu()

