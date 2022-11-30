from defgestion import transformarArchivos, agregarEmpleado
from controlerrores import controlErrornumerico
from decoraciones import tablaActivos, tablaInactivos,tablabusprof,menuPrin,menuGestion,menuReportes,tablaListaTrabajadores
import os
from time import sleep
from colorama import Style,Fore, init
init()

diccEmpleados=transformarArchivos("BDempleados.txt")

while True:
    menuPrin()
    print("")
    opcion= controlErrornumerico(leyenda="SELECCIONE UNA OPCION: ", msjError="INGRESE UN NÚMERO [1],[2] o [0] PARA SALIR")
    os.system("cls")
    match (opcion):
        case 1:
              while True:            
               menuGestion()
               print("")
               opcion= controlErrornumerico(leyenda="SELECCIONE UNA OPCION: ", msjError="INGRESE UN NÚMERO [1],[2],[3],[4] o [0] PARA VOLVER")
               os.system("cls")
               match (opcion):
                    case 1:
                         
                          agregarEmpleado(diccEmpleados)
                          
                    case 2:
                          print ("ACA MODIFICA DATOS")
                    case 3:
                          print ("ACA ELIMINA DATOS")
                    case 4:
                          print ("CAMBIAR STATUS")        

                    case 0: 
                          break 
                    case _:
                           print(Fore.RED+Style.BRIGHT+"¡¡OPCIÓN INEXISTENTE!!"+Fore.GREEN+"...Return Menu"+Style.NORMAL)  
                           sleep(3)
        case 2:#REPORTES
             while True:            
               menuReportes()
               print("")
               opcion= controlErrornumerico(leyenda="SELECCIONE UNA OPCION: ", msjError="INGRESE UN NÚMERO [1],[2],[3],[4],[5] o [0] PARA VOLVER")
               os.system("cls")
               match (opcion):
                             case 0:
                                   #volver
                                   break 
                             case 1:
                                    #trabajadores activos
                                    diccEmpleados=transformarArchivos("BDempleados.txt")
                                    tablaActivos(diccEmpleados)
                                    print("")
                                    enter=input(Fore.RED+"PRESIONE ENTER PARA VOLVER AL MENU_")
                                    os.system("cls")
                                   
                                    
                             case 2:
                                    #trabajadores desocupados
                                    diccEmpleados=transformarArchivos("BDempleados.txt")
                                    tablaInactivos(diccEmpleados)
                                    print("")
                                    enter=input(Fore.RED+"PRESIONE ENTER PARA VOLVER AL MENU_")
                                    os.system("cls")
                                    
                             case 3:
                                   print ("ACA VA DESOCUPADOS SEGUN RANGO")  
                             case 4:
                                   #busqueda por profesion
                                   diccEmpleados=transformarArchivos("BDempleados.txt")
                                   tablabusprof(diccEmpleados)
                                   print("")
                                   enter=input(Fore.RED+"PRESIONE ENTER PARA VOLVER AL MENU_")
                                   os.system("cls")
                             case 5:
                                    #lista trabajadores
                                    diccEmpleados=transformarArchivos("BDempleados.txt")
                                    tablaListaTrabajadores(diccEmpleados)
                                    print("")
                                    enter=input(Fore.RED+"PRESIONE ENTER PARA VOLVER AL MENU_")
                                    os.system("cls")
                             case _:
                                    print(Fore.RED+Style.BRIGHT+"¡¡OPCIÓN INEXISTENTE!!"+Fore.GREEN+"...Return Menu"+Style.NORMAL)  
                                    sleep(3)        

        
                   
        case 0:
               break 
        case _:
                 print(Fore.RED+Style.BRIGHT+"¡¡OPCIÓN INEXISTENTE!!"+Fore.GREEN+"...Return Menu"+Style.NORMAL)  
                 sleep(3)
              
