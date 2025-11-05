import csv
import os
NOMBRE_ARCHIVO = "paises.csv"

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
        seleccion = int(opcion)
        
        print("-------------------------------------------")

        # Estructura Case para realizar las acciones del menú según la opción elegida
        match seleccion:
            case 1: # Agregar un país con todos los datos necesarios para almacenarse (No se permiten campos vacios). 
                pass
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

