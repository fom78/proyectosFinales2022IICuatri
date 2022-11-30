from colorama import Back,Fore,init
init()

def tablaActivos(dicc):
    print("")
    print("")
    print(Fore.CYAN+            "+-----------------------------------------------+")  
    print(Back.CYAN+Fore.WHITE+ "|         REPORTE:TRABAJADORES ACTIVOS          |"+Back.RESET)
    print(Back.CYAN+Fore.WHITE+ "+--------------------+---------------+----------+"+Back.RESET)
    print(Back.CYAN+Fore.WHITE+ "|NOMBRE Y APELLIDO   |PROFESIÓN      |ACTIVO    |"+Back.RESET)
    print(Fore.CYAN+            "+--------------------+---------------+----------+")
    for empleado in dicc:
        if empleado["Activo"]=="True":
           activo=empleado["Activo"]
           nom= empleado["NomyApe"] 
           prof= empleado["Profesion"]
           cadena= Fore.CYAN+"|{:<20}|{:<15}|{:<10}|".format(nom,prof,activo)
           print (cadena)
           print(Fore.CYAN+"+--------------------+---------------+----------+"+Fore.RESET)

def tablaInactivos(dicc):
    print("")
    print("") 
    print(Fore.CYAN+              "+-----------------------------------------------+")  
    print(Back.CYAN+Fore.WHITE+   "|        REPORTE:TRABAJADORES INACTIVOS         |"+Back.RESET)
    print(Back.CYAN+Fore.WHITE+   "+--------------------+---------------+----------+"+Back.RESET)
    print(Back.CYAN+Fore.WHITE+   "|NOMBRE Y APELLIDO   |PROFESIÓN      |ACTIVO    |"+Back.RESET)
    print(Fore.CYAN+              "+--------------------+---------------+----------+")
    for empleado in dicc:
         if empleado["Activo"]=="False":
            activo=empleado["Activo"]
            nom= empleado["NomyApe"] 
            prof= empleado["Profesion"]
            cadena =Fore.CYAN+("|{:<20}|{:<15}|{:<10}|").format(nom,prof,activo)
            print (cadena)
            print(Fore.CYAN+ "+--------------------+---------------+----------+"+Fore.RESET)   
             


def tablabusprof(dicc): 
    print("")
    prof=input("INGRESE EL NOMBRE DE LA PROFESIÓN A BUSCAR: ")
    print("")
    print(Fore.CYAN+            "+------------------------------------------------------------------------------------------+")  
    print(Back.CYAN+Fore.WHITE+ "|                         REPORTE:BUSQUEDA DE TRABAJADORES POR PROFESIÓN                   |"+Back.RESET)
    print(Back.CYAN+Fore.WHITE+ "+--------------------+----------+----------+--------------------+---------------+----------+"+Back.RESET)
    print(Back.CYAN+Fore.WHITE+ "|NOMBRE Y APELLIDO   |EDAD      |DNI       |LOCALIDAD           |PROFESIÓN      |ACTIVO    |"+Back.RESET)
    print(Fore.CYAN+            "+--------------------+----------+----------+--------------------+---------------+----------+") 
    for empleado in dicc:
        if prof.title()==empleado["Profesion"]:
           nombre = empleado["NomyApe"]
           edad =empleado["Edad"]
           dni=empleado["Dni"]
           localidad=empleado["Localidad"]
           profesion=empleado["Profesion"]
           activo=empleado["Activo"]
           cadena = Fore.CYAN+"|{:<20}|{:<10}|{:<10}|{:<20}|{:<15}|{:<10}|".format(nombre,edad,dni,localidad,profesion,activo)
           print(cadena)
           print(Fore.CYAN+"+--------------------+----------+----------+--------------------+---------------+----------+"+Fore.RESET)

def menuPrin():
   print("")
   print("")
   print(Fore.CYAN+           "+---------------------------------------------+")  
   print(Back.CYAN+Fore.WHITE+"|               MENU PRINCIPAL:               |"+Back.RESET) 
   print(Fore.CYAN+           "+---------------------------------------------+")
   print(Fore.CYAN+           "|         -[1]GESTION DE TRABAJADORES         |")
   print(Fore.CYAN+           "|         -[2]REPORTES                        |")
   print(Fore.CYAN+           "|         -[0]SALIR                           |")
   print(Fore.CYAN+           "+---------------------------------------------+"+Fore.RESET)


def menuGestion():
    print("")
    print("")
    print(Fore.CYAN+           "+---------------------------------------------+")  
    print(Back.CYAN+Fore.WHITE+"|         [1]MENU GESTION TRABAJADORES:       |"+Back.RESET) 
    print(Fore.CYAN+           "+---------------------------------------------+")
    print(Fore.CYAN+           "|        -[1]INGRESAR NUEVO TRABAJADOR        |")
    print(Fore.CYAN+           "|        -[2]MODIFICAR DATOS TRABAJADOR       |")
    print(Fore.CYAN+           "|        -[3]ELIMINAR TRABAJADOR              |")
    print(Fore.CYAN+           "|        -[4]MODIFICAR STATUS TRABAJADOR      |")
    print(Fore.CYAN+           "|        -[0]VOLVER MENU PRINCIPAL            |")
    print(Fore.CYAN+           "+---------------------------------------------+"+Fore.RESET)
       


def menuReportes():
    print("")
    print("")
    print(Fore.CYAN+           "+---------------------------------------------+")  
    print(Back.CYAN+Fore.WHITE+"|              [2]MENU REPORTES:              |"+Back.RESET) 
    print(Fore.CYAN+           "+---------------------------------------------+")
    print(Fore.CYAN+           "|     -[1]MOSTRAR TRABAJADORES ACTIVOS        |")
    print(Fore.CYAN+           "|     -[2]MOSTRAR TRABAJADORES DESOCUPADOS    |")
    print(Fore.CYAN+           "|     -[3]DESCOUPADOS EN UN RANGO DE EDAD     |")
    print(Fore.CYAN+           "|     -[4]TRABAJADORES SEGUN LA PROFESIÓN     |")
    print(Fore.CYAN+           "|     -[5]LISTA TRABAJADORES                  |")
    print(Fore.CYAN+           "|     -[0]VOLVER MENU PRINCIPAL               |")
    print(Fore.CYAN+           "+---------------------------------------------+"+Fore.RESET)


def tablaListaTrabajadores(dicc):
    print("")
    print("")
    print(Fore.CYAN+           "+------------------------------------------------------------------------------------------+")  
    print(Back.CYAN+Fore.WHITE+"|                         REPORTE:LISTA DE TRABAJADORES COMPLETA                           |"+Back.RESET)
    print(Back.CYAN+Fore.WHITE+"+--------------------+----------+----------+--------------------+---------------+----------+"+Back.RESET)
    print(Back.CYAN+Fore.WHITE+"|NOMBRE Y APELLIDO   |EDAD      |DNI       |LOCALIDAD           |PROFESIÓN      |ACTIVO    |"+Back.RESET)
    print(Fore.CYAN+           "+--------------------+----------+----------+--------------------+---------------+----------+")
    for empleado in dicc:
        nombre = empleado["NomyApe"]
        edad =empleado["Edad"]
        dni=empleado["Dni"]
        localidad=empleado["Localidad"]
        profesion=empleado["Profesion"]
        activo=empleado["Activo"]
        cadena =Fore.CYAN+"|{:<20}|{:<10}|{:<10}|{:<20}|{:<15}|{:<10}|".format(nombre, edad,dni,localidad,profesion,activo)
        print(cadena)
        print(Fore.CYAN+"+--------------------+----------+----------+--------------------+---------------+----------+"+Fore.RESET)




