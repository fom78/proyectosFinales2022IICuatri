
""" Realizar un sistema que permita ejecutar distintas funciones a un empleado de una consultora de
trabajo.
La consultora guarda los datos de los trabajadores en un archivo llamado trabajadores.dat, la
estructura de este archivo es la siguiente
Nombre, edad, dni, profesion, activo(Opcionalmente pueden agregar algunos datos más.)
En activo se define si esta o no trabajando dicho trabajador.
Un ejemplo del archivo con algunos trabajadores seria:
Enzo, 12, 3223233232, Gamer, True
Ingrid, 14, 687678345, Programador/a, False
Roque, 34, 34343434, Electricista, False
El Menú principal del sistema debe mostrar las siguientes opciones:
[1] Gestión de Trabajadores
[2] Reportes
[3] Cambiar status trabajador
[0] Salir
Gestión de Trabajadores
Deberá mostrar otro menú con estas opciones:
[1] Ingresar nuevo Trabajador
[2] Modificar dato de trabajador
[3] Eliminar Trabajador
[0] Volver al menú principal
Reportes
[1] Mostrar trabajadores Activos
[2] Mostrar trabajadores desocupados
[3] Mostrar desocupados en un rango de edad
[4] Mostrar trabajadores según la profesión
[0] Volver al menú principal
Cambiar status trabajador
En esta opción se debe buscar el trabajador por dni y cambiarle el status activo, es cuando se da
de alta/baja en un trabajo """

from io import open
from gestionar import apertura, altaTrabajador, modificarTrabajador, eliminarTrabajador, status
from tryExcept import tryExceptOptions
import os
from reportes import trabajadorActivo, trabajadorDesocupados, trabajadorRangoEdad, trabajadorProfesion
from decoraciones import decorar

    
#archivo = apertura("trabajadores.dat")
#print(archivo)
while True:
    os.system("cls")
    print("""
        ┌──────────────────────────┐
        │ TRABAJO PRACTICO GRUPO A │
        │   CONSULTORA DE TRABAJO  │
        │   CURSO CODO A CODO 4.0  │
        └──────────────────────────┘\n
        ┌──────────────────────────┐
        │     Menú Principal       │ 
        └──────────────────────────┘\n                   
       ┌───────────────────────────────────┐
       │ [1] Gestion de trabajadores       │
       │ [2] Reportes                      │
       │ [3] Cambiar status del trabajador │
       │ [4] Salir                         │
       └───────────────────────────────────┘
    """)

    opcion = tryExceptOptions()
    if opcion == 4:
        break

    elif opcion == 1:
        os.system("cls")
        while True:
            print("""
                ┌───────────────────────────────────┐
                │     Gestion de trabajadores       │
                └───────────────────────────────────┘\n
                ┌──────────────────────────────────────┐
                │ [1] Ingresar nuevo trabajador        │
                │ [2] Modificar datos de un trabajador │
                │ [3] Eliminar trabajador              │
                │ [4] Volver al Menu Principal         │
                └──────────────────────────────────────┘
                """)
        
            opcion = tryExceptOptions()
            if opcion == 4:
                break

            elif opcion == 1:
                altaTrabajador()
                decorar()
                os.system("pause")
            
            elif opcion == 2:
                #dni = tryExceptOptions("Ingrese DNI del trabajador a modificar: ")
                decorar()
                modificarTrabajador()
                os.system("pause")
            
            elif opcion == 3:
                #dni = tryExceptOptions("Ingrese DNI del trabajador que quiere eliminar: ")
                decorar()
                eliminarTrabajador() 
                os.system("pause")

    elif opcion == 2:
        os.system("cls")
        while True:
            print("""
                ┌──────────────────────────────────────┐
                │            Reportes                  │
                └──────────────────────────────────────┘\n

                ┌──────────────────────────────────────────────┐
                │  [1] Mostrar trabajadores Activos            │
                │  [2] Mostrar trabajadores Desocupados        │
                │  [3] Mostrar Desocupados en un rango de edad │
                │  [4] Mostrar trabajadores segun su Profesion │
                │  [5] Volver al Menu Principal                │
                └──────────────────────────────────────────────┘\n
                """)
            opcion = tryExceptOptions()
            if opcion == 5:
                break

            elif opcion == 1:
                decorar()
                trabajadorActivo()
                os.system("pause")

            elif opcion == 2:
                decorar()
                trabajadorDesocupados()
                os.system("pause")

            elif opcion == 3:
                decorar()
                trabajadorRangoEdad()
                os.system("pause")

            elif opcion == 4:
                decorar()
                trabajadorProfesion()
                os.system("pause")

    elif opcion == 3:
        decorar()
        status()
        print("El Status fue actualizado")
        os.system("pause")

os.system("cls")
print("""
     ┌─────────────────────────┐
     │    Fin del Programa     │
     └─────────────────────────┘\n
    """)
