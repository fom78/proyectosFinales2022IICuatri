import os
import time
from gestorTrabajadores import ingresarTrabajador, modificarTrabajador, eliminarTrabajador
from gestorReportes import mostrarDesocupadosPorEdad, mostrarTrabajadoresActivos, mostrarTrabajadoresDesocupados, mostrarTrabajadoresPorProfesion
from gestorStatus import cambiarStatusTrabajador

def finalizo():
    os.system("cls")
    print("")
    print("\t"*2, " GRACIAS POR UTILIZAR EL PROGRAMA ")
    print("\t"*2, "==================================")
    print("\n"*1)
    print("\t"*2, ".===============================.")
    print("\t"*2, "|    SISTEMA DE TRABAJADORES    |")
    print("\t"*2, "|       CODO A CODO  2022       |")
    print("\t"*2, "|            GRUPO C            |")
    print("\t"*2, ".===============================.")



def volverAtras():
    print("====================================================")
    print("")
    print("\t[1] CONTINUAR")
    print("\t[2] VOLVER AL MENU ANTERIOR")
    print("")
    while True:
        try:
            option = int(input(">>> INGRESE UNA OPCION: "))
            if option == 1:
                return False
            elif option == 2:
                return True
            else:
                print("OPCION INVALIDA")
        except:  
            print("OPCION INVALIDA")

def menuGestionReportes(listaTrabajadores):
    while True:
        os.system("cls")
        print("################################################")
        print("#             GESTION DE REPORTES              #")
        print("################################################")
        print("")
        
        print("\t[1] MOSTRAR TRABAJADORES ACTIVOS")
        print("\t[2] MOSTRAR TRABAJADORES DESOCUPADOS")
        print("\t[3] MOSTRAR DESOCUPADOS POR RANGO DE EDAD")
        print("\t[4] MOSTRAR TRABAJADORES POR PROFESION")
        print("\t[0] VOLVER AL MENU ANTERIOR")
        print("")
        while True:
            try:
                option = int(input(">>> INGRESE UNA OPCION: "))
                break
            except:
                print(">>> LA OPCION NO ES VALIDA <<<")
        print("")
        if option == 1:
            while True:
                os.system("cls")
                print("################################################")
                print("#             TRABAJADORES ACTIVOS             #")
                print("################################################")
                print("")
                mostrarTrabajadoresActivos(listaTrabajadores)
                if volverAtras():
                    break
        elif option == 2:
            while True:
                os.system("cls")
                print("################################################")
                print("#           TRABAJADORES DESOCUPADOS           #")
                print("################################################")
                print("")
                mostrarTrabajadoresDesocupados(listaTrabajadores)
                if volverAtras():
                    break
        elif option == 3: 
            while True:
                os.system("cls")
                print("################################################")
                print("#       TRABAJADORES DESOCPADOS POR EDAD       #")
                print("################################################")
                print("")
                mostrarDesocupadosPorEdad(listaTrabajadores)
                if volverAtras():
                    break
        elif option == 4:
            while True:
                os.system("cls")
                print("################################################")
                print("#          TRABAJADORES POR PROFESION          #")
                print("################################################")
                print("")
                mostrarTrabajadoresPorProfesion(listaTrabajadores)
                if volverAtras():
                    break
        elif option == 0:
            break
        else:
            print(">>> LA OPCION NO ES VALIDA <<<")
            time.sleep(1)

def menuGestionTrajadores(listaTrabajadores):
    while True:
        os.system("cls")
        print("################################################")
        print("#           GESTION DE TRABAJADORES            #")
        print("################################################")
        print("")
        
        print("\t[1] INGRESAR NUEVO TRABAJADOR")
        print("\t[2] MODIFICAR DATO DE TRABAJADOR")
        print("\t[3] ELIMINAR TRABAJADOR")
        print("\t[0] VOLVER AL MENU ANTERIOR")
        print("")
        while True:
            try:
                option = int(input(">>> INGRESE UNA OPCION: "))
                break
            except:
                print(">>> LA OPCION NO ES VALIDA <<<")
        print("")
        if option == 1:
            while True:
                os.system("cls")
                print("################################################")
                print("#             INGRESAR TRABAJADOR              #")
                print("################################################")
                print("")
                ingresarTrabajador(listaTrabajadores)
                if volverAtras():
                    break
        elif option == 2:
            while True:
                os.system("cls")
                print("################################################")
                print("#             MODIFICAR TRABAJADOR             #")
                print("################################################")
                print("")
                modificarTrabajador(listaTrabajadores)
                if volverAtras():
                    break
        elif option == 3: 
            while True:
                os.system("cls")
                print("################################################")
                print("#             ELIMINAR TRABAJADOR              #")
                print("################################################")
                print("")
                eliminarTrabajador(listaTrabajadores)
                if volverAtras():
                    break   
        elif option == 0:
            break
        else:
            print(">>> LA OPCION NO ES VALIDA <<<")
            time.sleep(1)

def menuStatus(listaTrabajadores):
    while True:
        os.system("cls")
        print("################################################")
        print("#              MODIFICAR STATUS                #")
        print("################################################")
        print("")
        cambiarStatusTrabajador(listaTrabajadores)
        if volverAtras():
            break
    