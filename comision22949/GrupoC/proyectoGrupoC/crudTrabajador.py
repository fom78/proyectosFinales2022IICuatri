"""Este modulo contiene funciones para Alta-Baja-Modificacion del Trabajador"""
from controlErrores import validarOpcion, validarCaracter, validarCadena
import os
from time import time, sleep
from vista import decorarListaTrabajador


def obtenerTrabajadores(nombreArchivo): #recibe el nombre de archivo "Trabajadores.dat"
  #respuestaUsuario=None
  try:

    if os.stat(nombreArchivo).st_size == 0: # Este metodo comprueba si el archivo contiene datos evaluado byte.
        print(f"El archivo {nombreArchivo} se encuentra vacio")
        print("Presione |Enter| para volver al menu principal")
    else:
        archivo = open(nombreArchivo,"r")
        print("cargando el listado")
        sleep(1)
        #print(archivo.read())
        listaDeTrabajadores=[]
        for linea in archivo.readlines():
            # print(linea)
            trabajador=linea.replace('\n','') #5Pez4
            trabajador=trabajador.split(",") # ["5Pez4"] >> ["5","Pez","4"] ['']
            trabajador = {
                "nombre":trabajador[0],
                "apellido":trabajador[1],
                "edad":trabajador[2],
                "dni":trabajador[3],
                "profesion":trabajador[4],
                "estadoactual":trabajador[5]
                }
            listaDeTrabajadores.append(trabajador)
        archivo.close()

  except FileNotFoundError:
    print("El archivo no existe para mostrar")
    respuestaUsuario= validarCaracter("""Desea ingresar un trabajador a la base de datos ?
    Presione |S| para agregar o |N| para volver al menu principal: """)
    if respuestaUsuario == 'S':
       agregarTrabajador(nombreArchivo)
    elif respuestaUsuario == 'N':
       print("volviendo al menu principal")
  return listaDeTrabajadores


def agregarTrabajador(nombreArchivo):

    listadoTrabajadores=[]
    nombre = validarCadena("Ingrese el nombre: ")
    apellido= validarCadena("Ingrese el apellido: ")
    edad=validarOpcion("Ingrese la edad del trabajador: ")
    dni=validarOpcion("Ingrese el documento de identidad: ")
    profesion=validarCadena("Ingrese la profesion: ")
    estadoactual=validarCaracter("Situacion Laboral? presione |S| para empleado |N| para desempleado ")
    perfilTrabajador={
        "nombre":nombre,
        "apellido":apellido,
        "edad":edad,
        "dni":dni,
        "profesion":profesion,
        "estadoactual":estadoactual,
    }
    listadoTrabajadores.append(perfilTrabajador)

    archivo= open (nombreArchivo,"a")
    datosTrabajador=f"{nombre},{apellido},{edad},{dni},{profesion},{estadoactual}\n"
    archivo.write(datosTrabajador)
    archivo.close()
    print("El trabajador se ha ingresado correctamente")


def modificarTrabajador(listadoTrabajadores, dniTrabajador):
    var=0 #variable para salir del bucle while
    while var==0: #este bucle sirve para volver a preguntar si el trabajador encontrado es el correcto (línea 78)
        for trabajador in listadoTrabajadores:
            if trabajador["dni"] == dniTrabajador:
                    pregunta = input(f"El trabajador que está buscando es: {trabajador['nombre']} {trabajador['apellido']}? |S| o |N|: ")
                    if pregunta.upper() == "N":
                        dniTrabajador = input("Ingrese nuevamente el dni del trabajador: ")
                    elif pregunta.upper() == "S":
                        print(f'''
                        ###########################
                        ¡¡¡Trabajador encontrado!!!
                        ###########################
                        ''')
                        while True: #modificar nombre
                            opcionNombre = input("Desea modificar el nombre del trabajador? |S| para SÍ - |N| para NO: ")
                            if opcionNombre.upper() == "S":
                                nombreNuevo = input("Ingrese el nombre del trabajador: ")
                                trabajador["nombre"] = nombreNuevo
                                print(trabajador)
                                break
                            elif opcionNombre.upper() == "N":
                                print(f'''
                                ----No se modificó el nombre----
                                ''')
                                break
                            else:
                                print("Ingrese una opción válida")
                        while True: #modificar apellido
                            opcionApellido = input("Desea modificar el apellido del trabajador? |S| para SÍ - |N| para NO: ")
                            if opcionApellido.upper() == "S":
                                apellidoNuevo = input("Ingrese el apellido del trabajador: ")
                                trabajador["apellido"] = apellidoNuevo
                                break
                            elif opcionApellido.upper() == "N":
                                print(f'''
                                ----No se modificó el apellido----
                                ''')
                                break
                            else:
                                print("Ingrese una opción válida")
                        while True: #modificar edad
                            opcionEdad = input("Desea modificar la edad del trabajador? |S| para SÍ - |N| para NO: ")
                            if opcionEdad.upper() == "S":
                                edadNueva = input("Ingrese la edad del trabajador: ")
                                trabajador["Edad"] = edadNueva
                                break
                            elif opcionEdad.upper() == "N":
                                print(f'''
                                ----No se modificó la edad----
                                ''')
                                break
                            else:
                                print("Ingrese una opción válida")
                        while True: #modificar profesion
                            opcionProfesion = input("Desea modificar la profesión del trabajador? |S| para SÍ - |N| para NO: ")
                            if opcionProfesion.upper() == "S":
                                profesionNueva = input("Ingrese la profesion: ")
                                trabajador["profesion"] = profesionNueva
                                break
                            elif opcionProfesion.upper() == "N":
                                print(f'''
                                ----No se modificó la profesión actual----
                                ''')
                                print("### Estás siendo redirigido al menú principal ###")
                                sleep(3)
                                os.system("cls")
                                break
                            else:
                                print("Ingrese una opción válida")
                        var=1 #salida del bucle while
                    else:
                        print("Ingrese una opción correcta")
                        os.system("cls")

    trabajadores = open("Trabajadores.dat","w") #modificar datos en el archivo
    datos = []
    for trabajador in listadoTrabajadores:
        datosTrabajador = f"\n{trabajador['nombre']},{trabajador['apellido']},{trabajador['edad']},{trabajador['dni']},{trabajador['profesion']},{trabajador['estadoactual']}"
        datos.append(datosTrabajador)
    datos[0] = datos[0].replace("\n", "")
    trabajadores.writelines(datos)
    trabajadores.close()
