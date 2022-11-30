import os
from tryExcept import tryExceptOptions, matchLetras, apertura


def trabajadorActivo():
    os.system("cls")
    print("Mostrar trabajadores Activos")
    archivo = apertura("trabajadores.dat", "r")
    for line1 in archivo:
        line2 = line1.strip().replace("\n", "")
        line3 = line2.split(',')
        if line3[4] == "True":
            print(f'''
            Nombre: {line3[1]}
            Edad: {line3[2]}
            Profesion: {line3[3]}
            ''')
    archivo.close()


def trabajadorDesocupados():
    os.system("cls")
    print("Mostrar trabajadores Desocupados")
    archivo = apertura("trabajadores.dat", "r")
    for line1 in archivo:
        line2 = line1.strip().replace("\n", "")
        line3 = line2.split(',')
        if line3[4] == "False":
            print(f'''
            Nombre: {line3[1]}
            Edad: {line3[2]}
            Profesion: {line3[3]}
            ''')

    archivo.close()


def trabajadorRangoEdad():
    os.system("cls")
    print("Mostrar Desocupados en un rango de edad")
    edadMinima = tryExceptOptions("Edad minima: ")
    edadMaxima = tryExceptOptions("Edad maxima: ")
    archivo = apertura("trabajadores.dat", "r")
    for line1 in archivo:
        line2 = line1.strip().replace("\n", "")
        line3 = line2.split(',')
        if line3[4] == "False" and int(line3[2]) >= edadMinima and int(line3[2]) <= edadMaxima:
            print(f'''
            Nombre: {line3[1]}
            Edad: {line3[2]}
            Profesion: {line3[3]}
            ''')

    archivo.close()


def trabajadorProfesion():
    os.system("cls")
    print("Mostrar trabajadores según su Profesión")
    profesion = matchLetras("Profesion: ")
    archivo = apertura("trabajadores.dat", "r")
    for line1 in archivo:
        line2 = line1.strip().replace("\n", "")
        line3 = line2.split(',')
        if line3[3] == profesion:
            print(f'''
            Nombre: {line3[1]}
            Edad: {line3[2]}
            Profesion: {line3[3]}
            ''')

    archivo.close()
