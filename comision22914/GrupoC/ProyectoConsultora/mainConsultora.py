import os
import time
from viewConsultora import menuStatus, menuGestionTrajadores, menuGestionReportes, finalizo
from persistenciaTrabajadores import recuperarTrabajadores

try:
    listaTrabajadores = recuperarTrabajadores()
except:
    listaTrabajadores = []

# main
while True:
    os.system("cls")
    print("################################################")
    print("#             PROYECTO CONSULTORA              #")
    print("################################################")
    print("")
    print("\t[1] GESTION DE TRABAJADORES")
    print("\t[2] REPORTES")
    print("\t[3] CAMBIAR STATUS DE TRABAJADOR")
    print("\t[0] SALIR")
    print("")
    while True:
        try:
            option = int(input(">>> INGRESE UNA OPCION: "))
            break
        except:
            print("LA OPCION NO ES VALIDA")
    if option == 1:
        menuGestionTrajadores(listaTrabajadores)
    elif option == 2:
        menuGestionReportes(listaTrabajadores)
    elif option == 3:
        menuStatus(listaTrabajadores)
    elif option == 0:
        finalizo()
        break
    else:
        print("")
        print(">>> OPCION INVALIDA <<<")
        time.sleep(1)