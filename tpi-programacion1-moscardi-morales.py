import csv
import os
NOMBRE_ARCHIVO = "paises.csv"

# Función que valida los números ingresados
def validar_numero(numero):
    if not numero.isdigit():
        return False
    else:
        return True

# Función que valida que el país no exista dentro del archivo
def existe_pais(nombre_pais):
    paises = obtenerPaises()

    for pais in paises:
        if pais["nombre"].lower() == nombre_pais.lower():
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
            escritor = csv.DictWriter(archivo, fieldnames=["nombre", "continente","poblacion", "superficie"])
            escritor.writeheader()
            return paises

    # Si existe, lo lee
    with open(NOMBRE_ARCHIVO, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            paises.append({"nombre": fila["nombre"].strip().title(), "continente": fila["continente"].strip().title(),"poblacion": float(fila["poblacion"]), "superficie": float(fila["superficie"])})
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

# 2. Actualizar población y superficie
def actualizar_poblacion_superficie():
    paises = obtenerPaises()
    
    if len(paises) == 0:
        print("No hay países en el archivo. Debe ingresar al menos uno para poder modificar su población y superficie. ")
        return
    
    # Muestra los países para que el usuario pueda elegir
    print("Lista de países: ")
    for pais in paises:
        print(f"País: {pais['nombre']} - Población: {pais['poblacion']} - Superficie: {pais['superficie']}.")

    pais_ingresado = input("Ingrese el país para modificar su población y superficie. ").strip().title()

    if pais_ingresado == "":
        print("El país ingresado no puede estar vacío.")
        return

    if not existe_pais(pais_ingresado):
        print(f"'{pais_ingresado}' no se encuentra en el listado.")
        return
    
    # Solicita nuevos datos
    nueva_poblacion = input("Ingrese la nueva población: ").strip()
    if not validar_numero(nueva_poblacion) or nueva_poblacion == "":
        print("La población ingresada no es válida.")
        return
    else:
        nueva_poblacion = float(nueva_poblacion)

    nueva_superficie = input("Ingrese la nueva superficie (en km²): ").strip()
    if not validar_numero(nueva_superficie) or nueva_superficie == "":
        print("La superficie ingresada no es válida.")
        return
    else:
        nueva_superficie = float(nueva_superficie)

    # Actualiza los datos en la lista
    actualizado = False
    for pais in paises:
        if pais["nombre"].lower() == pais_ingresado.lower():
            pais["poblacion"] = nueva_poblacion
            pais["superficie"] = nueva_superficie
            actualizado = True
            break

    if not actualizado:
        print("No se pudo actualizar el país.")
        return

    # Reescribe el archivo CSV con los datos actualizados
    with open(NOMBRE_ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["nombre", "continente", "poblacion", "superficie"])
        escritor.writeheader()
        escritor.writerows(paises)

    print(f"Se actualizaron correctamente los datos de '{pais_ingresado}'.")

# 3. Buscar un país por nombre (coincidencia parcial o exacta)
def buscar_pais_nombre():
    paises = obtenerPaises()
    
    if len(paises) == 0:
        print("No hay países en el archivo. ")
        return
    
    pais_ingresado = input("Ingrese el nombre del país que desea buscar: ").strip().title()

    if pais_ingresado == "":
        print("El país ingresado no puede estar vacío.")
        return

    encontrados = []
    
    for pais in paises:
        if pais_ingresado in pais["nombre"].title():
            encontrados.append(pais)

    if len(encontrados) == 0:
        print(f"No se encontraron países que coincidad con '{pais_ingresado}'")
    else:
        for pais in encontrados:
            print(f"País: {pais['nombre']} - Continente: {pais['continente']} - Población: {pais['poblacion']} - Superficie: {pais['superficie']}")

# 4. Filtrar países (continente/rango de población/rango de superficie)
def filtrar_paises():
    while True:
        opcion = input("Seleccione una de las siguientes opciones: "
        "\n1. Filtrar países por continente. " 
        "\n2. Filtrar países por rango de población. " 
        "\n3. Filtrar países por rango de superficie. " 
        "\n4. Volver. ").strip()

        if not validar_numero(opcion):
            print ("El número ingresado no es válido. ")
            return
        else:
            opcion = int(opcion)
        
        print("-------------------------------------------")

        match opcion:
            case 1: # Filtrar por continente.
                filtrar_pais_continente()
            case 2: # Filtrar por rango de población.
                filtrar_pais_poblacion()
            case 3: # Filtrar por rango de superficie. 
                pass
            case 4: # Volver.
                print("Volviendo...")
                return
            case _:
                print("Por favor, seleccione una opción válida.")

# 4.1 Filtrar países por continente
def filtrar_pais_continente():
    paises = obtenerPaises()
    
    if len(paises) == 0:
        print("No hay países en el archivo. ")
        return
    
    continente = input("Ingrese el continente por el cual desea filtrar los países: ").strip().title()
    print()

    if continente == "":
        print("El continente ingresado no puede estar vacío.")
        return

    encontrados = []
    
    for pais in paises:
        if continente == pais["continente"].title():
            encontrados.append(pais)

    if len(encontrados) == 0:
        print(f"No se encontraron países que pertenezcan a {continente}.")
    else:
        for pais in encontrados:
            print(f"País: {pais['nombre']} - Continente: {pais['continente']} - Población: {pais['poblacion']} - Superficie: {pais['superficie']}")
    print()

# 4.2 Filtrar países por rango de población
def filtrar_pais_poblacion():
    paises = obtenerPaises()
    
    if len(paises) == 0:
        print("No hay países en el archivo. ")
        return
    
    min_pob = input("Ingrese la población mínima: ").strip()
    max_pob = input("Ingrese la población máxima: ").strip()
    print()

    if not validar_numero(min_pob) or not validar_numero(max_pob):
        print("Ambos valores deben ser números válidos.")
        return
    else:
        min_pob = float(min_pob)
        max_pob = float(max_pob)

    if min_pob > max_pob:
        print("La población mínima no puede ser mayor que la máxima.")
        return

    encontrados = []
    
    for pais in paises:
        if min_pob <= pais["poblacion"] <= max_pob:
            encontrados.append(pais)

    if len(encontrados) == 0:
        print(f"No se encontraron países con población entre a {min_pob} y {max_pob}.")
    else:
        for pais in encontrados:
            print(f"País: {pais['nombre']} - Continente: {pais['continente']} - Población: {pais['poblacion']} - Superficie: {pais['superficie']}")
    print()

# Función que muestra el menú
def mostrar_menu_principal():
    while True:
        print("\n============ PAÍSES DEL MUNDO ============")
        opcion = input("Seleccione una de las siguientes opciones: "
        "\n1. Agregar país. " 
        "\n2. Actualizar población y superficie. " 
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
            case 2: # Actualizar los datos de población y superfice de un país. 
                actualizar_poblacion_superficie()
            case 3: # Buscar un país por nombre (coincidencia parcial o exacta). 
                buscar_pais_nombre()
            case 4: # Filtrar países (continente/rango de pobalción/rango de superficie).
                filtrar_paises()
            case 5: # Ordenar países (nombre/población/superficie).
                pass
            case 6: # Mostrar estadísticas. 
                pass
            case 7: # Salir
                print("Saliendo...")
                break
            case _:
                print("Por favor, seleccione una opción válida.")

mostrar_menu_principal()

