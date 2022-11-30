import os
from controlErrores import validarOpcion
from crudTrabajador import agregarTrabajador, obtenerTrabajadores, modificarTrabajador
from vista  import decorarTitulos, decorarMenu, decorarMenuTrabajador, decorarListaTrabajador

listaDeTrabajadores = obtenerTrabajadores("Trabajadores.dat")

while True:

    decorarTitulos("Menu Principal","#",50)
    decorarMenu()
    opcion = validarOpcion("Selecccione una opcion: ")

    if opcion == 0:
        print("Hasta pronto...")
        break
    elif opcion == 1: #menu gestion

        os.system("cls")
        decorarTitulos("Gestion Trabajadores","#",50)
        decorarMenuTrabajador()
        opcion = validarOpcion("Selecccione una opcion: ")

        if opcion ==1:
            os.system("cls")
            #print("ingresar Trabajador")
            agregarTrabajador("Trabajadores.dat")
        elif opcion == 2:
            os.system("cls")
            dniTrabajador=input("Ingrese el dni del trabajador: ")
            modificarTrabajador(listaDeTrabajadores, dniTrabajador)
        elif opcion == 3:
            os.system("cls")
            print("Eliminar Trabajador")
    elif opcion == 2:
        print("reportes")

    elif opcion == 4:
        os.system("cls")
        decorarListaTrabajador(listaDeTrabajadores)
           #print(input("tendria que mostrar un trabajador"))
    else:
        #decorar()
        os.system("cls")
        print("Elija una opcion correcta")
