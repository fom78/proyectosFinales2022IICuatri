
from decoraciones import decorar
from validaciones import validarIngresoEntero
from ABMtrabajadores import obtenerTrabajadores, agregarTrabajadores, modificarTrabajador, eliminarTrabajador, modificarEstadoTrabajador, salida
from compara import comparaTrue, comparaFalse

listadoTrabajadores = obtenerTrabajadores("trabajadores.txt")
print(listadoTrabajadores)

while True:

    print(
        '''
        [1] Gestión de trabajadores
        [2] Reportes
        [3] Cambiar estado trabajador
        [0] Salir
        
        '''
    )

    opcion = validarIngresoEntero("Ingrese una opción (cero para salir): ")

    if opcion == 0:
        break

    elif opcion == 1: # Gestion trabajadores
        while True:
            print(
            '''
            [1] Ingresar un nuevo trabajador
            [2] Modificar dato de trabajador
            [3] Eliminar trabajador
            [0] Volver al menú principal
        
            '''
            )        
            op = validarIngresoEntero("Ingrese una opción: ")
            
            if op == 1:
                decorar()
                print("[1] Ingresar un trabajador")
                agregarTrabajadores(listadoTrabajadores)

            elif op == 2:
                decorar()
                print("[2] Modificar dato de trabajador")
                dni=validarIngresoEntero("DNI del trabajador a modificar: ")
                modificarTrabajador(listadoTrabajadores, dni)

            elif op == 3:
                decorar()
                print("[3] Eliminar trabajador")
                dni=validarIngresoEntero("DNI del trabajador a eliminar: ")
                eliminarTrabajador(listadoTrabajadores, dni)

            elif op == 0:
                print("[0] Volver al menu principal")
                break
        
    elif opcion == 2: #  Reportes
        while True:
            print(
            '''
            [1] Mostrar trabajadores activos
            [2] Mostrar trabajadores desocupados
            [3] Mostrar desocupados en un rango de edad
            [4] Mostrar trabajadores según la profesión
            [5] Volver al menu principal
        
            '''
            )        
            opc = validarIngresoEntero("Ingrese una opción: ")

            if opc == 1: # trabajadores activos
                decorar()
                print("[1] Mostrar trabajadores activos")
                comparaTrue(listadoTrabajadores)
                                                        
            elif opc == 2: # trabajadores desocupados
                decorar()
                print("[2] Mostrar trabajadores desocupados")
                comparaFalse(listadoTrabajadores)
                                    
            elif opc == 3: # desocupados con un rango de edad
                decorar()
                print("[3] Mostrar desopupados en un rango de edad")
                edadMin = int(input("Ingrese la edad mínima: "))
                edadMax = int(input("Ingese la edad máxima: "))
                
                for trab in listadoTrabajadores:
                    if trab["edad"] in range (edadMin, edadMax + 1) and trab["estado"] == "False":
                        salida(trab)
                
            elif opc == 4: # trabajadores segun profesion
                decorar()
                print("[4] Mostrar trabajadores según profesion")
                prof = input("Ingrese una profesión: ")
                for trab in listadoTrabajadores:
                    if trab["profesion"] == prof:
                        salida(trab)

            elif opc == 5:
                print("[5] Volver al menu principal")
                break
    
    elif opcion == 3:
        decorar()
        print("[3] Cambiar status del trabajador")
        dni=validarIngresoEntero("DNI del trabajador a cambiar status: ")
        modificarEstadoTrabajador(listadoTrabajadores, dni)
          
    else:
        print("Ingrese una opción válida.")

print(listadoTrabajadores)
print("Fin del programa")