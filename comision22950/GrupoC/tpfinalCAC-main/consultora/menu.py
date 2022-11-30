from excepcion import correccionErrores
import crud

while True:
    print(f'''
        Menu:
        [1] Gestion de Trabajadores
        [2] Reportes
        [3] Cambiar status trabajador
        [0] Salir
        ''')

    opcion = correccionErrores()
    
    if (opcion == 0):
        break
    elif (opcion == 1):

        while True:
            print(f'''
            Gestion de Trabajadores:
            [1] Ingresar nuevo Trabajador
            [2] Modificar datos de un trabajador
            [3] Eliminar Trabajador
            [0] Salir
        ''')

            opcion = correccionErrores()

            if (opcion == 0):
                break
            elif (opcion == 1):
                print('Complete los datos para ingresar nuevo Trabajador:')
                crud.agregarTrabajador()
            elif (opcion == 2):
                print('Modificar trabajador:')
                crud.modificar("trabajadores.dat")
            elif (opcion == 3):
                print('Eliminar Trabajador:')
                crud.eliminarTrabajador("trabajadores.dat")

    
    elif (opcion == 2):
        while True:
            print(f'''
                Reportes:
                [1] Mostrar trabajadores Activos
                [2] Mostrar trabajadores desocupados
                [3] Mostrar desocupados en un rango de edad
                [4] Mostrar trabajadores segun la profesion
                [0] Salir
            ''')
    
            opcion = correccionErrores()
            if (opcion == 0):
                break
            elif (opcion == 1):
                print('Mostrar trabajadores Activos')
                crud.armarReporte('trabajadores.dat', 'Activo', 'True')
            elif (opcion == 2):
                print('Mostrar trabajadores desocupados')
                crud.armarReporte('trabajadores.dat','Activo', 'False')
            elif (opcion == 3):
                print('Mostrar desocupados en un rango de edad')
                crud.armarReporteEdad('trabajadores.dat','Activo', 'False', 'Edad')
            elif (opcion == 4):
                print('Mostrar trabajadores segun la profesion')
                crud.armarReporteProfesion('trabajadores.dat','Profesion',)
            else:
                print('Ingresa una opcion valida')
    
    elif (opcion == 3):
        print('Cambiar status trabajador: ')
    else:
        print('Ingresa una opcion valida')
