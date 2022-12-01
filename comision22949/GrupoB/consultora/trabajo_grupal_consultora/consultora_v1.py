
from modulo import ingreso_trabajador, decorar, encuentra_lineas, eliminar_linea, mostrar_dato, imp_lista, lista_por_edad, modificarDatos, busqueda_por_dni, controlErrores, controlErrorNumero, controlErrordni
print()

# decoracion de 2 lineas, mensaje de binvenida y otras 2 lineas
decorar("#", "=", "s")
print('''\t ┌─────────────── •✧✧• ────────────────────┐
            Bienvenido a la consultora de trabajo  
         └─────────────── •✧✧• ────────────────────┘ ''')
decorar("=", "#")

while True:  # bucle del 1er menú e ingreso de opcion
    # idea: agregar la experiencia del trabajador!!!
    opcion = controlErrores('''                           
    Ingrese el numero de una de las siguientes opciones:

    1)Gestion de trabajadores
    2)Reportes
    0)Para salir del menú
    ==> ''', "\t Ingrese una opcion valida!!!!", 3)

    if opcion == 0:
        decorar("#", "=", "s")  # opcion "0" para salir
        print('''\t ┌─────────────── •✧✧• ────────────────────┐
                    Hasta la proxima  
         └─────────────── •✧✧• ────────────────────┘ ''')
        decorar("#", "=")
        break
    elif opcion == 1:  # opcion "1" gestion de trabajadores
        while True:
            # bucle del sub menu "gestion de trabajadores"
            decorar("#", "=", "s")
            opcion1 = controlErrores('''                           
    Ingrese el numero de una de las siguientes opciones:

    1)Ver listado completo
    2)Ingresar nuevo trabajador
    3)Modificar datos de trabajador
    4)Eliminar datos de trabajador
    0)Para volver al menú principal
    ==> ''', "\t Ingrese una opcion valida!!!!", 5)

            if opcion1 == 0:
                # opcion "0" para volver al menu principal
                decorar("#", "=", "s")
                break

            elif opcion1 == 1:
                print("\tLista de todos los trabajadores en la base de datos")
                lista_completa = mostrar_dato("trabajadores.dat")
                imp_lista(lista_completa)
                input("\nPresione enter para continuar...")
                decorar("#", "=", "s")
                continue

            # opcion "2" ingreso datos del trabajador(funcionando)
            elif opcion1 == 2:
                print("\tIngreso de datos del trabajador")
                ingreso_trabajador("trabajadores.dat")
                input("Presione enter para continuar...")
                decorar("#", "=", "s")
                continue

            # opcion "3" modificar datos del trabajador(funcionando)
            elif opcion1 == 3:
                print("\tModificar registro de trabajador")
                dni = controlErrordni("Ingrese el dni del trabajador:==> ")
                lista_completa = mostrar_dato("trabajadores.dat")
                modificarDatos("trabajadores.dat", lista_completa, dni)
                input("Presione enter para continuar...")
                decorar("#", "=", "s")
                continue

            # opcion "4" elimina datos del trabajador(funcionando)
            elif opcion1 == 4:
                print("\tEliminar registro del trabajador:")
                dni = controlErrordni("Ingrese el dni del trabajador:==> ")
                trabajador_a_eliminar = mostrar_dato(
                    "trabajadores.dat", 2, str(dni))
                imp_lista(trabajador_a_eliminar)
                eliminar = input(
                    "Esta seguro que desea eliminar los datos del trabajador? s/n... ").capitalize()
                if eliminar == "S":
                    linea_a_eliminar = encuentra_lineas(
                        "trabajadores.dat", dni)
                    eliminar_linea("trabajadores.dat", linea_a_eliminar)
                    input("Presione enter para continuar...")
                    decorar("#", "=", "s")
                    continue
                else:
                    decorar("#", "=", "s")
                    continue

    elif opcion == 2:  # opcion "2" menu principal: reportes
        while True:  # bucle del sub menu "reportes"
            decorar("#", "=", "s")
            opcion1 = controlErrores('''                           
    Ingrese el numero de una de las siguientes opciones:

    1)Mostrar trabajadores activos
    2)Mostrar trabajadores desocupados
    3)Mostrar trabajadores desocupados en un rango de edad
    4)Mostrar trabajadores segun la profecion
    0)Para volver al menú principal
    ==> ''', "\t Ingrese una opcion valida!!!!", 5)
            if opcion1 == 0:
                # vuelve al menú principal
                decorar("#", "=", "s")
                break

            # muestra trabajadores activos(funcionando)
            elif opcion1 == 1:
                lista_activos = mostrar_dato("trabajadores.dat", 4, "True")
                imp_lista(lista_activos)
                input("\nPresione enter para continuar...")
                decorar("#", "=", "s")
                continue

            elif opcion1 == 2:
                # muestra trabajadores inactivos(funcionando)
                lista_desocupados = mostrar_dato(
                    "trabajadores.dat", 4, "False")
                imp_lista(lista_desocupados)
                input("\nPresione enter para continuar...")
                decorar("#", "=", "s")
                continue

            # Mostrar trabajadores desocupados en un rango de edad(funcionando)
            elif opcion1 == 3:
                lista = mostrar_dato("trabajadores.dat", 4, "False")
                lista_final = lista_por_edad(lista)
                imp_lista(lista_final)
                input("\nPresione enter para continuar...")
                decorar("#", "=", "s")
                continue

            # muestra trabajadores por profesion(funcionando)
            elif opcion1 == 4:
                profesion = input("Ingrese la profesión buscada: ")
                lista_profeciones = mostrar_dato(
                    "trabajadores.dat", 3, profesion)
                imp_lista(lista_profeciones)
                input("\nPresione enter para continuar...")
                decorar("#", "=", "s")
                continue
