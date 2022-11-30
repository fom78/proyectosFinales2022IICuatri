import os
from tryExcept import tryExceptOptions, tryExceptNumero, matchLetras, apertura


def altaTrabajador():
    os.system("cls")
    print("Ingresar nuevo trabajador")
    archivo = apertura("trabajadores.dat", "a")
    dni = tryExceptOptions("Ingrese DNI: ")
    nombre = matchLetras("Ingrese nombre: ")
    edad = tryExceptOptions("Ingrese la edad: ")
    profesion = matchLetras("Ingrese su profesión: ")

    activo = input("Actualmente, está trabajando? (s/n):")
    if activo == "s" or activo == "S":
        activo = True
    else:
        activo = False

    print(dni, nombre, edad, profesion, activo)
    linea = f"{dni},{nombre},{edad},{profesion},{activo}\n"
    archivo.write(linea)
    archivo.close()


def modificarTrabajador():
    os.system("cls")
    print("Modificar datos de un trabajador")
    dni = tryExceptOptions("Ingrese DNI del trabajador a modificar: ")
    with open("trabajadores.dat", "r") as archivo:
        modificar = ""

        for line1 in archivo:

            # quita espacios en blanco y salto de linea
            line2 = line1.strip().replace("\n", "")
            line3 = line2.split(',')
            if line3[0] == str(dni):  # busca por DNI

                nombre = matchLetras(
                    f"Modificar nombre de {line3[1]}? \n Ingrese:  ")
                if nombre:
                    line2 = line2.replace(line3[1], nombre)

                edad = tryExceptNumero(
                    f"La edad del Trabajador es {line3[2]}. Modificar? \n Ingrese: ")
                if edad:
                    line2 = line2.replace(line3[2], edad)

                profesion = matchLetras(
                    f"La profesión del trabajador es {line3[3]}. Modificar? \n Ingrese: ")
                if profesion:
                    line2 = line2.replace(line3[3], profesion)

                activo = input("Actualmente, está trabajando? (s/n): ")
                if activo == "s" or activo == "S":
                    line2 = line2.replace(line3[4], 'True')
                else:
                    line2 = line2.replace(line3[4], 'False')

                modificar = modificar + line2 + "\n"

            else:
                modificar = modificar + line2 + "\n"

    archivo.close()
    registroActualizado = apertura("trabajadores.dat", "w")
    registroActualizado.write(modificar)
    registroActualizado.close()


def eliminarTrabajador():
    os.system("cls")
    print("Eliminar trabajador")

    archivo = open("trabajadores.dat", "r")
    dni = tryExceptOptions("Ingrese DNI del trabajador que quiere eliminar: ")
    with open("trabajadores.dat", "r") as archivo:
        modificar = ""

        for line1 in archivo:

            # quita espacios en blanco y salto de linea
            line2 = line1.strip().replace("\n", "")
            line3 = line2.split(',')
            if line3[0] != str(dni):  # busca por DNI
                modificar = modificar + line2 + "\n"
                
        archivo.close()
        registroActualizado = open("trabajadores.dat", "w")
        registroActualizado.write(modificar)
        registroActualizado.close()
        print(f"El trbajador {dni} fue eliminado")
      

        


def status():
    os.system("cls")
    print(" Cambiar status del trabajador \n")
    dni = tryExceptOptions("Ingrese DNI del trabajador a modificar:")
    with open("trabajadores.dat", "r") as archivo:
        modificar = ""

        for line1 in archivo:
            # quita espacios en blanco y salto de linea
            line2 = line1.strip().replace("\n", "")
            line3 = line2.split(',')

            if line3[0] == str(dni):  # busca por DNI
                if line3[4] == 'True':
                    nueva_linea = line2.replace("True", "False")
                    modificar = modificar + nueva_linea + "\n"
                else:
                    nueva_linea = line2.replace("False", "True")
                    modificar = modificar + nueva_linea + "\n"

            else:
                modificar = modificar + line2 + "\n"

        archivo.close()
        registroActualizado = apertura("trabajadores.dat", "w")
        registroActualizado.write(modificar)
        registroActualizado.close()
    