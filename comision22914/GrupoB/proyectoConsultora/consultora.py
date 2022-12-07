
archivo = open("trabajadores.txt", "a")

trabajadores = []
while True:

    print(
        '''
        [1] Gestión de trabajadores
        [2] Reportes
        [3] Cambiar estado trabajador
        [0] Salir
        
        '''
    )

    opcion = int(input("Ingrese una opción (cero para salir): "))

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
            op = int(input("Ingrese una opción: "))
            
            if op == 1:
                dni = int(input("DNI: "))
                nombre = input("Nombre: ")
                edad = int(input("Edad: "))
                profesion = input("Profesión: ")
                activo = input("Activo? (s/n): ")
                if activo == "s":
                    activo = True
                else:
                    activo = False
                data = {"dni": dni, "Nombre":nombre, "Edad":edad, "Profesion":profesion, "Activo": activo}
                trabajadores.append(data)
                datos = f"\n{dni}, {nombre}, {edad}, {profesion}, {activo}"
                archivo.write(datos)

            elif op == 2:
                print("Opcion 2")

            elif op == 3:
                print("Opcion 3") 

            elif op == 0:
                break
                print("Volver al menu principal")
        
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
            opc = int(input("Ingrese una opción: "))

            if opc == 1: # trabajadores activos
                for usu in trabajadores:
                    if usu[3] == True:
                        print(usu)
            
            elif opc == 2: # trabajadores desocupados
                print("Opcion 2")
                for usu in trabajadores:
                    if usu[3] == False:
                        print(usu)

            elif opc == 3: # desocupados con un rango de edad
                edadMin = int(input("Ingrese la edad mínima: "))
                edadMax = int(input("Ingese la edad máxima"))
                for usu in trabajadores:
                    if usu[1] in range(edadMin, edadMax + 1):
                        print(usu)
                print("Opcion 3") 

            elif opc == 3: # trabajadores segun profesion
                profesion = input("Profesión a buscar: ")
                for usu in trabajadores:
                    if usu[2] == profesion:
                        print(usu)
                print("Opcion 4") 

            elif opc == 5:
                print("Volver al menu principal")
                break
    
    elif opcion == 3:
        print("Eliminar trabajador")  
        
    else:
        print("Ingrese una opción válida.")

print("Fin del programa")

archivo.close()