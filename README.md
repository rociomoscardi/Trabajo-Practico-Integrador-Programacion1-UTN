# 💻 Trabajo Práctico Integrador - Programación 1  
**Tecnicatura Universitaria en Programación**  
📍 *Universidad Tecnológica Nacional*  

## ✨ Estudiantes
- Moscardi, Rocío - Comisión 9
- Morales, Susana - Comisión 9

## 👩🏻‍🏫 Docente
- Gubiotti, Flor - Comisión 9 

## 🌎 Descripción del Proyecto
Este programa en Python permite gestionar información de países a través de una interfaz de consola interactiva.
Utiliza estructuras como **listas** y **diccionarios**, y opera sobre **archivos CSV** para almacenar datos de forma persistente.
El sistema ofrece un menú de opciones que permite agregar, actualizar, buscar, filtrar y ordenar países según distintos criterios, además de calcular estadísticas básicas sobre población y superficie.
Se implementan **validaciones** para garantizar la integridad de los datos, evitar errores de formato y brindar mensajes claros al usuario.

## 🧩 Descripción del Programa
Este programa permite gestionar un archivo CSV con información sobre países del mundo. El usuario puede agregar, buscar, actualizar, filtrar, ordenar y visualizar estadísticas de los países registrados. Cada país contiene los siguientes datos:
- Nombre
- Continente
- Población
- Superficie (en km²)

El archivo paises.csv se crea automáticamente si no existe, y se actualiza dinámicamente con cada operación.

## 🛠️ Instrucciones de uso
1. Ejecutá el programa desde tu entorno Python.
2. Se mostrará un menú principal con las siguientes opciones:
- Agregar país
- Actualizar población y superficie
- Buscar país por nombre
- Filtrar países por continente, población o superficie
- Ordenar países por nombre, población o superficie
- Mostrar estadísticas generales
- Salir
3. Ingresá el número correspondiente a la opción deseada.
4. Seguí las instrucciones en pantalla para completar cada operación.

## 💡 Ejemplos de entradas y salidas
**➕ Agregar país**
- Entrada:\n
Ingrese el país que desea agregar: Argentina
Ingrese la población del país unicamente con números: 47000000
Ingrese la superficie del país (en km²): 2780000
Ingrese el continente al que pertenece el país: América

- Salida:\n
Se agregó correctamente: 'Argentina' con sus datos correspondientes.

**🔍 Buscar país**
- Entrada:\n
Ingrese el nombre del país que desea buscar: Argen

- Salida:\n
País: Argentina - Continente: América - Población: 47000000 - Superficie: 2780000

**📊 Mostrar estadísticas**
- Salida:\n
============== Estadísticas Generales ==============
- País con mayor población: China (1400000000)
- País con menor población: Uruguay (3500000)
- Promedio de población: 500000000.00
- Promedio de superficie: 1200000.00
Cantidad de países por continente:
- América: 3 país(es)
- Europa: 2 país(es)
- Asia: 1 país(es)

## 👥 Participación de los integrantes
Este proyecto fue desarrollado por:

**Rocío Moscardi:**
- Diseño de la estructura del programa
- Implementación de funciones de validación.
- Desarrollo del menú principal.
- Coordinación de la integración final del código y verificación de consistencia entre funciones.

**Susana Morales:**
- Implementación de funciones de filtrado y ordenamiento.
- Desarrollo de la lógica de interacción.
- Pruebas de funcionamiento de cada módulo.
- Pruebas y depuración del sistema.

📌 **Archivo CSV con el dataset base:**  
[Ver archivo de países (CSV)](paises.csv)

## 🔗 Video explicativo:
- Youtube: 



