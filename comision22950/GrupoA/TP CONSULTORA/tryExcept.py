import re

def apertura(file, modo):
    try:
        archivo = open(file, modo)
        return archivo
    except FileNotFoundError:
        print('No se puede leer el Archivo!')


def tryExceptOptions(mensaje="Elija una opcion: "):
    while True:
        try:
            opcion = int(input(mensaje))
            break
        except ValueError:
            print('\n\tALERTA: Ingresa un numero valido!\n')

    return opcion


def tryExceptNumero(mensaje):
    opcion = ''
    while True:
        try:
            ingreso = input(mensaje)
            if ingreso:
                opcion = int(ingreso)
                break
            else:
                break
        except ValueError:
            print('\n\tALERTA: Ingresa un numero valido!\n')

    return str(opcion)


def matchLetras(mensaje):
    while True:
        nombre = input(mensaje)
        # solo letras
        if re.match("^[A-Za-z áéíóúÁÉÍÓÚñÑ]*$", nombre):
            return nombre
            break
        else:
            print('\n\tALERTA: Ingresa no valido!\n')
